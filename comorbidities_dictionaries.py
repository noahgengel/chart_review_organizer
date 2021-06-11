"""
File contains dictionaries for the following:

1. cm_dict_final: what number is associated with the final
co-moribidity

2. co_morbidities: provides a mapping from the originally-logged
number to the number associated with the updated co-morbidity
"""


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

    "41": cm_dict_final["tep_fistula_malfunction"],
    "42": cm_dict_final["hx_esophagectomy"],
    "43": cm_dict_final["delete"],
    "44": cm_dict_final["cp_muscle_dysfcn"],
    "45": cm_dict_final["esophageal_dysmotility"],
    "46": cm_dict_final["hx_anterior_spine_surgery"],
    "47": cm_dict_final["neurodegenerative_disease"],
    "48": cm_dict_final["cp_muscle_dysfcn"],
    "49": cm_dict_final["esophageal_dysmotility"],
    "50": cm_dict_final["esophageal_dysmotility"],

    "51": cm_dict_final["hiatal_hernia"],
    "52": cm_dict_final["delete"],
    "53": cm_dict_final["eosinophilic_esophagitis"],
    "54": cm_dict_final["schatzki_ring"],
    "55": cm_dict_final["hiatal_hernia"],
    "56": cm_dict_final["esophageal_stricture"],
    "57": cm_dict_final["delete"],
    "58": cm_dict_final["cervical_osteophyte"],
    "59": cm_dict_final["cp_muscle_dysfcn"],
    "60": cm_dict_final["delete"],

    "61": cm_dict_final["cp_muscle_dysfcn"],
    "62": cm_dict_final["delete"],
    "63": cm_dict_final["viral_esophagitis"],
    "64": cm_dict_final["delete"],
    "65": cm_dict_final["delete"],
    "66": cm_dict_final["esophageal_stricture"],
    "67": cm_dict_final["delete"],
    "68": cm_dict_final["reflux_esophagitis"],
    "69": cm_dict_final["delete"],
    "70": cm_dict_final["laryngopharyngeal_reflux"],

    "71": cm_dict_final["acalasia"],
    "72": cm_dict_final["delete"],
    "73": cm_dict_final["delete"],
    "74": cm_dict_final["delete"],
    "75": cm_dict_final["esophageal_stricture"],
    "76": cm_dict_final["neurodegenerative_disease"],
    "77": cm_dict_final["cp_muscle_dysfcn"],
    "78": cm_dict_final["cp_muscle_dysfcn"],
    "79": cm_dict_final["hn_cancer"],
    "80": cm_dict_final["esophageal_stricture"],

    "81": cm_dict_final["delete"],
    "82": cm_dict_final["cp_muscle_dysfcn"],
    "83": cm_dict_final["delete"],
    "84": cm_dict_final["delete"],
    "85": cm_dict_final["delete"],
    "86": cm_dict_final["hx_esophagectomy"],
    "87": cm_dict_final["delete"],
    # accidentally skipped 88
    "89": cm_dict_final["delete"],
    "90": cm_dict_final["delete"],

    "91": cm_dict_final["delete"],
    "92": cm_dict_final["esophageal_stent"],
    "93": cm_dict_final["delete"],
    "94": cm_dict_final["delete"],
    "95": cm_dict_final["delete"],
    "96": cm_dict_final["reflux_esophagitis"],
    "97": cm_dict_final["barretts_esophagus"],
    "98": cm_dict_final["tep"],
    "99": cm_dict_final["delete"],
    "100": cm_dict_final["delete"],

    "101": cm_dict_final["delete"],
    "102": cm_dict_final["delete"],
    "103": cm_dict_final["g_tube_dependent"],
    "104": cm_dict_final["gastric_pull_up"],
    "105": cm_dict_final["delete"],
    "106": cm_dict_final["delete"],
    "107": cm_dict_final["delete"],
    "108": cm_dict_final["delete"],
    "109": cm_dict_final["delete"],
    "110": cm_dict_final["g_tube_dependent"],

    "111": cm_dict_final["delete"],
    "112": cm_dict_final["delete"],
    "113": cm_dict_final["delete"],
    "114": cm_dict_final["autoimmune_disease"],
    "115": cm_dict_final["hx_anterior_spine_surgery"],
    "116": cm_dict_final["g_tube_dependent"],
    "117": cm_dict_final["esophageal_stricture"],
    "118": cm_dict_final["esophageal_stricture"],
    "119": cm_dict_final["malnourished"],
    "120": cm_dict_final["traction_diverticulum"],

    "121": cm_dict_final["delete"],
    "122": cm_dict_final["trach_dependent"],
    "123": cm_dict_final["chondroradionecrosis"],
    "124": cm_dict_final["delete"]
}


