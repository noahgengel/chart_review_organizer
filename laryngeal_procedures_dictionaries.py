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
