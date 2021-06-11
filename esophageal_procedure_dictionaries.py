"""
File contains dictionaries for the following:

1. esoph_procedures_final: what number is associated with the final
esophageal procedure

2. esoph_procedures: provides a mapping from the originally-logged
number to the number associated with the updated esophageal procedure
"""


esoph_procedures_final = {
    "none": 0,
    "therapeutic_injection": 1,
    "pneumatic_dilation": 2,
    "tep_puncture": 3,
    "fb_removal": 4,
    "esophageal_dilation": 5,
    "biopsy": 6,
    "prosthesis_replacement": 7,
    "removal_salivary_stent": 8,
    "esophageal_disimpaction": 9,
    "closure_malf_tep_fistula": 10,

    "peg_removal": 11,
    "non_esoph_biopsy": 12,

    "delete": None  # waiting to be approved
}


esoph_procedures = {
    "0": esoph_procedures_final["none"],
    "1": esoph_procedures_final["therapeutic_injection"],
    "2": esoph_procedures_final["pneumatic_dilation"],
    "3": esoph_procedures_final["tep_puncture"],
    "4": esoph_procedures_final["fb_removal"],
    "5": esoph_procedures_final["esophageal_dilation"],
    "6": esoph_procedures_final["biopsy"],
    "7": esoph_procedures_final["prosthesis_replacement"],
    "8": esoph_procedures_final["removal_salivary_stent"],
    "9": esoph_procedures_final["esophageal_disimpaction"],
    "10": esoph_procedures_final["closure_malf_tep_fistula"],

    "11": esoph_procedures_final["therapeutic_injection"],
    "12": esoph_procedures_final["delete"],
    "13": esoph_procedures_final["tep_puncture"],
    "14": esoph_procedures_final["therapeutic_injection"],
    "15": esoph_procedures_final["peg_removal"],
    "16": esoph_procedures_final["non_esoph_biopsy"],
    "17": esoph_procedures_final["delete"]
}
