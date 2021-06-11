"""
File contains dictionaries for the following:

1. laryngeal_procedures_final: what number is associated with the final
laryngeal procedures

2. laryngeral_procedures: provides a mapping from the originally-logged
number to the number associated with the updated esophageal finding
"""

laryng_procedures_final = {
    "none": 0,
    "laryngeal_biopsy": 1,
    "laser_ablation": 2,
    "laryngeal_injection": 3,
    "removal_larry_tube": 4,

    "delete": None
}


laryng_procedures = {
    "0": laryng_procedures_final["none"],
    "1": laryng_procedures_final["laryngeal_biopsy"],
    "2": laryng_procedures_final["laser_ablation"],
    "3": laryng_procedures_final["laryngeal_injection"],
    "4": laryng_procedures_final["removal_larry_tube"]
}
