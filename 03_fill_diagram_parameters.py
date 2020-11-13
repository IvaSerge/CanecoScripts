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


# =========standart parameters
reload = IN[0]
calculate_all = IN[1]
update_board_name = IN[2]
outlist = list()
DISTR_SYS_NAME = "400/230"

# Get all electrical circuits
# Circuit type need to be electrilcal only
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

# # Filtering systems that need to be calculated
# if calculate_all:
# 	# Filtering out not connected circuits
# 	rvtSystems = [sys for sys in rvtAllSystems if sys.BaseEquipment]
# else:
# 	# changes to the board will also affect all other boards
# 	# that are higher in the electrical diagramm
# 	# That's why all that board circuits also need to be changed
# 	rvtSystems = list()
# 	while update_board_name:
# 		# Get board instance
# 		update_board = getByCatAndStrParam(
# 			BuiltInCategory.OST_ElectricalEquipment,
# 			BuiltInParameter.RBS_ELEC_PANEL_NAME,
# 			update_board_name,
# 			False)
# 		try:
# 			board_systems = getSystems(update_board[0])
# 		except:
# 			raise ValueError("Board \"%s\" not found" % update_board_name)
# 		board_main_system = board_systems[0]
# 		low_systems = board_systems[1]
# 		if low_systems:
# 			map(lambda x: rvtSystems.append(x), low_systems)

# 		# loop exit conditions
# 		update_board_name = None
# 		if board_main_system:
# 			update_board_name = GetParVal(
# 				board_main_system,
# 				"RBS_ELEC_CIRCUIT_PANEL_PARAM")


# =========Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

TransactionManager.Instance.TransactionTaskDone()
# =========End transaction

OUT = outlist
