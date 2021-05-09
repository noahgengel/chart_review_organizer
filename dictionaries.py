"""
File contains dictionaries for the following:

- Co-morbidities
- Indications
- Complications
- Associated esophageal procedure
- Associated laryngeal procedure
- Abnormal esophageal endoscopic findings
- Abnormal esophageal biopsy results
"""

# CO-MORBIDITIES

# dictionary used to ensure consistency when replacing each of the
# original co-morbidities with their most appropriate 'umbrella' term
cm_dict_final = {
    "none": "0",
    "hn_cancer": "1",
    "esophageal_stricture": "2",
    "other": "None"  # waiting to be approved
}


co_morbidities = {
    "0": cm_dict_final["none"],
    "1": cm_dict_final["hn_cancer"],
    "2": cm_dict_final["esophageal_stricture"],

    # still waiting for approval on below - revisit

    "3": cm_dict_final["other"],
    "4": cm_dict_final["other"],
    "5": cm_dict_final["other"],
    "6": cm_dict_final["other"],
    "7": cm_dict_final["other"],
    "8": cm_dict_final["other"],
    "9": cm_dict_final["other"],
    "10": cm_dict_final["other"],
    "11": cm_dict_final["other"],
    "12": cm_dict_final["other"],
    "13": cm_dict_final["other"],
    "14": cm_dict_final["other"],
    "15": cm_dict_final["other"],
    "16": cm_dict_final["other"],
    "17": cm_dict_final["other"],
    "18": cm_dict_final["other"],
    "19": cm_dict_final["other"],
    "20": cm_dict_final["other"],
    "21": cm_dict_final["other"],
    "22": cm_dict_final["other"],
    "23": cm_dict_final["other"],
    "24": cm_dict_final["other"],
    "25": cm_dict_final["other"],
    "26": cm_dict_final["other"],
    "27": cm_dict_final["other"],
    "28": cm_dict_final["other"],
    "29": cm_dict_final["other"],
    "30": cm_dict_final["other"],
    "31": cm_dict_final["other"],
    "32": cm_dict_final["other"],
    "33": cm_dict_final["other"],
    "34": cm_dict_final["other"],
    "35": cm_dict_final["other"],
    "36": cm_dict_final["other"],
    "37": cm_dict_final["other"],
    "38": cm_dict_final["other"],
    "39": cm_dict_final["other"],
    "40": cm_dict_final["other"],
    "41": cm_dict_final["other"],
    "42": cm_dict_final["other"],
    "43": cm_dict_final["other"],
    "44": cm_dict_final["other"],
    "45": cm_dict_final["other"],
    "46": cm_dict_final["other"],
    "47": cm_dict_final["other"],
    "48": cm_dict_final["other"],
    "49": cm_dict_final["other"],
    "50": cm_dict_final["other"],
    "51": cm_dict_final["other"],
    "52": cm_dict_final["other"],
    "53": cm_dict_final["other"],
    "54": cm_dict_final["other"],
    "55": cm_dict_final["other"],
    "56": cm_dict_final["other"],
    "57": cm_dict_final["other"],
    "58": cm_dict_final["other"],
    "59": cm_dict_final["other"],
    "60": cm_dict_final["other"],
    "61": cm_dict_final["other"],
    "62": cm_dict_final["other"],
    "63": cm_dict_final["other"],
    "64": cm_dict_final["other"],
    "65": cm_dict_final["other"],
    "66": cm_dict_final["other"],
    "67": cm_dict_final["other"],
    "68": cm_dict_final["other"],
    "69": cm_dict_final["other"],
    "70": cm_dict_final["other"],
    "71": cm_dict_final["other"],
    "72": cm_dict_final["other"],
    "73": cm_dict_final["other"],
    "74": cm_dict_final["other"],
    "75": cm_dict_final["other"],
    "76": cm_dict_final["other"],
    "77": cm_dict_final["other"],
}


# INDICATION FOR TNE

# dictionary used to ensure consistency when replacing each of the
# original TNE indications with their most appropriate 'umbrella' term
tne_indciation_final = {
    "globus": "0",
    "reflux": "1",
    "dysnphagia": "2",
    "hn_cancer_screening": "3",
    "esophageal_stricture": "4",

    "other": "Other"  # waiting to be approved
}


tne_indication = {
    "0": tne_indciation_final["globus"],
    "1": tne_indciation_final["reflux"],
    "2": tne_indciation_final["dysnphagia"],
    "3": tne_indciation_final["hn_cancer_screening"],
    "4": tne_indciation_final["esophageal"],

    # still waiting for approval on below - revisit

    "5": tne_indciation_final["other"],
    "6": tne_indciation_final["other"],
    "7": tne_indciation_final["other"],
    "8": tne_indciation_final["other"],
    "9": tne_indciation_final["other"],
    "10": tne_indciation_final["other"],
    "11": tne_indciation_final["other"],
    "12": tne_indciation_final["other"],
    "13": tne_indciation_final["other"],
    "14": tne_indciation_final["other"],
    "15": tne_indciation_final["other"],
    "16": tne_indciation_final["other"],
    "17": tne_indciation_final["other"],
    "18": tne_indciation_final["other"],
    "19": tne_indciation_final["other"],
    "20": tne_indciation_final["other"],
    "21": tne_indciation_final["other"],
    "22": tne_indciation_final["other"],
    "23": tne_indciation_final["other"],
    "24": tne_indciation_final["other"],
    "25": tne_indciation_final["other"],
    "26": tne_indciation_final["other"],
    "27": tne_indciation_final["other"],
    "28": tne_indciation_final["other"]
}


# TNE COMPLICATIONS

# dictionary used to ensure consistency when replacing each of the
# original complications with their most appropriate 'umbrella' term
complications_final = {
    "none": "0",
    "epistaxis": "1",
    "esophageal_performatino": "2",
    "bleeding": "3",
    "gagging_stricture": "4",
    "vomiting": "5",

    "other": "Other"  # waiting to be approved
}


complications = {
    "0": complications_final["none"],
    "1": complications_final["epistaxis"],
    "2": complications_final["esophageal_performatino"],
    "3": complications_final["bleeding"],
    "4": complications_final["gagging"],
    "5": complications_final["vomiting"],

    # still waiting for approval on below - revisit
    "6": complications_final["other"],
    "7": complications_final["other"],
    "8": complications_final["other"],
    "9": complications_final["other"],
    "10": complications_final["other"],
}


# associated esophageal procedure

# dictionary used to ensure consistency when replacing each of the
# original procedures with their most appropriate 'umbrella' term
esoph_procedures_final = {
    "none": "0",
    "therapeutic_injection": "1",
    "pneumatic_dilation": "2",
    "tep_puncture": "3",
    "fb_removal": "4",
    "esophageal_dilation": "5",
    "biopsy": "6",

    "other": "Other"  # waiting to be approved
}


esoph_procedures = {
    "0": esoph_procedures_final["none"],
    "1": esoph_procedures_final["therapeutic_injection"],
    "2": esoph_procedures_final["pneumatic_dilation"],
    "3": esoph_procedures_final["tep_puncture"],
    "4": esoph_procedures_final["fb_removal"],
    "5": esoph_procedures_final["esophageal_dilation"],
    "6": esoph_procedures_final["biopsy"],

    # still waiting for approval on below - revisit
    "7": esoph_procedures_final["biopsy"],
    "8": esoph_procedures_final["other"],
    "9": esoph_procedures_final["other"],
    "10": esoph_procedures_final["other"],
    "11": esoph_procedures_final["other"],
    "12": esoph_procedures_final["other"]
}


# associated laryngeal procedure

# dictionary used to ensure consistency when replacing each of the
# original procedures with their most appropriate 'umbrella' term
laryng_procedures_final = {
    "none": "0",
    "laryngeal_biopsy": "1",
    "laser_ablation": "2",
    "laryngeal_injection": "3",

    "other": "Other"  # waiting to be approved
}


laryng_procedures = {
    "0": laryng_procedures_final["none"],
    "1": laryng_procedures_final["laryngeal_biopsy"],
    "2": laryng_procedures_final["laser_ablation"],
    "3": laryng_procedures_final["laryngeal_injection"],

    # still waiting for approval on below - revisit
    "4": laryng_procedures_final["other"]
}


# associated biopsy results

# dictionary used to ensure consistency when replacing each of the
# original biopsy results with their most appropriate 'umbrella' term
biopsy_final = {
    "none": "0",
    "candida": "1",
    "invasive_scca": "2",
    "eosinophilic_esophagitis": "3",
    "barretts_esoph": "4",

    "other": "Other"  # waiting to be approved
}


biopsy = {
    "0": biopsy_final["none"],
    "1": biopsy_final["candida"],
    "2": biopsy_final["invasive_scca"],
    "3": biopsy_final["eosinophilic_esophagitis"],
    "4": biopsy_final["barretts_esoph"],

    # still waiting for approval on below - revisit
    "5": biopsy_final["other"]
}
