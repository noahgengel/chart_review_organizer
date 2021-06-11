

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
