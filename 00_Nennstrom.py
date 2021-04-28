import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

import System
from System import Array
from System.Collections.Generic import *

import math
from math import sqrt

doc = DocumentManager.Instance.CurrentDBDocument


def GetParVal(elem, name):
	value = None
	# custom parameter
	param = elem.LookupParameter(name)
	# check is it a BuiltIn parameter if not found
	if not(param):
		param = elem.get_Parameter(GetBuiltInParam(name))

	# get paremeter Value if found
	try:
		storeType = param.StorageType
		# value = storeType
		if storeType == StorageType.String:
			value = param.AsString()
		elif storeType == StorageType.Integer:
			value = param.AsDouble()
		elif storeType == StorageType.Double:
			value = param.AsDouble()
		elif storeType == StorageType.ElementId:
			value = param.AsValueString()
	except:
		pass
	return value


def GetBuiltInParam(paramName):
	builtInParams = System.Enum.GetValues(BuiltInParameter)
	param = []
	for i in builtInParams:
		if i.ToString() == paramName:
			param.append(i)
			return i


def SetupParVal(elem, name, pValue):
	global doc
	# custom parameter
	param = elem.LookupParameter(name)
	# check is it a BuiltIn parameter if not found
	if not(param):
		try:
			param = elem.get_Parameter(GetBuiltInParam(name)).Set(pValue)
		except:
			pass
	if param:
		try:
			param.Set(pValue)
		except:
			pass
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


def clearParam(_elem):
	name = "CBT:CIR_Elektrischen Schlag"
	parVal = GetParVal(_elem, name)
	if parVal and "Schutz Datenbank" in parVal:
		SetupParVal(_elem, name, "")
	return parVal


def SSclearCable(_sys):
	"""replace cable type to "N/A" for cable
	that connects board with quasi-board"""

	global doc, cabNA
	brdCategory = -2001040
	# Is this system contains subsystems "Sammelschiene"?
	elems = [elem for elem in _sys.Elements]
	elem = elems[0]
	# is it electrical board?
	if int(elem.Category.Id.ToString()) == int(brdCategory):
		brdCode = elem.LookupParameter("MC Panel Code").AsString()
		# is this board marked as subboard?
		if brdCode and brdCode != "":
			SetupParVal(_sys, "E_CableSize", "")
			SetupParVal(_sys, "RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", cabNA.Id)
			return _sys
		else:
			return None
	return None


def SetApparentValues(_elSys):
	global doc
	global TESTBOARD
	outlist = list()
	calcSystem = _elSys
	phaseN = calcSystem.PolesNumber
	# Main board of electrical system
	mainBoard = calcSystem.BaseEquipment
	brdCategory = mainBoard.Category.Id
	# reconnect system from Main to Test board
	calcSystem.SelectPanel(TESTBOARD)
	doc.Regenerate()

	# Electrical calculations using formulas
	cos_Phi = calcSystem.PowerFactor
	rvtS = TESTBOARD.get_Parameter(
		BuiltInParameter.
		RBS_ELEC_PANEL_TOTALESTLOAD_PARAM).AsDouble()
	rvtS = UnitUtils.ConvertFromInternalUnits(
		rvtS, DisplayUnitType.DUT_VOLT_AMPERES)

	rvtS_total = TESTBOARD.get_Parameter(
		BuiltInParameter.
		RBS_ELEC_PANEL_TOTALLOAD_PARAM).AsDouble()

	P_total = rvtS_total * cos_Phi
	P_apparent = rvtS * cos_Phi

	if phaseN == 1:
		I_apparent = P_apparent / (cos_Phi * 230)
	else:
		I_apparent = P_apparent / (cos_Phi * 400 * sqrt(3))

	# Is it any Board in circuit?
	elems = [elem for elem in calcSystem.Elements]
	elem = elems[0]

	# Wirte parameters in Board
	if elem.Category.Id == brdCategory:
		SetupParVal(elem, "MC CosPhi", cos_Phi)
		SetupParVal(elem, "MC Active Power", P_total)
		SetupParVal(elem, "E_EstimatedPower", P_apparent)

	# Write parameters in Circuit
	calcSystem.LookupParameter("E_EstimatedPower").Set(P_apparent)
	calcSystem.LookupParameter("E_EstimatedCurrent").Set(I_apparent)

	# reconnect circuit back
	calcSystem.SelectPanel(mainBoard)
	doc.Regenerate()
	outlist.append([calcSystem, rvtS, cos_Phi, P_apparent, I_apparent])
	return outlist


def getSystems(_brd):
	"""Get all systems of electrical board.

		args:
		_brd - electrical board FamilyInstance

		return list(1, 2) where:
		1 - main electrical circuit
		2 - list of connectet low circuits
	"""
	allsys = _brd.MEPModel.ElectricalSystems
	lowsys = _brd.MEPModel.AssignedElectricalSystems
	if lowsys:
		lowsysId = [i.Id for i in lowsys]
		mainboardsysLst = [i for i in allsys if i.Id not in lowsysId]
		if len(mainboardsysLst) == 0:
			mainboardsys = None
		else:
			mainboardsys = mainboardsysLst[0]
		lowsys = [i for i in allsys if i.Id in lowsysId]
		lowsys.sort(key=lambda x: float(GetParVal(x, "RBS_ELEC_CIRCUIT_NUMBER")))
		return mainboardsys, lowsys
	else:
		return [i for i in allsys][0], None


# =========standart parameters
reload = IN[0]
calculate_all = IN[1]
update_board_name = IN[2]
outlist = list()
DISTR_SYS_NAME = "400/230"

# Get all electrical circuits
# Circuit type need to be electrilca only
# electrical circuit type ID == 6
testParam = BuiltInParameter.RBS_ELEC_CIRCUIT_TYPE
pvp = ParameterValueProvider(ElementId(int(testParam)))
sysRule = FilterIntegerRule(pvp, FilterNumericEquals(), 6)

testParam = BuiltInParameter.RBS_ELEC_CIRCUIT_TYPE
pvp = ParameterValueProvider(ElementId(int(testParam)))
sysRule = FilterIntegerRule(pvp, FilterNumericEquals(), 6)
filter = ElementParameterFilter(sysRule)

rvtAllSystems = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElectricalCircuit).\
	WhereElementIsNotElementType().WherePasses(filter).\
	ToElements()

# Find board type to create TESTBOARD instance later
testParam = BuiltInParameter.RBS_FAMILY_CONTENT_DISTRIBUTION_SYSTEM
pvp = ParameterValueProvider(ElementId(int(testParam)))
fnrvStr = FilterStringEquals()
filter = ElementParameterFilter(
	FilterStringRule(pvp, fnrvStr, DISTR_SYS_NAME, False))

firstBoardInst = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElectricalEquipment).\
	WhereElementIsNotElementType().\
	WherePasses(filter).\
	FirstElement()

try:
	testBoardType = doc.GetElement(firstBoardInst.GetTypeId())
except:
	raise ValueError(
		"Board not found \n check system name \"%s\""
		% DISTR_SYS_NAME)

testParam = BuiltInParameter.SYMBOL_NAME_PARAM
pvp = ParameterValueProvider(ElementId(int(testParam)))
fnrvStr = FilterStringEquals()
filter = ElementParameterFilter(
	FilterStringRule(pvp, fnrvStr, DISTR_SYS_NAME, False))

distrSys = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElecDistributionSys).\
	WhereElementIsElementType().\
	WherePasses(filter).\
	ToElements()[0].Id

testParam = BuiltInParameter.SYMBOL_NAME_PARAM
pvp = ParameterValueProvider(ElementId(int(testParam)))
filter = ElementParameterFilter(
	FilterStringRule(pvp, fnrvStr, "N/A", False))
fnrvStr = FilterStringEquals()
cabNA = FilteredElementCollector(doc).\
	OfClass(Autodesk.Revit.DB.Electrical.WireType).\
	WherePasses(filter).\
	ToElements()[0]

# Filtering systems that need to be calculated
if calculate_all:
	# Filtering out not connected circuits
	rvtSystems = [sys for sys in rvtAllSystems if sys.BaseEquipment]
else:
	# changes to the board will also affect all other boards
	# that are higher in the electrical diagramm
	# That's why all that board circuits also need to be changed
	rvtSystems = list()
	while update_board_name:
		# Get board instance
		update_board = getByCatAndStrParam(
			BuiltInCategory.OST_ElectricalEquipment,
			BuiltInParameter.RBS_ELEC_PANEL_NAME,
			update_board_name,
			False)
		try:
			board_systems = getSystems(update_board[0])
		except:
			raise ValueError("Board \"%s\" not found" % update_board_name)
		board_main_system = board_systems[0]
		low_systems = board_systems[1]
		if low_systems:
			map(lambda x: rvtSystems.append(x), low_systems)

		# loop exit conditions
		update_board_name = None
		if board_main_system:
			update_board_name = GetParVal(
				board_main_system,
				"RBS_ELEC_CIRCUIT_PANEL_PARAM")


# =========Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

TESTBOARD = doc.Create.NewFamilyInstance(
	XYZ(0, 0, 0), testBoardType, Structure.StructuralType.NonStructural)
TESTBOARD.get_Parameter(
	BuiltInParameter.RBS_FAMILY_CONTENT_DISTRIBUTION_SYSTEM).Set(distrSys)

# map(clearParam, rvtAllSystems)
clearSSList = [SSclearCable(x) for x in rvtSystems]
setParList = [SetApparentValues(x) for x in rvtSystems]
doc.Delete(TESTBOARD.Id)

# =========End transaction
TransactionManager.Instance.TransactionTaskDone()

OUT = clearSSList
# OUT = rvtSystems
