"""
File is intended to associate numbers for the folliowng:
    - comorbidities
    - complications
    - esophageal biopsy results
    - esophageal findings
    - esophageal procedures
    - laryngeal procedures
    - indications for TNE
to strings to be placed in figure legends

NOTE: Could be improved/streamlined by putting strings in a separate
    python file and using those in this file and in the 'dictionaries'
    file to ensure consistency.
"""

comorbidities_legend = {
    0: "None",
    1: "Head and Neck Cancer Survivor",
    2: "Esophageal Stricture/Stenosis",
    3: "Neurodegenerative Disease",
    4: "History of Total Laryngectomy",
    5: "Tracheoesophageal Puncture (TEP)",
    6: "Chondroradionecrosis",
    7: "Pseudovallecula",
    8: "GERD",
    9: "COPD",
    # no 10 - accidental duplicate
    11: "Tracheostomy Dependent",
    12: "Hiatal Hernia",
    13: "TEP Fistula Malfunction",
    14: "Gastrostomy Tube Dependent",
    15: "Esophageal Stent",
    16: "Cricopharyngeus Muscle Dysfunction",
    17: "History of Esophagectomy",
    18: "Esophageal Dysmotility",
    19: "History of Anterior c-spine Surgery",
    20: "Eosinophilic Esophagitis",
    21: "Schatzki Ring",
    22: "Cervical Osteophyte",
    23: "Viral Esophagitis",
    24: "Reflux Esophagistis",
    25: "Laryngopharyngeal Reflux",
    26: "Acalasia",
    27: "Barrett's Esophagus",
    28: "Gastric Pull-Up",
    29: "Autoimmune Disease",
    30: "Malnourished",
    31: "Traction Diverticulum"
}

tne_indication_legend = {
    1: "Globus",
    2: "Reflux",
    3: "Dysphagia",
    4: "Head and Neck Cancer Screening",
    5: "Esophageal Stricture/Stenosis",
    6: "TEP Malfunction",
    7: "Chronic Throat Pain",
    8: "Stent Removal",
    9: "TEP Malfunction",
    10: "Dysphonia",
    11: "Cricopharyngeus Muscle Dysfunction",
    12: "Foreign Body Evaluation",
    13: "TEP Evaluation",
    14: "Odynophagia",
    15: "Post-Surgical Evaluation",
    16: "Erucation",
    17: "Aerophagia",
    18: "Non-functional Larynx",
    19: "Vocal Fold Granuloma",
    20: "Malnutrition",
    21: "Velopharyngeal Insufficiency",
    22: "Chronic Cough"
}

complications_legend = {
    0: "None",
    1: "Epistaxis",
    2: "Esophageal Perforation",
    3: "Bleeding",
    4: "Gagging",
    5: "Vomiting",
    6: "Challenge Intubating due to Stricture",
    7: "Unable to Pass Guidewire during Dilation",
    8: "Oxygen Desaturation",
    9: "Discomfort",
    10: "Anxiety",
    11: "Mucosal Tear"
}

esophageal_procedure_legend = {
    0: "None",
    1: "Theraputic Injection",
    2: "Pneumatic Dilation",
    3: "TEP Puncture",
    4: "FB Removal",
    5: "Esophageal Dilation",
    6: "Biopsy",
    7: "Prosthesis Replacement",
    8: "Removal of Salivary Bypass Stent",
    9: "Esophageal Disimpaction",
    10: "Closure of Malfunctioning TEP Fistula",
    11: "PEG Removal",
    12: "Biopsy other than Esophagus"
}

esophageal_findings_legend = {
    0: "None",
    1: "Esophageal Stricture/Stenosis",
    2: "CP Muscle Dysfunction",
    3: "TEP Malfunction",
    4: "Esophageal Candidiasis",
    5: "Pharyngoesophageal Stricture",
    6: "Lesion Suspicious for Head and Neck Cancer",
    7: "Neopharyngeal Stenosis",
    8: "Granulation Tissue at TEP",
    9: "Enlarging TEP Fistula",
    10: "Laryngeal Edema",
    11: "Supraglottic Stenosis",
    12: "Reflux Esophagitis",
    13: "Suspicion for Barrett's Esophagus",
    14: "Esophageal Food Impaction",
    15: "Glycogenic Acanthosis",
    16: "Suspicion for Barrett's Esophagus",
    17: "Hiatal Hernia",
    18: "Vocal Fold Immobility",
    19: "Gastric Polyps",
    20: "Prebylarynges",
    21: "Irregular Z-line",
    22: "Tortuous Esophagus",
    23: "Shortened Esophagus",
    24: "Vocal Cord Granuloma",
    25: "Zenker's Diverticulum"
}

esophageal_biopsy_legend = {
    0: "None",
    1: "Candida",
    2: "Invasive SCCA",
    3: "Eosinophilic Esophagitis",
    4: "Barrett's Esophagus without Dysphasia",
    5: "Chronic Inflammation Consistent with Reflux",
    6: "Squamous Mucosa with Atypia",
    # skip 7 - accidental duplicate
    8: "Parakeratosis",
    9: "Attached Gastric Cardiac Mucosa"
}

laryngeal_procedures_legend = {
    0: "None",
    1: "Laryngeal Biopsy",
    2: "Laser Ablation",
    3: "Laryngeal Injection",
    4: "Removal of Larry Tube (Tracheobronchoscopy)"
}
