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
    "none": 0,
    "hn_cancer": 1,
    "esophageal_stricture": 2,
    "neurodegenerative_disease": 3,
    "hx_total_laryngectomy": 4,
    "tep": 5,
    "chondroradionecrosis": 6,
    "pseudovallecula": 7,
    "gerd": 8,
    "copd": 9,
    # note - there is no 10 because i accidentally double-counted

    "trach_dependent": 11,
    "hiatal_hernia": 12,
    "tep_fistula_malfunction": 13,
    "g_tube_dependent": 14,
    "esophageal_stent": 15,
    "cp_muscle_dysfcn": 16,
    "hx_esophagectomy": 17,
    "esophageal_dysmotility": 18,
    "hx_anterior_spine_surgery": 19,
    "eosinophilic_esophagitis": 20,

    "schatzki_ring": 21,
    "cervical_osteophyte": 22,
    "viral_esophagitis": 23,
    "reflux_esophagitis": 24,
    "laryngopharyngeal_reflux": 25,
    "acalasia": 26,
    "barretts_esophagus": 27,
    "gastric_pull_up": 28,
    "autoimmune_disease": 29,
    "malnourished": 30,

    "traction_diverticulum": 31,
    "delete": None  # waiting to be approved
}


co_morbidities = {
    "0": cm_dict_final["none"],
    "1": cm_dict_final["hn_cancer"],
    "2": cm_dict_final["esophageal_stricture"],
    "3": cm_dict_final["neurodegenerative_disease"],
    "4": cm_dict_final["hx_total_laryngectomy"],
    "5": cm_dict_final["delete"],
    "6": cm_dict_final["tep"],
    "7": cm_dict_final["delete"],
    "8": cm_dict_final["chondroradionecrosis"],
    "9": cm_dict_final["pseudovallecula"],
    "10": cm_dict_final["delete"],

    "11": cm_dict_final["gerd"],
    "12": cm_dict_final["delete"],
    "13": cm_dict_final["copd"],
    "14": cm_dict_final["delete"],
    "15": cm_dict_final["delete"],
    "16": cm_dict_final["hx_total_laryngectomy"],
    "17": cm_dict_final["tep"],
    "18": cm_dict_final["delete"],
    "19": cm_dict_final["hx_total_laryngectomy"],
    "20": cm_dict_final["delete"],

    "21": cm_dict_final["cp_muscle_dysfcn"],
    "22": cm_dict_final["tep"],
    "23": cm_dict_final["trach_dependent"],
    "24": cm_dict_final["delete"],
    "25": cm_dict_final["delete"],
    "26": cm_dict_final["delete"],
    "27": cm_dict_final["delete"],
    "28": cm_dict_final["delete"],
    "29": cm_dict_final["delete"],
    "30": cm_dict_final["hiatal_hernia"],

    "31": cm_dict_final["delete"],
    "32": cm_dict_final["tep_fistula_malfunction"],
    "33": cm_dict_final["g_tube_dependent"],
    "34": cm_dict_final["esophageal_stent"],
    "35": cm_dict_final["cp_muscle_dysfcn"],
    "36": cm_dict_final["esophageal_stent"],
    "37": cm_dict_final["delete"],
    "38": cm_dict_final["tep"],
    "39": cm_dict_final["delete"],
    "40": cm_dict_final["tep_fistula_malfunction"],

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


