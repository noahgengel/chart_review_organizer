"""
File contains dictionaries for the following:

1. tne_indication_final: what number is associated with the final
indication for the TNE

2. tne_indication: provides a mapping from the originally-logged
number to the number associated with the updated indication for the
TNE
"""

tne_indication_final = {
    "globus": 1,
    "reflux": 2,
    "dysphagia": 3,
    "hn_cancer_screening": 4,
    "esophageal_stricture": 5,
    "tep_malfunction": 6,
    "chronic_throat_pain": 7,
    "stent_removal": 8,
    # note: there is no '9' because I had a duplicate
    "dysphonia": 10,

    "cp_muscle_dysfunction": 11,
    "foreign_body_evaluation": 12,
    "tep_evaluation": 13,
    "odynophagia": 14,
    "post_surgical_eval": 15,
    "erucation": 16,
    "aerophagia": 17,
    "non_functional_larynx": 18,
    "vocal_fold_granuloma": 19,
    "malnutrition": 20,

    "velopharyngeal_insuff": 21,
    "chronic_cough": 22,

    "delete": None
}


tne_indication = {
    "0": tne_indication_final["globus"],
    "1": tne_indication_final["reflux"],
    "2": tne_indication_final["dysphagia"],
    "3": tne_indication_final["hn_cancer_screening"],
    "4": tne_indication_final["esophageal_stricture"],
    "5": tne_indication_final["tep_malfunction"],
    "6": tne_indication_final["esophageal_stricture"],
    "7": tne_indication_final["chronic_throat_pain"],
    "8": tne_indication_final["hn_cancer_screening"],
    "9": tne_indication_final["esophageal_stricture"],
    "10": tne_indication_final["stent_removal"],

    "11": tne_indication_final["esophageal_stricture"],
    "12": tne_indication_final["esophageal_stricture"],
    "13": tne_indication_final["dysphagia"],
    "14": tne_indication_final["tep_malfunction"],
    "15": tne_indication_final["tep_malfunction"],
    "16": tne_indication_final["dysphagia"],
    "17": tne_indication_final["tep_malfunction"],
    "18": tne_indication_final["dysphonia"],
    "19": tne_indication_final["cp_muscle_dysfunction"],
    "20": tne_indication_final["globus"],

    "21": tne_indication_final["dysphagia"],
    "22": tne_indication_final["chronic_throat_pain"],
    "23": tne_indication_final["dysphagia"],
    "24": tne_indication_final["foreign_body_evaluation"],
    "25": tne_indication_final["tep_evaluation"],
    "26": tne_indication_final["delete"],
    "27": tne_indication_final["delete"],
    "28": tne_indication_final["delete"],
    "29": tne_indication_final["dysphagia"],
    "30": tne_indication_final["odynophagia"],

    "31": tne_indication_final["tep_evaluation"],
    "32": tne_indication_final["delete"],
    "33": tne_indication_final["tep_malfunction"],
    "34": tne_indication_final["post_surgical_eval"],
    "35": tne_indication_final["reflux"],
    "36": tne_indication_final["erucation"],
    "37": tne_indication_final["aerophagia"],
    "38": tne_indication_final["delete"],
    "39": tne_indication_final["dysphonia"],
    "40": tne_indication_final["tep_malfunction"],

    "41": tne_indication_final["tep_malfunction"],
    "42": tne_indication_final["non_functional_larynx"],
    "43": tne_indication_final["delete"],
    "44": tne_indication_final["dysphagia"],
    "45": tne_indication_final["delete"],
    "46": tne_indication_final["globus"],
    "47": tne_indication_final["delete"],
    "48": tne_indication_final["vocal_fold_granuloma"],
    "49": tne_indication_final["esophageal_stricture"],
    "50": tne_indication_final["delete"],

    "51": tne_indication_final["malnutrition"],
    "52": tne_indication_final["tep_evaluation"],
    "53": tne_indication_final["tep_evaluation"],
    "54": tne_indication_final["delete"],
    "55": tne_indication_final["delete"],
    "56": tne_indication_final["velopharyngeal_insuff"],
    "57": tne_indication_final["hn_cancer_screening"],
    "58": tne_indication_final["tep_malfunction"],
    "59": tne_indication_final["chronic_throat_pain"],
    "60": tne_indication_final["delete"],

    "61": tne_indication_final["delete"],
    "62": tne_indication_final["chronic_cough"],
    "63": tne_indication_final["globus"],
    "64": tne_indication_final["delete"],
    "65": tne_indication_final["delete"],
    "66": tne_indication_final["foreign_body_evaluation"],
    "67": tne_indication_final["esophageal_stricture"]
}

