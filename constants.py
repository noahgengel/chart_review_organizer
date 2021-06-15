# File is used to store constants that can be used elsewhere


from comorbidities_dictionaries import co_morbidities
from complications_dictionaries import complications
from esophageal_biopsy_dictionaries import biopsy
from esophageal_findings_dictionaries import esophageal_findings
from esophageal_procedure_dictionaries import esoph_procedures
from laryngeal_procedures_dictionaries import laryng_procedures
from tne_indication_dictionaries import tne_indication

file_name = "slp_data.xlsx"

sheet_name = "Sheet1"


columns_dictionary = {
    "name_col": 0,
    "mrn_col": 1,
    "dob_col": 2,
    "age_col": 3,
    "sex_col": 4,
    "race_col": 5,
    "procedure_date_col": 6,
    "comorbidities_col": 7,
    "barium_col": 8,
    "tne_indication_col": 9,
    "surgeon_col": 10,
    "slp_col": 11,
    "procedure_completion_col": 12,
    "complications_col": 13,
    "esophageal_procedure_col": 14,
    "laryngeal_procedure_col": 15,
    "abnormal_esoph_findings_col": 16,
    "abnormal_esophageal_biopsy_results": 17,
    "cpt_col": 18,
    "icd_col": 19
}


associated_dictionary = {
    columns_dictionary["comorbidities_col"]: co_morbidities,
    columns_dictionary["complications_col"]: complications,
    columns_dictionary["abnormal_esophageal_biopsy_results"]: biopsy,
    columns_dictionary["abnormal_esoph_findings_col"]: esophageal_findings,
    columns_dictionary["esophageal_procedure_col"]: esoph_procedures,
    columns_dictionary["laryngeal_procedure_col"]: laryng_procedures,
    columns_dictionary["tne_indication_col"]: tne_indication
}

value_error_msg = """Unanticipated input at row {row_idx}, column {column_idx}.
            Value {values} is of type {type}"""

output_file = "tne_data.xlsx"
