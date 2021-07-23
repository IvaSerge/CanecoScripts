# available logic operators
# string_contains
# string_not_contains
# is_equal
# is_not_equal

# Rules for NSHV
rules_NSHV = list()
rules_NSHV.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "NSHV"])
param_NSHV = list()
param_NSHV.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_1modul+WH"])
param_NSHV.append(["E_Sch_FamilyType", "Ausschalter"])
param_NSHV.append(["E_Sch_Nennstrom", "63A"])
param_NSHV.append(["E_Sch_Schutztyp", "Schalter"])
param_NSHV.append(["E_Sch_Schutztyp_kurz", "QS"])
param_NSHV.append(["E_Sch_Elektrischen Schlag", ""])
param_NSHV.append(["E_CableSize", "4x35/16"])
param_NSHV.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYCWY"])
filter_NSHV = [rules_NSHV, param_NSHV]

# Rules for Büro SS
rules_Büro_SS = list()
rules_Büro_SS.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS"])
param_Büro_SS = list()
param_Büro_SS.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_2lvl"])
param_Büro_SS.append(["E_Sch_FamilyType", "Schalter+WH_lvl2"])
param_Büro_SS.append(["E_Sch_Nennstrom", "40A"])
param_Büro_SS.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS.append(["E_Sch_Schutztyp_kurz", "QS"])
param_Büro_SS.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS.append(["E_CableSize", ""])
param_Büro_SS.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_Büro_SS = [rules_Büro_SS, param_Büro_SS]

# Rules for SS1
rules_SS1 = list()
rules_SS1.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_SS1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS1"])
param_SS1 = list()
param_SS1.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS1.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_SS1.append(["E_Sch_Nennstrom", "10A"])
param_SS1.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS1.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS1.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS1.append(["E_CableSize", "3x1.5"])
param_SS1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS1 = [rules_SS1, param_SS1]

# Rules for SS2
rules_SS2 = list()
rules_SS2.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_SS2.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS2"])
param_SS2 = list()
param_SS2.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS2.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_SS2.append(["E_Sch_Nennstrom", "16A"])
param_SS2.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS2.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS2.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS2.append(["E_CableSize", "3x2.5"])
param_SS2.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS2 = [rules_SS2, param_SS2]

# Rules for SS4
rules_SS4 = list()
rules_SS4.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_SS4.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS4"])
param_SS4 = list()
param_SS4.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS4.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_SS4.append(["E_Sch_Nennstrom", "16A"])
param_SS4.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS4.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS4.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS4.append(["E_CableSize", "3x2.5"])
param_SS4.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS4 = [rules_SS4, param_SS4]

# Rules for SS6 / 3poles
rules_SS6 = list()
rules_SS6.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_SS6.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS6"])
rules_SS6.append(["RBS_ELEC_CIRCUIT_NAME", "is_not_equal", "NOT-Austaster"])
param_SS6 = list()
param_SS6.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS6.append(["E_Sch_FamilyType", "3p.QF-FI"])
param_SS6.append(["E_Sch_Nennstrom", "16A"])
param_SS6.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS6.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS6.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS6.append(["E_CableSize", "5x2.5"])
param_SS6.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS6 = [rules_SS6, param_SS6]


# Rules for WeWork 1pole
rules_WeWork_1 = list()
rules_WeWork_1.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_WeWork_1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
param_WeWork_1 = list()
param_WeWork_1.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_WeWork_1.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_WeWork_1.append(["E_Sch_Nennstrom", "16A"])
param_WeWork_1.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_WeWork_1.append(["E_Sch_Schutztyp_kurz", "QD"])
param_WeWork_1.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_WeWork_1.append(["E_CableSize", "3x2.5"])
param_WeWork_1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_WeWork_1 = [rules_WeWork_1, param_WeWork_1]

# Rules for WeWork MSR
rules_WeWork_2 = list()
rules_WeWork_2.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_WeWork_2.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
rules_WeWork_2.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "MSR"])
param_WeWork_2 = list()
param_WeWork_2.append(["E_Sch_Family", "E_SCH_SICHERUNGSSCHALTER"])
param_WeWork_2.append(["E_Sch_FamilyType", "3p.Schutzschalter"])
param_WeWork_2.append(["E_Sch_Nennstrom", "25A"])
param_WeWork_2.append(["E_Sch_Schutztyp", "LS-Schalter B"])
param_WeWork_2.append(["E_Sch_Schutztyp_kurz", "QF"])
param_WeWork_2.append(["E_Sch_Elektrischen Schlag", ""])
param_WeWork_2.append(["E_CableSize", "5x4"])
param_WeWork_2.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_WeWork_2 = [rules_WeWork_2, param_WeWork_2]

# Rules for WeWork Reserve 1 poles
rules_WeWork_3 = list()
rules_WeWork_3.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_WeWork_3.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
rules_WeWork_3.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "Reserve"])
param_WeWork_3 = list()
param_WeWork_3.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_WeWork_3.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_WeWork_3.append(["E_Sch_Nennstrom", "16A"])
param_WeWork_3.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_WeWork_3.append(["E_Sch_Schutztyp_kurz", "QD"])
param_WeWork_3.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_WeWork_3.append(["E_CableSize", ""])
param_WeWork_3.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_WeWork_3 = [rules_WeWork_3, param_WeWork_3]

# Rules for WeWork Reserve 3 poles
rules_WeWork_4 = list()
rules_WeWork_4.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_WeWork_4.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
rules_WeWork_4.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "Reserve"])
param_WeWork_4 = list()
param_WeWork_4.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_WeWork_4.append(["E_Sch_FamilyType", "3p.QF-FI"])
param_WeWork_4.append(["E_Sch_Nennstrom", "16A"])
param_WeWork_4.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_WeWork_4.append(["E_Sch_Schutztyp_kurz", "QD"])
param_WeWork_4.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_WeWork_4.append(["E_CableSize", ""])
param_WeWork_4.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_WeWork_4 = [rules_WeWork_4, param_WeWork_4]

# Rules for WeWork Überspannungsableiter 3 poles
rules_WeWork_U = list()
rules_WeWork_U.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_WeWork_U.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
rules_WeWork_U.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "Überspannungsableiter"])
param_WeWork_U = list()
param_WeWork_U.append(["E_Sch_Family", "E_SCH_ÜBERSPANNUNGSABLEITER_T2"])
param_WeWork_U.append(["E_Sch_FamilyType", "3p.Überspannungsableiter"])
param_WeWork_U.append(["E_Sch_Nennstrom", "40A"])
param_WeWork_U.append(["E_Sch_Schutztyp", "LS-Schalter B"])
param_WeWork_U.append(["E_Sch_Schutztyp_kurz", "QF"])
param_WeWork_U.append(["E_Sch_Elektrischen Schlag", ""])
param_WeWork_U.append(["E_CableSize", ""])
param_WeWork_U.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_WeWork_U = [rules_WeWork_U, param_WeWork_U]

# Rules for WeWork SS5 Einspeisung
rules_WeWork_SS5 = list()
rules_WeWork_SS5.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "WeWork"])
rules_WeWork_SS5.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS5"])
param_WeWork_SS5 = list()
param_WeWork_SS5.append(["E_Sch_Family", "E_SCH_EinspeisungKontaktor_2lvl"])
param_WeWork_SS5.append(["E_Sch_FamilyType", "Kontaktor"])
param_WeWork_SS5.append(["E_Sch_Nennstrom", "25A"])
param_WeWork_SS5.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_WeWork_SS5.append(["E_Sch_Schutztyp_kurz", "QF"])
param_WeWork_SS5.append(["E_Sch_Elektrischen Schlag", ""])
param_WeWork_SS5.append(["E_CableSize", ""])
param_WeWork_SS5.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_WeWork_SS5 = [rules_WeWork_SS5, param_WeWork_SS5]

# Rules for SS5 / "NOT-Austaster"
rules_SS5_NOT = list()
rules_SS5_NOT.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS5"])
rules_SS5_NOT.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "NOT-Austaster"])
param_SS5_NOT = list()
param_SS5_NOT.append(["E_Sch_Family", "E_SCH_NOT-Austaster"])
param_SS5_NOT.append(["E_Sch_FamilyType", "NOT-Austaster"])
param_SS5_NOT.append(["E_Sch_Nennstrom", ""])
param_SS5_NOT.append(["E_Sch_Schutztyp", ""])
param_SS5_NOT.append(["E_Sch_Schutztyp_kurz", ""])
param_SS5_NOT.append(["E_Sch_Elektrischen Schlag", ""])
param_SS5_NOT.append(["E_CableSize", "3x2.5"])
param_SS5_NOT.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS5_NOT = [rules_SS5_NOT, param_SS5_NOT]

# Rules for WeWork SS5 / 3 pole
rules_SS5_1 = list()
rules_SS5_1.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_SS5_1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS5"])
param_SS5_1 = list()
param_SS5_1.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS5_1.append(["E_Sch_FamilyType", "3p.QF-FI"])
param_SS5_1.append(["E_Sch_Nennstrom", "16A"])
param_SS5_1.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS5_1.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS5_1.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS5_1.append(["E_CableSize", ""])
param_SS5_1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_SS5_1 = [rules_SS5_1, param_SS5_1]

# list of filters
sys_filters = list()
sys_filters.append(filter_NSHV)
sys_filters.append(filter_Büro_SS)
sys_filters.append(filter_SS1)
sys_filters.append(filter_SS2)
sys_filters.append(filter_SS4)
sys_filters.append(filter_SS6)
sys_filters.append(filter_WeWork_1)
sys_filters.append(filter_WeWork_2)
sys_filters.append(filter_WeWork_3)
sys_filters.append(filter_WeWork_4)
sys_filters.append(filter_WeWork_U)
sys_filters.append(filter_WeWork_SS5)
sys_filters.append(filter_SS5_NOT)
sys_filters.append(filter_SS5_1)

# =======================
# Rules for boards
# =======================

# Rules for Büro
rules_brd_Büro = list()
rules_brd_Büro.append(["RBS_ELEC_PANEL_NAME", "string_contains", "Büro"])
param_brd_Büro = list()
param_brd_Büro.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_1modul"])
param_brd_Büro.append(["E_Sch_FamilyType", "Ausschalter"])
param_brd_Büro.append(["E_Sch_Nennstrom", "50A"])
param_brd_Büro.append(["E_Sch_Schutztyp", "Ausschalter"])
param_brd_Büro.append(["E_Sch_Schutztyp_kurz", "QS"])
param_brd_Büro.append(["E_CableSize", "4x35/16"])

filter_brd_Büro = [rules_brd_Büro, param_brd_Büro]


# Rules for WeWork
rules_brd_WeWork = list()
rules_brd_WeWork.append(["RBS_ELEC_PANEL_NAME", "string_contains", "WeWork"])
param_brd_WeWork = list()
param_brd_WeWork.append(["E_Sch_Family", "E_SCH_Einspeisung-3P+WH_1modul"])
param_brd_WeWork.append(["E_Sch_FamilyType", "Ausschalter"])
param_brd_WeWork.append(["E_Sch_Nennstrom", "63A"])
param_brd_WeWork.append(["E_Sch_Schutztyp", "Ausschalter"])
param_brd_WeWork.append(["E_Sch_Schutztyp_kurz", "QS"])
param_brd_WeWork.append(["E_CableSize", "4x35/16"])

filter_brd_WeWork = [rules_brd_WeWork, param_brd_WeWork]

# list of filters
brd_filters = list()
brd_filters.append(filter_brd_Büro)
brd_filters.append(filter_brd_WeWork)

OUT = sys_filters, brd_filters
