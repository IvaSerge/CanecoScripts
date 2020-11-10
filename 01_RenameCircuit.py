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
		lambda x:
		ProcessList(_func, x)
		if type(x) == list else _func(x), _list)


def Unwrap(_item):
	if isinstance(_item, list):
		return ProcessList(Unwrap, _item)
	else:
		return UnwrapElement(_item)


def GetParVal(elem, name):
	# For user parameters
	try:
		param = elem.LookupParameter(name)
		storeType = param.StorageType
		if storeType == StorageType.String:
			value = elem.LookupParameter(name).AsString()
		elif storeType == StorageType.Integer:
			value = elem.LookupParameter(name).AsDouble()
		elif storeType == StorageType.Double:
			value = elem.LookupParameter(name).AsDouble()
	# For BuiltIn parameters
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
elCircuits = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ElectricalCircuit).ToElements()

cNames = [GetParVal(x, "RBS_ELEC_CIRCUIT_NAME") for x in elCircuits]
cNumbers = [GetParVal(x, "RBS_ELEC_CIRCUIT_NUMBER") for x in elCircuits]

formatedNames = list()
regexp = re.compile(r"\d{2}_(.*)")
for num, nam in zip(cNumbers, cNames):
	# Is the system allready have a number?
	check = regexp.match(nam)
	if check:
		try:
			fnumber = '{:02}'.format(int(num))
			newName = fnumber + "_" + check.group(1)
			formatedNames.append(newName)
		except:
			formatedNames.append(check.group(1))

	else:
		try:
			fnumber = '{:02}'.format(int(num))
			newName = fnumber + "_" + nam
			formatedNames.append(newName)
		except:
			formatedNames.append(nam)

# =========Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

paramToSet = zip(elCircuits, formatedNames)
for elem, pVal in zip(elCircuits, formatedNames):
	elem.get_Parameter(
		BuiltInParameter.RBS_ELEC_CIRCUIT_NAME)\
		.Set(pVal)

TransactionManager.Instance.TransactionTaskDone()
# =========End transaction


OUT = formatedNames
