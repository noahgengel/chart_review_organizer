"""
File contains dictionaries for the following:

1. biopsy_final: what number is associated with the final
biopsy result

2. biopsy: provides a mapping from the originally-logged
number to the number associated with the updated biopsy
"""

biopsy_final = {
    "none": 0,
    "candida": 1,
    "invasive_scca": 2,
    "eosinophilic_esophagitis": 3,
    "barretts_esoph": 4,
    "chronic_inflammation_consistent_with_reflux": 5,
    "squamous_mucosa_atypia": 6,
    "invasive_scca": 7,
    "parakeratosis": 8,

    "delete": None  # waiting to be approved
}


biopsy = {
    "0": biopsy_final["none"],
    "1": biopsy_final["candida"],
    "2": biopsy_final["invasive_scca"],
    "3": biopsy_final["eosinophilic_esophagitis"],
    "4": biopsy_final["barretts_esoph"],
    "5": biopsy_final["chronic_inflammation_consistent_with_reflux"],
    "6": biopsy_final["chronic_inflammation_consistent_with_reflux"],
    "7": biopsy_final["squamous_mucosa_atypia"],
    "8": biopsy_final["chronic_inflammation_consistent_with_reflux"],
    "9": biopsy_final["chronic_inflammation_consistent_with_reflux"],
    "10": biopsy_final["invasive_scca"],
    "11": biopsy_final["parakeratosis"],
    "12": biopsy_final["delete"]
}
