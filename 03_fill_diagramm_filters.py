# available logic operators
# string_contains
# string_not_contains
# is_equal is_not_equal

# Rules for Büro SS1
rules_Büro_SS1 = list()
rules_Büro_SS1.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS1.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS1"])
param_Büro_SS1 = list()
param_Büro_SS1.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_1modul"])
param_Büro_SS1.append(["E_Sch_FamilyType", "Schutzschalter"])
param_Büro_SS1.append(["E_Sch_Nennstrom", "20A"])
param_Büro_SS1.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS1.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS1.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS1.append(["E_CableSize", "N/A"])
filter_Büro_SS1 = [rules_Büro_SS1, param_Büro_SS1]

# Rules for Büro SS2
rules_Büro_SS2 = list()
rules_Büro_SS2.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS2.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS2"])
param_Büro_SS2 = list()
param_Büro_SS2.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_1modul"])
param_Büro_SS2.append(["E_Sch_FamilyType", "Schutzschalter"])
param_Büro_SS2.append(["E_Sch_Nennstrom", "32A"])
param_Büro_SS2.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS2.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS2.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS2.append(["E_CableSize", "N/A"])
filter_Büro_SS2 = [rules_Büro_SS2, param_Büro_SS2]


# Rules for Büro SS3
rules_Büro_SS3 = list()
rules_Büro_SS3.append(["RBS_ELEC_CIRCUIT_PANEL_PARAM", "string_contains", "Büro"])
rules_Büro_SS3.append(["RBS_ELEC_CIRCUIT_NAME", "string_contains", "SS3"])
param_Büro_SS3 = list()
param_Büro_SS3.append(["E_Sch_Family", "E_SCH_Einspeisung-3P_1modul"])
param_Büro_SS3.append(["E_Sch_FamilyType", "Schutzschalter"])
param_Büro_SS3.append(["E_Sch_Nennstrom", "25A"])
param_Büro_SS3.append(["E_Sch_Schutztyp", "LS-Schalter C"])
param_Büro_SS3.append(["E_Sch_Schutztyp_kurz", "QF"])
param_Büro_SS3.append(["E_Sch_Elektrischen Schlag", ""])
param_Büro_SS3.append(["E_CableSize", "N/A"])
filter_Büro_SS3 = [rules_Büro_SS3, param_Büro_SS3]

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
param_SS3_3.append(["E_Sch_Schutztyp", "FILS-Schalter B"])
param_SS3_3.append(["E_Sch_Schutztyp_kurz", "QD"])
param_SS3_3.append(["E_Sch_Elektrischen Schlag", "FI 30mA"])
param_SS3_3.append(["E_CableSize", "5x4"])
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
filter_SS4_1 = [rules_SS4_1, param_SS4_1]

# Rules for SS4 / "NOT-Austaster"

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
filter_SS4_3 = [rules_SS4_3, param_SS4_3]


# Rules for SS4 / 3poles / Reserve

# Rules for SS4 / 1poles / Reserve


# list of filters
all_filters = list()
all_filters.append(filter_Büro_SS1)
all_filters.append(filter_Büro_SS2)
all_filters.append(filter_Büro_SS3)
all_filters.append(filter_SS1)
all_filters.append(filter_SS2)
all_filters.append(filter_SS3_3)
all_filters.append(filter_SS3_1)
all_filters.append(filter_SS4_1)
all_filters.append(filter_SS4_3)


OUT = all_filters
