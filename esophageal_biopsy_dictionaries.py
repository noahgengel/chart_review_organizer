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
