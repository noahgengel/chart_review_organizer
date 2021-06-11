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
