# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Notebook to visualize data for the TNE project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math

from legend_dictionaries import *
from constants import output_file, sheet_name, columns_dictionary
from classes import tne_row

# +
plt.tight_layout()
cwd = os.getcwd()
full_file_name = cwd + "/" + output_file

xl = pd.ExcelFile(full_file_name)
df = xl.parse(sheet_name)
# -

df = df.iloc[:, 1:]
df

tne_objects = []

for idx, row in df.iterrows():
    name = row[columns_dictionary["name_col"]]
    mrn = row[columns_dictionary["mrn_col"]]
    dob = row[columns_dictionary["dob_col"]]
    age = row[columns_dictionary["age_col"]]
    sex = row[columns_dictionary["sex_col"]]
    race = row[columns_dictionary["race_col"]]
    procedure_date = row[columns_dictionary["procedure_date_col"]]
    co_morbidities = row[columns_dictionary["comorbidities_col"]]
    prev_barium_swallow = row[columns_dictionary["barium_col"]]
    tne_indication = row[columns_dictionary["tne_indication_col"]]
    surgeon = row[columns_dictionary["surgeon_col"]]
    slp = row[columns_dictionary["slp_col"]]
    completion = row[columns_dictionary["procedure_completion_col"]]
    complications = row[columns_dictionary["complications_col"]]
    esoph_procedure = row[columns_dictionary["esophageal_procedure_col"]]
    laryngeal_procedure = row[columns_dictionary["laryngeal_procedure_col"]]
    abnormal_esoph_findings = row[columns_dictionary["abnormal_esoph_findings_col"]]
    abnormal_biopsy_findings = row[columns_dictionary["abnormal_esophageal_biopsy_results"]]
    cpt_code = row[columns_dictionary["cpt_col"]]
    icd_code = row[columns_dictionary["icd_col"]]
    
    tne_object = tne_row(
        name = name, mrn = mrn, dob = dob, age = age,
        sex = sex, race = race, procedure_date = procedure_date,
        co_morbidities = co_morbidities,
        prev_barium_swallow = prev_barium_swallow,
        tne_indication = tne_indication,
        surgeon = surgeon, slp = slp, completion = completion,
        complications = complications, esoph_procedure = esoph_procedure,
        laryngeal_procedure = laryngeal_procedure,
        abnormal_esoph_findings = abnormal_esoph_findings,
        abnormal_biopsy_findings = abnormal_biopsy_findings,
        cpt_code = cpt_code, icd_code = icd_code)
    
    tne_objects.append(tne_object)

rotation_val = 90

# +
num_rows = 0

for obj in tne_objects:
    if isinstance(obj.co_morbidities[0], str):
        num_rows += 1

print(f"""
There are {num_rows} rows of relevant TNE data.
""")

# +
encountered_mrns = []

for obj in tne_objects:
    if obj.mrn not in encountered_mrns and isinstance(obj.co_morbidities[0], str):  # ensure and actual person
        encountered_mrns.append(obj.mrn)

num_distinct_mrns = len(encountered_mrns)
        
print(f"""
There are {num_distinct_mrns} distinct MRNs.
""")
# -

# ## Patient Demographics

# +
encountered_mrns = []

num_males, num_females = 0, 0
num_whites, num_hispanic, num_black, num_asian = 0, 0, 0, 0
ages = []

for obj in tne_objects:

    if obj.mrn not in encountered_mrns and isinstance(obj.co_morbidities[0], str):
        encountered_mrns.append(obj.mrn)
        
        # sex encoded as a tuple - take first
        if obj.sex[0] == 1:
            num_males += 1
        elif obj.sex[0] == 2:
            num_females += 1
            
        if obj.race[0] == 1:
            num_whites += 1
        elif obj.race[0] == 2:
            num_hispanic += 1
        elif obj.race[0] == 3:
            num_black += 1
        elif obj.race[0] == 4:
            num_asian += 1
            
        ages.append(obj.age)
            
print(f"""There are {num_males} males in the dataset and {num_females} females in the dataset""")

print(f"""
There are:
    {num_whites} white persons in the dataset
    {num_hispanic} hispanic persons in the dataset
    {num_black} black persons in the dataset
    {num_asian} Asian persons in the dataset
""")

# +
fig = plt.figure()
plt.pie([num_males, num_females], labels = [
    'Males (n={num_males})'.format(num_males=num_males),
    'Females (n={num_females})'.format(num_females=num_females)], autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Sex Distribution in TNE Study')
plt.axis('equal')
plt.legend(title = 'Sex')

plt.show()
fig.savefig('sex_distribution.png')

# +
fig = plt.figure()
plt.pie([num_whites, num_hispanic, num_black, num_asian],
        labels = ['White (n ={num_whites})'.format(num_whites=num_whites),
                  'Hispanic (n={num_hispanic})'.format(num_hispanic=num_hispanic),
                  'Black (n={num_black})'.format(num_black=num_black),
                  'Asian (n={num_asian})'.format(num_asian=num_asian)], autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Race Distribution in TNE Study')
plt.axis('equal')
plt.legend(title = 'Race')

plt.show()
fig.savefig('race_distribution.png')
# +
fig = plt.figure()
array = np.array(ages)

array = np.concatenate(array)


plt.title(
    f"""Box Plot of Distinct Ages (n={num_distinct_mrns})""".format(num_distinct_mrns))
plt.boxplot(array)

plt.ylabel("Age")

plt.show()
fig.savefig('age_box_plot.png')


# +
x = np.percentile(array, 25)
y = np.percentile(array, 50)
z = np.percentile(array, 75)

print(f"""
The patients have the following age characteristics:
   25th percentile: {x}
   Median: {y}
   75th percentile: {z}""")


# -

# ## By patient statistics

#    - NOTE: This takes ALL instances (e.g. comorbidities, indications, findings) that a patient ever has into account (even if it was only reported once but the patient had multiple visits)

def create_dictionary_for_patient_focused_statistics(
    attribute, relevant_dictionary, num_patients):
    """
    Function is used to generate statistics for patient-centered statistics
    
    Parameters
    ----------
    attribute (property): property of the TNE objects to investigate
    
    relevant_dictionary (dict): dict that is used to correlate the number
        to a full-text
        
    num_patients (int): number of patients in the dataset
        
    Returns
    -------
    dictionary (dict): contains key:value pairs with the following structure
        key: text with the descriptions
        value: percentage (with respect to entire patient population) the description occurs
        
    results (list): list with the text descriptions
    
    values (list): list with the values (in the same order as the results)
    """
    mrn_dict = {}

    # creating a dictionary with mrn:relevant conditions (in text)
    for obj in tne_objects:
        mrn = obj.mrn[0]
        
        if mrn not in mrn_dict:
            mrn_dict[mrn] = []

        # get the property to investigate
        for property, value in vars(obj).items():
            if str(property).lower() == attribute:
                findings = value[0]
    
        if isinstance(findings, str):
            findings = findings.splitlines()

            for finding in findings:
                finding = int(finding)
                finding = relevant_dictionary[finding]

                if finding not in mrn_dict[mrn]:
                    mrn_dict[mrn].append(finding)

        elif isinstance(findings, float) and not math.isnan(findings):
            finding = int(findings)
            finding = relevant_dictionary[finding]

            if finding not in mrn_dict[mrn]:
                mrn_dict[mrn].append(finding)
                
        elif math.isnan(findings):
            pass

        else:
            raise ValueError("Unanticipated type found")
    
    dictionary = {}

    # creating dictionary with # of patient with each condition
    for mrn, text_descriptions in mrn_dict.items():
        for text_description in text_descriptions:
        
            if text_description not in dictionary:
                dictionary[text_description] = 1
            else:
                dictionary[text_description] += 1
    
    for text_description, frequency in dictionary.items():
        frequency_percent = round(frequency / num_patients * 100, 1)
        dictionary[text_description] = frequency_percent
    
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))

    text = dictionary.keys()
    values = dictionary.values()
    
    return dictionary, text, values


esoph_procedure_dict, esoph_procedure_text, esoph_procedure_values = create_dictionary_for_patient_focused_statistics(
    attribute = "esoph_procedure",
    relevant_dictionary = esophageal_procedure_legend,
    num_patients = num_distinct_mrns)

esoph_procedure_dict

fig = plt.figure()
plt.bar(esoph_procedure_text, esoph_procedure_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Esophageal Procedure')
plt.ylabel('% of Patients with Procedure')
plt.title(f"""Procedure Prevalence Amongst Patients (n={num_distinct_mrns})""")
plt.show()
plt.gcf().subplots_adjust(bottom=0.8)
fig.savefig('esoph_procedure_by_patient.png', bbox_inches="tight")

cm_dictionary, comorbidities, cm_values = create_dictionary_for_patient_focused_statistics(
    attribute = "co_morbidities",
    relevant_dictionary = comorbidities_legend,
    num_patients = num_distinct_mrns)

fig = plt.figure()
plt.bar(comorbidities, cm_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Comorbidity')
plt.ylabel('% of Patients with Comorbidity')
plt.title(f"""Comorbidity Prevalence Amongst Patients (n={num_distinct_mrns})""")
plt.show()
plt.gcf().subplots_adjust(bottom=0.8)
fig.savefig('comorbidity_prevalence_by_patient.png', bbox_inches="tight")

tne_indication_dict, tne_indications, tne_indication_values = create_dictionary_for_patient_focused_statistics(
    attribute = "tne_indication", 
    relevant_dictionary = tne_indication_legend,
    num_patients = num_distinct_mrns)

tne_indication_dict

# +
tne_indication_values = list(tne_indication_values)
print(tne_indication_values)
tne_indication_array = np.array(tne_indication_values)

x = np.percentile(tne_indication_array, 25)
y = np.percentile(tne_indication_array, 50)
z = np.percentile(tne_indication_array, 75)

print(f"""
The indications for TNE % were as follows:
   25th percentile: {x}
   Median: {y}
   75th percentile: {z}""")
# -

fig = plt.figure()
plt.bar(tne_indications, tne_indication_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Indication for TNE')
plt.ylabel('% of Patients with TNE Indication')
plt.title(f"""Indication for TNE Among Patients (n={num_distinct_mrns})""")
plt.show()
fig.savefig('tne_indication_distribution_by_patient.png', bbox_inches="tight")

abnormal_findings_dict, abnormal_findings, abnormal_values = create_dictionary_for_patient_focused_statistics(
    attribute = "abnormal_esoph_findings", 
    relevant_dictionary = esophageal_findings_legend,
    num_patients = num_distinct_mrns)

len(abnormal_findings_dict)

fig = plt.figure()
plt.bar(abnormal_findings, abnormal_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Abnormal Esophageal Findings By Patient')
plt.ylabel('% of Visits')
plt.title(f"""Abnormal Esophageal Findings Frequency Amongst Patients (n={num_distinct_mrns})""")
plt.show()
fig.savefig('abnormal_esophageal_findings_by_patient.png', bbox_inches="tight")

binary_dict = {0: "No", 1: "Yes"}

prev_barium_dict, prev_barium, prev_barium_values = create_dictionary_for_patient_focused_statistics(
    attribute = "prev_barium_swallow", 
    relevant_dictionary = binary_dict,
    num_patients = num_distinct_mrns)

prev_barium_values

fig = plt.figure()
plt.bar(prev_barium, prev_barium_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=0)
plt.xlabel('Previous Barium Swallow By Patient')
plt.ylabel('% of Patients')
plt.title(f"""Previous Barium Swallow Frequency Amongst Patients (n={num_distinct_mrns})""")
plt.show()
fig.savefig('previous_barium_swallow_by_patient.png', bbox_inches="tight")

biopsy_dict, biopsy_results, biopsy_values = create_dictionary_for_patient_focused_statistics(
    attribute = "abnormal_biopsy_findings", 
    relevant_dictionary = esophageal_biopsy_legend,
    num_patients = num_distinct_mrns)

biopsy_dict


# ## Visit-focused statistics
#     - This is in contrast to statistics that are on a per-patient focus
#     - NOTE: Values may be >100% beacuse more than one value may be reported per visit

def create_dictionary_for_visit_focused_statistics(
    attribute, relevant_dictionary, num_rows):
    """
    Function is used to generate statistics for visit-centered statistics
    
    Parameters
    ----------
    attribute (property): property of the TNE object to investigate
    
    relevant_dictionary (dict): dict that is used to correlate the number
        to a full-text
        
    num_rows (int): number of rows in the dataset
        
    Returns
    -------
    dictionary (dict): contains key:value pairs with the following structure
        key: text with the description
        value: percentage (with respect to entire dataste) the description occurs
        
    results (list): list with the text descriptions
    
    values (list): list with the values (in the same order as the results)
    """
    dictionary = {}

    for obj in tne_objects:
        for property, value in vars(obj).items():
            if str(property).lower() == attribute:
                findings = value[0]
    
        if isinstance(findings, str):
            findings = findings.splitlines()

            for finding in findings:
                finding = int(finding)
                finding = relevant_dictionary[finding]

                if finding not in dictionary:
                    dictionary[finding] = 1
                else:
                    dictionary[finding] += 1

        elif isinstance(findings, float) and not math.isnan(findings):
            finding = int(findings)
            finding = relevant_dictionary[finding]

            if finding not in dictionary:
                dictionary[finding] = 1
            else:
                dictionary[finding] += 1
                
        elif math.isnan(findings):
            pass

        else:
            raise ValueError("Unanticipated type found")
            
    for txt, frequency in dictionary.items():
        frequency_percent = round(frequency / num_rows * 100, 1)
        dictionary[txt] = frequency_percent
        
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    
    results = dictionary.keys()
    values = dictionary.values()
    
    return dictionary, results, values


prev_barium_dict, prev_barium, prev_barium_values = create_dictionary_for_visit_focused_statistics(
    attribute = "prev_barium_swallow", 
    relevant_dictionary = binary_dict,
    num_rows = num_rows)

prev_barium_dict

biopsy_dict, biopsy_results, biopsy_values = create_dictionary_for_visit_focused_statistics(
    attribute = "abnormal_biopsy_findings", 
    relevant_dictionary = esophageal_biopsy_legend,
    num_rows = num_rows)

biopsy_dict

fig = plt.figure()
plt.bar(biopsy_results, biopsy_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Abnormal Biopsy Result')
plt.ylabel('% of Visits with Biopsy Finding')
plt.title(f"""Biopsy Result Frequencies Amongst TNE Visits (n={num_rows})""")
plt.show()
fig.savefig('abnormal_biopsy_values_by_visit.png', bbox_inches="tight")

abnormal_findings_dict, abnormal_findings, abnormal_values = create_dictionary_for_visit_focused_statistics(
    attribute = "abnormal_esoph_findings", 
    relevant_dictionary = esophageal_findings_legend,
    num_rows = num_rows)

abnormal_findings_dict

# fig = plt.figure()
plt.bar(abnormal_findings, abnormal_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Abnormal Esophageal Findings')
plt.ylabel('% of Visits')
plt.title(f"""Abnormal Esophageal Findings Frequency Amongst TNE Visits (n={num_rows})""")
plt.show()
fig.savefig('abnormal_esophageal_findings_by_visit.png', bbox_inches="tight")

tne_indication_dict, tne_indications, tne_indication_values = create_dictionary_for_visit_focused_statistics(
    attribute = "tne_indication", 
    relevant_dictionary = tne_indication_legend,
    num_rows = num_rows)

tne_indication_dict

fig = plt.figure()
plt.bar(tne_indications, tne_indication_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Indication for TNE')
plt.ylabel('% of Visits with TNE Indication')
plt.title(f"""Indication for TNE (n={num_rows})""")
plt.show()
fig.savefig('tne_indication_distribution_by_visit.png', bbox_inches="tight")

cm_dictionary, comorbidities, cm_values = create_dictionary_for_visit_focused_statistics(
    attribute = "co_morbidities",
    relevant_dictionary = comorbidities_legend,
    num_rows = num_rows)

cm_dictionary

esoph_procedures_dict, esoph_procedures, esoph_procedure_values = create_dictionary_for_visit_focused_statistics(
    attribute = "esoph_procedure", 
    relevant_dictionary = esophageal_procedure_legend,
    num_rows = num_rows)

esoph_procedures_dict

fig = plt.figure()
plt.bar(esoph_procedures, esoph_procedure_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Esophageal Procedure')
plt.ylabel('% of Visits with Esophageal Procedure')
plt.title(f"""Percentage of Visits with Esophageal Procedure (n={num_rows})""")
plt.show()
fig.savefig('esophageal_procedures_by_visit.png', bbox_inches="tight")

# ### NOTE: 'Complications' below is later split up into 'true complications' and 'challenges'

complications_dict, complications, complications_values = create_dictionary_for_visit_focused_statistics(
    attribute = "complications", 
    relevant_dictionary = complications_legend,
    num_rows = num_rows)

fig = plt.figure()
plt.bar(complications, complications_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Complication')
plt.ylabel('% of Visits with Reported Complication')
plt.title(f"""TNE Complication Frequency (n={num_rows})""")
plt.show()
# fig.savefig('tne_complication_frequency_by_visit.png', bbox_inches="tight")
# above is later split into two graphs - true complications and challenges

# ## Below are selected graphs IF NOT NONE

biopsy_values

biopsy_values = list(biopsy_values)[:-1]
biopsy_values = np.array(biopsy_values)

biopsy_results = list(biopsy_results)[:-1]
biopsy_results = np.array(biopsy_results)

print(biopsy_values)
fig = plt.figure()
plt.bar(biopsy_results, biopsy_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Abnormal Biopsy Result (if any abnormal result reported)')
plt.ylabel('Percentage of Visits')
plt.title(f"""Abnormal Biopsy Result Frequency Amongst TNE Visits (n={num_rows})""")
plt.show()
fig.savefig('abnormal_biopsy_values_excluding_none_by_visit.png', bbox_inches="tight")

print(complications)

true_complications_list = ["Oxygen Desaturation", "Bleeding", "Esophageal Perforation"]

true_complications_dict, challenges_dict = {}, {}

complications_dict

for key, value in complications_dict.items():
    if key in true_complications_list:
        true_complications_dict[key] = value
    else:
        challenges_dict[key] = value

true_complications_dict

true_complications = true_complications_dict.keys()
true_complications_values = true_complications_dict.values()

challenges = challenges_dict.keys()
challenges_values = challenges_dict.values()

fig = plt.figure()
plt.bar(true_complications, true_complications_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Complication')
plt.ylabel('% of Visits with Reported Complication')
plt.title(f"""TNE Complication Frequency, Excluding None (n={num_rows})""")
plt.show()
fig.savefig('tne_complication_frequencyby_visit.png', bbox_inches="tight")

challenges = list(challenges)[:-1]
challenges = np.array(challenges)

challenges_values

challenges_values = list(challenges_values)[:-1]
challenges_values = np.array(challenges_values)

fig = plt.figure()
plt.bar(challenges, challenges_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=rotation_val)
plt.xlabel('Challenge')
plt.ylabel('% of Visits with Reported Challenges')
plt.title(f"""TNE Challenge Frequency, Excluding None (n={num_rows})""")
plt.show()
fig.savefig('tne_challenge_frequency_by_visit.png', bbox_inches="tight")

# ### Wanting to see biopsy results - how many biopsies were performed?

# +
objs_with_biopsy = []
biopsy = "Biopsy"
row_num = 0

for obj in tne_objects:

    for property, value in vars(obj).items():
        if str(property).lower() == 'esoph_procedure':
            procedures = value[0]
    
            if isinstance(procedures, str):
                procedures = procedures.splitlines()

                for procedure in procedures:
                    procedure = int(procedure)
                    procedure = esophageal_procedure_legend[procedure]
                    
                if procedure == biopsy:
                    objs_with_biopsy.append(obj)

            elif isinstance(procedures, float) and not math.isnan(procedures):
                procedure = int(procedures)
                procedure = esophageal_procedure_legend[procedure]

                if procedure == biopsy:
                    objs_with_biopsy.append(obj)

            row_num += 1
# -

len(objs_with_biopsy)

# +
number_with_none = 0

for obj_with_biopsy in objs_with_biopsy:
    findings = obj_with_biopsy.abnormal_biopsy_findings[0]
    print(findings)
    
    if isinstance(findings, str):
        findings = findings.splitlines()

        for finding in findings:
            finding = int(finding)
            if finding == 0:
                number_with_none += 1

    elif isinstance(findings, float) and not math.isnan(findings):
        findings = int(findings)

        if finding == 0:
            number_with_none += 1

        
print(f"""
There are {number_with_none} instances where a
biopsy was performed but no abnormal finding was reported.""")

# +
n_wo_abnormal_finding = 0

mrns_encountered = []
mrn_and_associated_findings_total = {}

for obj in tne_objects:
    mrn = obj.mrn[0]
    
    if mrn not in mrn_and_associated_findings_total:
        mrn_and_associated_findings_total[mrn] = []

    abnormal_findings = obj.abnormal_esoph_findings[0]
    
    if isinstance(abnormal_findings, str):
        abnormal_findings = abnormal_findings.splitlines()

        for abnormal_finding in abnormal_findings:
            if abnormal_finding not in mrn_and_associated_findings_total[mrn]:
                mrn_and_associated_findings_total[mrn].append(abnormal_finding)
            

    elif isinstance(abnormal_findings, float) and not math.isnan(abnormal_findings):
        finding = int(abnormal_findings)
        if finding not in mrn_and_associated_findings_total[mrn]:
            mrn_and_associated_findings_total[mrn].append(finding)

# +
for mrn, associated_findings in mrn_and_associated_findings_total.items():
    if len(associated_findings) == 1 and associated_findings[0] == '0':
        n_wo_abnormal_finding += 1
        
print(f"""
There are {n_wo_abnormal_finding} patients who have no abnormal
esophageal findings in any of their visits
""")

# +
n_wo_procedures = 0

mrns_encountered = []
mrn_and_associated_procedures = {}

for obj in tne_objects:
    mrn = obj.mrn[0]

    if mrn not in mrn_and_associated_procedures:
        mrn_and_associated_procedures[mrn] = []

    procedures = obj.esoph_procedure[0]
    
    if isinstance(procedures, str):
        procedures = procedures.splitlines()

        for procedure in procedures:
            if procedure not in mrn_and_associated_procedures[mrn]:
                mrn_and_associated_procedures[mrn].append(procedure)
            

    elif isinstance(procedures, float) and not math.isnan(procedures):
        procedure = int(procedures)
        
        if procedure not in mrn_and_associated_procedures[mrn]:
            mrn_and_associated_procedures[mrn].append(procedure)

# +
for mrn, associated_procedures in mrn_and_associated_procedures.items():
    if len(associated_procedures) == 1 and associated_procedures[0] == '0':
        n_wo_procedures += 1
        
print(f"""
There are {n_wo_abnormal_finding} patients who have no procedures in any of their visits.
""")

# +
n_wo_complications = 0

mrns_encountered = []
mrn_and_complications = {}

for obj in tne_objects:
    mrn = obj.mrn[0]

    if mrn not in mrn_and_complications:
        mrn_and_complications[mrn] = []

    complications = obj.complications[0]
    
    if isinstance(complications, str):
        complications = complications.splitlines()

        for complication in complications:
            mrn_and_complications[mrn].append(complication)
            

    elif isinstance(complications, float) and not math.isnan(complications):
        complication = int(complications)
        
        if complication not in mrn_and_complications[mrn]:
            mrn_and_complications[mrn].append(complication)

# +
for mrn, complications in mrn_and_complications.items():
    if len(complications) == 1 and complications[0] == '0':
        n_wo_complications += 1
        
print(f"""
There are {n_wo_complications} patients who have no complications in any of their visits.
""")

# +
those_with_complications = {}

for mrn, complications in mrn_and_complications.items():
    
    actual_complications = []
    for complication in complications:
        if complication != '0':
            actual_complications.append(complication)
    
    if len(actual_complications) > 0:
        if mrn not in those_with_complications:
            those_with_complications[mrn] = (actual_complications)
        elif mrn in those_with_complications:
            those_with_complications[mrn].append(actual_complications)

# +
for mrn, complications in those_with_complications.items():
    
    new_list = []
    
    for complication in complications:
        complication = int(complication)
        complication_text = complications_legend[complication]
        new_list.append(complication_text)
    
    those_with_complications[mrn] = new_list
        
those_with_complications
# -


