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
	storeType = param.StorageType

	# value = storeType
	if storeType == StorageType.String:
		value = param.AsString()
	elif storeType == StorageType.Integer:
		value = param.AsInteger()
	elif storeType == StorageType.Double:
		value = param.AsDouble()
	elif storeType == StorageType.ElementId:
		value = param.AsValueString()
	return value


def GetBuiltInParam(paramName):
	builtInParams = System.Enum.GetValues(BuiltInParameter)
	param = []
	for i in builtInParams:
		if i.ToString() == paramName:
			param.append(i)
			return i


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


def SetupParVal(elem, name, pValue):
	global doc
	if name == "RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM":
		fnrvStr = FilterStringEquals()
		wire_param = elem.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM)
		pvp = ParameterValueProvider(wire_param.Id)
		frule = FilterStringRule(pvp, fnrvStr, pValue, False)
		filter = ElementParameterFilter(frule)
		wire = FilteredElementCollector(doc).\
			OfClass(Autodesk.Revit.DB.Electrical.WireType).\
			WhereElementIsElementType().\
			WherePasses(filter).\
			FirstElement()
		param = elem.get_Parameter(BuiltInParameter.RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM)
		param.Set(wire.Id)
		return param

	# custom parameter
	param = elem.LookupParameter(name)
	# check is it a BuiltIn parameter if not found

	if not(param):
		try:
			param = elem.get_Parameter(GetBuiltInParam(name))
		except:
			pass
	if param:
		try:
			param.Set(pValue)
		except:
			pass
	return param


def check_element(elem, rules):
	"""
	Check if element correspondes rules

	:attrubutes:
		elem - elemet to be checked
		rules - list of rules to be applyed all rules
			need to be "True" to pass the filter

	:return:
		elem if all filters are True
	"""

	for rule in rules:
		param_name_to_check = rule[0]
		comparison_function = rule[1]
		value_to_check = rule[2]
		param_value = GetParVal(elem, param_name_to_check)

		if comparison_function == "is_equal":
			if not(param_value == value_to_check):
				# filter not passed - quit function
				return None

		elif comparison_function == "is_not_equal":
			if not(param_value != value_to_check):
				# filter not passed - quit function
				return None

		elif comparison_function == "string_contains":
			if not(value_to_check in param_value):
				# filter not passed - quit function
				return None

		elif comparison_function == "string_not_contains":
			if value_to_check in param_value:
				# filter not passed - quit function
				return None

		else:
			raise ValueError(
				"Function \"%s\" not found" % comparison_function)
	return elem


def set_params(elem, param_list):
	"""
	Set element parameters value

	:attrubutes:
		elem - element to be changed
		param_list - list of parameters to set
			param[0] - parameter name
			param[1] - parameter value
	"""
	if not(elem):
		return None

	for param in param_list:
		param_name = param[0]
		param_value = param[1]
		SetupParVal(elem, param_name, param_value)


# =========standart parameters
DISTR_SYS_NAME = "400/230"
reload = IN[0]  # type: ignore
calculate_all = IN[1]  # type: ignore
update_board_name = IN[2]  # type: ignore
filter_list_systems = IN[3]  # type: ignore
filter_list_boards = IN[4]  # type: ignore
outlist = list()

# Get all electrical circuits
# Circuit type need to be electrilcal only
# electrical circuit type ID == 6
test_param = BuiltInParameter.RBS_ELEC_CIRCUIT_TYPE
pvp = ParameterValueProvider(ElementId(int(test_param)))
sysRule = FilterIntegerRule(pvp, FilterNumericEquals(), 6)
filter = ElementParameterFilter(sysRule)

rvtAllSystems = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElectricalCircuit).\
	WhereElementIsNotElementType().WherePasses(filter).\
	ToElements()

# Get all boards
test_param = BuiltInParameter.RBS_FAMILY_CONTENT_DISTRIBUTION_SYSTEM
pvp = ParameterValueProvider(ElementId(int(test_param)))
fnrvStr = FilterStringEquals()
filter = ElementParameterFilter(
	FilterStringRule(pvp, fnrvStr, DISTR_SYS_NAME, False))

boards = FilteredElementCollector(doc).\
	OfCategory(BuiltInCategory.OST_ElectricalEquipment).\
	WhereElementIsNotElementType().\
	WherePasses(filter).\
	ToElements()


# Filtering systems that need to be calculated
if calculate_all:
	# Filtering out not connected circuits
	rvtSystems = [sys for sys in rvtAllSystems if sys.BaseEquipment]
else:
	# get electrical board to be changed
	boards = getByCatAndStrParam(
		BuiltInCategory.OST_ElectricalEquipment,
		BuiltInParameter.RBS_ELEC_PANEL_NAME,
		update_board_name,
		False)
	# get electrical systems of electircal board
	rvtSystems = boards[0].MEPModel.ElectricalSystems

# =========Start transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# set parameters to systems
for filter in filter_list_systems:
	filter_rules = filter[0]
	params_to_set = filter[1]
	# filter elements
	filtered_elements = map(
		lambda x: check_element(x, filter_rules), rvtSystems)
	filtered_elements = [x for x in filtered_elements if x]
	if not filtered_elements:
		continue
	list_to_set = zip(
		filtered_elements, params_to_set * len(filtered_elements))
	map(lambda x: set_params(x, params_to_set), filtered_elements)

# set parameters to boards
for filter in filter_list_boards:
	filter_rules = filter[0]
	params_to_set = filter[1]
	# filter elements
	filtered_elements = list()
	for board in boards:
		try:
			check_board = check_element(board, filter_rules)
			filtered_elements.append(check_board)
		except:
			pass
	filtered_elements = [x for x in filtered_elements if x]
	outlist.append(filtered_elements)
	list_to_set = zip(
		filtered_elements, params_to_set * len(filtered_elements))
	map(lambda x: set_params(x, params_to_set), filtered_elements)

TransactionManager.Instance.TransactionTaskDone()
# =========End transaction

OUT = outlist
# OUT = [x for x in filtered_elements if x]
