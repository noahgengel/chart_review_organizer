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
    "mrn_col": 1,
    "dob_col": 2,
    "age_col": 3,
    "procedure_date_col": 4,
    "comorbidities_col": 5,
    "barium_col": 6,
    "tne_indication_col": 7,
    "surgeon_col": 8,
    "slp_col": 9,
    "procedure_completion_col": 10,
    "complications_col": 11,
    "esophageal_procedure_col": 12,
    "laryngeal_procedure_col": 13,
    "abnormal_esoph_findings_col": 14,
    "abnormal_esophageal_biopsy_results": 15,
    "cpt_col": 16,
    "icd_col": 17
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
