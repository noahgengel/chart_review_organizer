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
    "esophageal_perforation": 2,
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
    "2": complications_final["esophageal_perforation"],
    "3": complications_final["bleeding"],
    "4": complications_final["gagging"],
    "5": complications_final["vomiting"],
    "6": complications_final["challenge_intubating_stricture"],
    "7": complications_final["unable_to_pass_guidewire"],
    "8": complications_final["esophageal_perforation"],
    "9": complications_final["oxygen_desat"],
    "10": complications_final["oxygen_desat"],
    "11": complications_final["discomfort"],
    "12": complications_final["anxiety"],
    "13": complications_final["challenge_intubating_stricture"],
    "14": complications_final["mucosal_tear"]
}
