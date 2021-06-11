"""
File contains dictionaries for the following:

1. complications_final: what number is associated with the final
complication

2. complications: provides a mapping from the originally-logged
number to the number associated with the updated complication
"""


complications_final = {
    "none": 0,
    "epistaxis": 1,
    "esophageal_performation": 2,
    "bleeding": 3,
    "gagging": 4,
    "vomiting": 5,
    "challenge_intubating_stricture": 6,
    "unable_to_pass_guidewire": 7,
    "oxygen_desat": 8,
    "discomfort": 9,
    "anxiety": 10,

    "mucosal_tear": 11,
    "delete": None
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
