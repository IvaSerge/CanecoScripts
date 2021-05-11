# available logic operators
# string_contains
# string_not_contains
# is_equal
# is_not_equal

# Rules for NSHV
rules_NSHV = list()
rules_NSHV.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "NSHV"])
param_NSHV = list()
param_NSHV.append(["E_Sch_Nennstrom", "50A"])
param_NSHV.append(["E_Sch_Schutztyp", "Schalter"])
param_NSHV.append(["E_Sch_Schutztyp_kurz", "QF"])
param_NSHV.append(["E_Sch_Elektrischen Schlag", ""])
param_NSHV.append(["E_CableSize", "4x35/16"])
param_NSHV.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYCWY"])
filter_NSHV = [rules_NSHV, param_NSHV]

# Rules for Büro SS1
rules_Büro_SS1 = list()
rules_Büro_SS1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS1.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS1"])
param_Büro_SS1 = list()
param_Büro_SS1.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_2lvl"])
param_Büro_SS1.append(["E_Sch_FamilyType", "Schalter+WH_lvl2"])
param_Büro_SS1.append(["E_Sch_Nennstrom", "20A"])
param_Büro_SS1.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS1.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS1.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS1.append(["E_CableSize", ""])
param_Büro_SS1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_Büro_SS1 = [rules_Büro_SS1, param_Büro_SS1]

# Rules for Büro SS2
rules_Büro_SS2 = list()
rules_Büro_SS2.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS2.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS2"])
param_Büro_SS2 = list()
param_Büro_SS2.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_2lvl"])
param_Büro_SS2.append(["E_Sch_FamilyType", "Schalter+WH_lvl2"])
param_Büro_SS2.append(["E_Sch_Nennstrom", "32A"])
param_Büro_SS2.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS2.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS2.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS2.append(["E_CableSize", ""])
param_Büro_SS2.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_Büro_SS2 = [rules_Büro_SS2, param_Büro_SS2]

# Rules for Büro SS3
rules_Büro_SS3 = list()
rules_Büro_SS3.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS3.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS3"])
param_Büro_SS3 = list()
param_Büro_SS3.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_2lvl"])
param_Büro_SS3.append(["E_Sch_FamilyType", "Schalter+WH_lvl2"])
param_Büro_SS3.append(["E_Sch_Nennstrom", "32A"])
param_Büro_SS3.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS3.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS3.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS3.append(["E_CableSize", ""])
param_Büro_SS3.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_Büro_SS3 = [rules_Büro_SS3, param_Büro_SS3]

# Rules for Büro SS4
rules_Büro_SS4 = list()
rules_Büro_SS4.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS4.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS4"])
param_Büro_SS4 = list()
param_Büro_SS4.append(["E_Sch_Family", "E_SCH_EinspeisungKontaktor_2lvl"])
param_Büro_SS4.append(["E_Sch_FamilyType", "Kontaktor"])
param_Büro_SS4.append(["E_Sch_Nennstrom", "25A"])
param_Büro_SS4.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS4.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS4.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS4.append(["E_CableSize", ""])
param_Büro_SS4.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "N/A"])
filter_Büro_SS4 = [rules_Büro_SS4, param_Büro_SS4]

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

# Rules for SS3 / 3poles
rules_SS3_3 = list()
rules_SS3_3.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_SS3_3.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS3"])
rules_SS3_3.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "Wasserheizer"])
param_SS3_3 = list()
param_SS3_3.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS3_3.append(["E_Sch_FamilyType", "3p.QF-FI"])
param_SS3_3.append(["E_Sch_Nennstrom", "20A"])
param_SS3_3.append(["E_Sch_Schutztyp", "LS-Schalter B"])
param_SS3_3.append(["E_Sch_Schutztyp_kurz", "QF"])
param_SS3_3.append(["E_Sch_Elektrischen Schlag", ""])
param_SS3_3.append(["E_CableSize", "5x4"])
param_SS3_3.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS3_3 = [rules_SS3_3, param_SS3_3]

# Rules for SS3 / 3poles / Reserve

# Rules for SS3 / 1poles
rules_SS3_1 = list()
rules_SS3_1.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_SS3_1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS3"])
param_SS3_1 = list()
param_SS3_1.append(["E_Sch_Family", "E_SCH_SICHERUNGSSCHALTER"])
param_SS3_1.append(["E_Sch_FamilyType", "1p.Schutzschalter"])
param_SS3_1.append(["E_Sch_Nennstrom", "16A"])
param_SS3_1.append(["E_Sch_Schutztyp", "LS-Schalter B"])
param_SS3_1.append(["E_Sch_Schutztyp_kurz", "QF"])
param_SS3_1.append(["E_Sch_Elektrischen Schlag", ""])
param_SS3_1.append(["E_CableSize", "3x2.5"])
param_SS3_1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS3_1 = [rules_SS3_1, param_SS3_1]

# Rules for SS4 / 1poles
rules_SS4_1 = list()
rules_SS4_1.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 1])
rules_SS4_1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS4"])
rules_SS4_1.append(["RBS_ELEC_CIRCUIT_NAME", "is_not_equal", "NOT-Austaster"])
param_SS4_1 = list()
param_SS4_1.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS4_1.append(["E_Sch_FamilyType", "1p.QF-FI"])
param_SS4_1.append(["E_Sch_Nennstrom", "16A"])
param_SS4_1.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS4_1.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS4_1.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS4_1.append(["E_CableSize", "3x2.5"])
param_SS4_1.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS4_1 = [rules_SS4_1, param_SS4_1]

# Rules for SS4 / "NOT-Austaster"
rules_SS4_NOT = list()
rules_SS4_NOT.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS4"])
rules_SS4_NOT.append(["RBS_ELEC_CIRCUIT_NAME", "is_equal", "NOT-Austaster"])
param_SS4_NOT = list()
param_SS4_NOT.append(["E_Sch_Family", "E_SCH_NOT-Austaster"])
param_SS4_NOT.append(["E_Sch_FamilyType", "NOT-Austaster"])
param_SS4_NOT.append(["E_Sch_Nennstrom", ""])
param_SS4_NOT.append(["E_Sch_Schutztyp", ""])
param_SS4_NOT.append(["E_Sch_Schutztyp_kurz", ""])
param_SS4_NOT.append(["E_Sch_Elektrischen Schlag", ""])
param_SS4_NOT.append(["E_CableSize", "3x2.5"])
param_SS4_NOT.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS4_NOT = [rules_SS4_NOT, param_SS4_NOT]

# Rules for SS4 / 3poles
rules_SS4_3 = list()
rules_SS4_3.append(["RBS_ELEC_NUMBER_OF_POLES", "is_equal", 3])
rules_SS4_3.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "SS4"])
rules_SS4_3.append(["RBS_ELEC_CIRCUIT_NAME", "is_not_equal", "NOT-Austaster"])
param_SS4_3 = list()
param_SS4_3.append(["E_Sch_Family", "E_SCH_QF-FI-SCHALTER"])
param_SS4_3.append(["E_Sch_FamilyType", "3p.QF-FI"])
param_SS4_3.append(["E_Sch_Nennstrom", "16A"])
param_SS4_3.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS4_3.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS4_3.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS4_3.append(["E_CableSize", "5x2.5"])
param_SS4_3.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYM"])
filter_SS4_3 = [rules_SS4_3, param_SS4_3]

# Rules for SS4 / 3poles / Reserve

# Rules for SS4 / 1poles / Reserve

# list of filters
sys_filters = list()
sys_filters.append(filter_NSHV)
sys_filters.append(filter_Büro_SS1)
sys_filters.append(filter_Büro_SS2)
sys_filters.append(filter_Büro_SS3)
sys_filters.append(filter_Büro_SS4)
sys_filters.append(filter_SS1)
sys_filters.append(filter_SS2)
sys_filters.append(filter_SS3_3)
sys_filters.append(filter_SS3_1)
sys_filters.append(filter_SS4_1)
sys_filters.append(filter_SS4_3)
sys_filters.append(filter_SS4_NOT)

# =======================
# Rules for boards
# =======================

# Rules for NSHV
rules_NSHV = list()
rules_NSHV.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "NSHV"])
param_NSHV = list()
param_NSHV.append(["E_Sch_Nennstrom", "50A"])
param_NSHV.append(["E_Sch_Schutztyp", "Schalter"])
param_NSHV.append(["E_Sch_Schutztyp_kurz", "QF"])
param_NSHV.append(["E_Sch_Elektrischen Schlag", ""])
param_NSHV.append(["E_CableSize", "4x35/16"])
param_NSHV.append(["RBS_ELEC_CIRCUIT_WIRE_TYPE_PARAM", "NYCWY"])
filter_NSHV = [rules_NSHV, param_NSHV]


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

# list of filters
brd_filters = list()
brd_filters.append(filter_brd_Büro)

OUT = sys_filters, brd_filters
