import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

import sys
# sys.path.append(r"C:\Program Files\Dynamo 0.8")
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


import System
from System import Array
from System.Collections.Generic import *

import re
from re import *

doc = DocumentManager.Instance.CurrentDBDocument


def ProcessList(_func, _list):
	return map(
		lambda x: ProcessList(_func, x)
		if type(x) == list else _func(x),
		_list)


def Unwrap(_item):
	if isinstance(_item, list):
		return ProcessList(Unwrap, _item)
	else:
		return UnwrapElement(_item)


def GetParVal(elem, name):
	# Параметр пользовательский
	try:
		param = elem.LookupParameter(name)
		storeType = param.StorageType
		if storeType == StorageType.String:
			value = elem.LookupParameter(name).AsString()
		elif storeType == StorageType.Integer:
			value = elem.LookupParameter(name).AsDouble()
		elif storeType == StorageType.Double:
			value = elem.LookupParameter(name).AsDouble()
	# Параметр встроенный
	except:
		bip = GetBuiltInParam(name)
		storeType = elem.get_Parameter(bip).StorageType
		if storeType == StorageType.String:
			value = elem.get_Parameter(bip).AsString()
		elif storeType == StorageType.Integer:
			value = elem.get_Parameter(bip).AsDouble()
		elif storeType == StorageType.Double:
			value = elem.get_Parameter(bip).AsDouble()
	return value


def GetBuiltInParam(paramName):
	builtInParams = System.Enum.GetValues(BuiltInParameter)
	param = []
	for i in builtInParams:
		if i.ToString() == paramName:
			param.append(i)
			break
		else:
			continue
	return param[0]


def SetpParVal(elem, name, pValue):
	global doc
	elem.LookupParameter(name).Set(pValue)
	return elem


def getByCatAndStrParam(_bic, _bip, _val, _isType):
	global doc
	if _isType:
		fnrvStr = FilterStringEquals()
		pvp = ParameterValueProvider(ElementId(int(_bip)))
		frule = FilterStringRule(pvp, fnrvStr, _val, False)
		filter = ElementParameterFilter(frule)
		elem = FilteredElementCollector(doc).\
			OfCategory(_bic).\
			WhereElementIsElementType().\
			WherePasses(filter).\
			ToElements()
	else:
		fnrvStr = FilterStringEquals()
		pvp = ParameterValueProvider(ElementId(int(_bip)))
		frule = FilterStringRule(pvp, fnrvStr, _val, False)
		filter = ElementParameterFilter(frule)
		elem = FilteredElementCollector(doc).\
			OfCategory(_bic).\
			WhereElementIsNotElementType().\
			WherePasses(filter).\
			ToElements()
	return elem


def getTypeByCatFamType(_bic, _fam, _type):
	global doc
	fnrvStr = FilterStringEquals()

	pvpType = ParameterValueProvider(ElementId(int(BuiltInParameter.SYMBOL_NAME_PARAM)))
	pvpFam = ParameterValueProvider(ElementId(int(BuiltInParameter.ALL_MODEL_FAMILY_NAME)))

	fruleF = FilterStringRule(pvpFam, fnrvStr, _fam, False)
	filterF = ElementParameterFilter(fruleF)

	fruleT = FilterStringRule(pvpType, fnrvStr, _type, False)
	filterT = ElementParameterFilter(fruleT)

	filter = LogicalAndFilter(filterT, filterF)

	elem = FilteredElementCollector(doc).\
		OfCategory(_bic).\
		WhereElementIsElementType().\
		WherePasses(filter).\
		FirstElement()

	return elem


reload = IN[0]
outlist = list()
elCircuits = FilteredElementCollector(doc).OfCategory(
	BuiltInCategory.OST_ElectricalCircuit).ToElements()

cNames = [GetParVal(x, "RBS_ELEC_CIRCUIT_NAME") for x in elCircuits]
cNumbers = [GetParVal(x, "RBS_ELEC_CIRCUIT_NUMBER") for x in elCircuits]
cPanel = [x.BaseEquipment for x in elCircuits]

check_type = Electrical.ElectricalSystemType.PowerCircuit
sysList = [
	x for x in zip(elCircuits, cPanel, cNames)
	if x[1] and x[0].SystemType == check_type]

sysList.sort(key=lambda x: (x[1].Name, x[2]))

sortedCicruits = [x[0] for x in sysList]
sortedPanels = [x[1] for x in sysList]

# Создание пустого щита для расчётов. Далее щит будет удален
# Тип щита "хард-кодед" для упрощения задачи
testBrdTyp = "KRA_OHT_0800x0400x2000"
testParam = BuiltInParameter.SYMBOL_NAME_PARAM
pvp = ParameterValueProvider(ElementId(int(testParam)))
fnrvStr = FilterStringEquals()
filter = ElementParameterFilter(
	FilterStringRule(pvp, fnrvStr, testBrdTyp, False))

testBoardType = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElectricalEquipment).\
	WhereElementIsElementType().\
	WherePasses(filter).\
	ToElements()[0]

testParam = BuiltInParameter.SYMBOL_NAME_PARAM
pvp = ParameterValueProvider(ElementId(int(testParam)))
fnrvStr = FilterStringEquals()
filter = ElementParameterFilter(FilterStringRule(
	pvp, fnrvStr, "400/230", False))

distrSys = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElecDistributionSys).\
	WhereElementIsElementType().\
	WherePasses(filter).\
	ToElements()[0].Id

# =========Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

testBoardType.Activate()
testBoard = doc.Create.NewFamilyInstance(
	XYZ(0, 0, 0), testBoardType, Structure.StructuralType.NonStructural)

testBoard.get_Parameter(
	BuiltInParameter.RBS_FAMILY_CONTENT_DISTRIBUTION_SYSTEM).Set(distrSys)
doc.Regenerate()

# подсоединяем каждую систему на тест-щит
# connect = lambda x: x[0].SelectPanel(x[1])
# map(connect, zip(sortedCicruits,[testBoard]*len(sortedCicruits)))

for circ in sortedCicruits:
	circ.SelectPanel(testBoard)
	doc.Regenerate()

# присоединяем цепи обратно в отсортированном порядке.
for circ, pan in zip(sortedCicruits, sortedPanels):
	circ.SelectPanel(pan)
	doc.Regenerate()

doc.Delete(testBoard.Id)
doc.Regenerate()

TransactionManager.Instance.TransactionTaskDone()
# =========End transaction


OUT = [GetParVal(x, "RBS_ELEC_CIRCUIT_NAME") for x in sortedCicruits]
