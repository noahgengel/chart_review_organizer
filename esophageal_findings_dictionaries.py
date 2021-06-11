"""
File contains dictionaries for the following:

1. esophageal_findings_final: what number is associated with the final
esophageal finding

2. esophageal_findings: provides a mapping from the originally-logged
number to the number associated with the updated esophageal finding
"""


esophageal_findings_final = {
    "none": 0,
    "esophageal_stricture": 1,
    "cp_muscle_dysfcn": 2,
    "tep_malfunction": 3,
    "esophageal_candidiasis": 4,
    "phargyngoesophageal_stricture": 5,
    "lesion_suspicious_for_hn_cancer": 6,
    "neopharyngeal_stenosis": 7,
    "granulation_tissue_tep": 8,
    "enlarging_tep_fistula": 9,
    "laryngeal_edema": 10,

    "supraglottic_stenosis": 11,
    "reflux_esophagitis": 12,
    "suspicion_barretts_esophagus": 13,
    "esophageal_food_impaction": 14,
    "glycogenic_acanthosis": 15,
    # 16 had a duplicate
    "hiatal_hernia": 17,
    "vocal_fold_immobility": 18,
    "gastric_polyps": 19,
    "prebylarynges": 20,

    "irregular_z_line": 21,
    "tortuous_esoph": 22,
    "shortened_esoph": 23,
    "vocal_cord_granuloma": 24,
    "zenkers_diverticulum": 25,

    "delete": None
}

esophageal_findings = {
    "0": esophageal_findings_final["none"],
    "1": esophageal_findings_final["esophageal_stricture"],
    "2": esophageal_findings_final["cp_muscle_dysfcn"],
    "3": esophageal_findings_final["tep_malfunction"],
    "4": esophageal_findings_final["cp_muscle_dysfcn"],
    "5": esophageal_findings_final["cp_muscle_dysfcn"],
    "6": esophageal_findings_final["esophageal_candidiasis"],
    "7": esophageal_findings_final["phargyngoesophageal_stricture"],
    "8": esophageal_findings_final["esophageal_stricture"],
    "9": esophageal_findings_final["esophageal_stricture"],
    "10": esophageal_findings_final["delete"],

    "11": esophageal_findings_final["esophageal_stricture"],
    "12": esophageal_findings_final["esophageal_stricture"],
    "13": esophageal_findings_final["esophageal_stricture"],
    "14": esophageal_findings_final["lesion_suspicious_for_hn_cancer"],
    "15": esophageal_findings_final["neopharyngeal_stenosis"],
    "16": esophageal_findings_final["granulation_tissue_tep"],
    "17": esophageal_findings_final["enlarging_tep_fistula"],
    "18": esophageal_findings_final["laryngeal_edema"],
    "19": esophageal_findings_final["laryngeal_edema"],
    "20": esophageal_findings_final["supraglottic_stenosis"],

    "21": esophageal_findings_final["reflux_esophagitis"],
    "22": esophageal_findings_final["delete"],
    "23": esophageal_findings_final["tep_malfunction"],
    "24": esophageal_findings_final["delete"],
    "25": esophageal_findings_final["tep_malfunction"],
    "26": esophageal_findings_final["delete"],
    "27": esophageal_findings_final["delete"],
    "28": esophageal_findings_final["esophageal_stricture"],
    "29": esophageal_findings_final["lesion_suspicious_for_hn_cancer"],
    "30": esophageal_findings_final["reflux_esophagitis"],

    "31": esophageal_findings_final["suspicion_barretts_esophagus"],
    "32": esophageal_findings_final["delete"],
    "33": esophageal_findings_final["esophageal_food_impaction"],
    "34": esophageal_findings_final["glycogenic_acanthosis"],
    "35": esophageal_findings_final["suspicion_barretts_esophagus"],
    "36": esophageal_findings_final["hiatal_hernia"],
    "37": esophageal_findings_final["lesion_suspicious_for_hn_cancer"],
    "38": esophageal_findings_final["vocal_fold_immobility"],
    "39": esophageal_findings_final["suspicion_barretts_esophagus"],
    "40": esophageal_findings_final["delete"],

    "41": esophageal_findings_final["gastric_polyps"],
    "42": esophageal_findings_final["prebylarynges"],
    "43": esophageal_findings_final["irregular_z_line"],
    "44": esophageal_findings_final["reflux_esophagitis"],
    "45": esophageal_findings_final["delete"],
    "46": esophageal_findings_final["prebylarynges"],
    "47": esophageal_findings_final["esophageal_stricture"],
    "48": esophageal_findings_final["suspicion_barretts_esophagus"],
    "49": esophageal_findings_final["phargyngoesophageal_stricture"],
    "50": esophageal_findings_final["gastric_polyps"],

    "51": esophageal_findings_final["reflux_esophagitis"],
    "52": esophageal_findings_final["tortuous_esoph"],
    "53": esophageal_findings_final["delete"],
    "54": esophageal_findings_final["delete"],
    "55": esophageal_findings_final["delete"],
    "56": esophageal_findings_final["esophageal_candidiasis"],
    "57": esophageal_findings_final["vocal_fold_immobility"],
    "58": esophageal_findings_final["shortened_esoph"],
    "59": esophageal_findings_final["delete"],
    "60": esophageal_findings_final["esophageal_stricture"],

    "61": esophageal_findings_final["esophageal_stricture"],
    "62": esophageal_findings_final["vocal_cord_granuloma"],
    "63": esophageal_findings_final["laryngeal_edema"],
    "64": esophageal_findings_final["vocal_cord_granuloma"],
    "65": esophageal_findings_final["laryngeal_edema"],
    "66": esophageal_findings_final["granulation_tissue_tep"],
    "67": esophageal_findings_final["delete"],
    "68": esophageal_findings_final["esophageal_candidiasis"],
    "69": esophageal_findings_final["neopharyngeal_stenosis"],
    "70": esophageal_findings_final["reflux_esophagitis"],

    "71": esophageal_findings_final["zenkers_diverticulum"],
    "72": esophageal_findings_final["reflux_esophagitis"],
    "73": esophageal_findings_final["suspicion_barretts_esophagus"],
    "74": esophageal_findings_final["esophageal_candidiasis"]
}
