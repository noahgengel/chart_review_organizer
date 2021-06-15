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

num_rows = len(tne_objects)

# +
encountered_mrns = []

for obj in tne_objects:
    if obj.mrn not in encountered_mrns:
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

    if obj.mrn not in encountered_mrns:
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
# -


# ## By patient statistics

# ### Let's look at the top comorbidities (% of patients with each comorbidity)
#     - NOTE: This takes ALL comorbidities that a patient ever has into account

# +
cm_dict = {}

for obj in tne_objects:  
    comorbidities = obj.co_morbidities[0]
    mrn = obj.mrn[0]
    
    if mrn not in cm_dict:
        cm_dict[mrn] = []
    
    if isinstance(comorbidities, str):
        comorbidities = comorbidities.splitlines()
        
        for cm in comorbidities:
            cm = int(cm)
            
            if cm not in cm_dict[mrn]:
                cm_dict[mrn].append(cm)
        
    elif math.isnan(comorbidities):
        pass
    
    elif isinstance(comorbidities, float):
        cm = int(comorbidities)  # put into a list
        
        if cm not in cm_dict[mrn]:
            cm_dict[mrn].append(cm)
    
    else:
        raise ValueError("Unanticipated type found")

# +
frequency_of_comorbidities = {}

for mrn, comorbidities in cm_dict.items():
    for cm in comorbidities:
        cm_name = comorbidities_legend[cm]
        
        if cm_name not in frequency_of_comorbidities:
            frequency_of_comorbidities[cm_name] = 1
        else:
            frequency_of_comorbidities[cm_name] += 1
# -

for cm, frequency in frequency_of_comorbidities.items():
    frequency_percent = round(frequency / num_distinct_mrns * 100, 1)
    frequency_of_comorbidities[cm] = frequency_percent

frequency_of_comorbidities

# +
frequency_of_comorbidities = dict(sorted(frequency_of_comorbidities.items(), key=lambda item: item[1]))

comorbidities = frequency_of_comorbidities.keys()
values = frequency_of_comorbidities.values()
# -

comorbidities

values

fig = plt.figure()
plt.bar(comorbidities, values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Comorbidity')
plt.ylabel('Percentage of Patients with Comorbidity')
plt.title(f"""Comorbidity Prevalence Amongst Patients (n={num_distinct_mrns})""")
plt.show()
plt.gcf().subplots_adjust(bottom=0.8)
fig.savefig('comorbidity_prevalence.png', bbox_inches="tight")


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


biopsy_dict, biopsy_results, biopsy_values = create_dictionary_for_visit_focused_statistics(
    attribute = "abnormal_biopsy_findings", 
    relevant_dictionary = esophageal_biopsy_legend,
    num_rows = num_rows)

biopsy_dict

fig = plt.figure()
plt.bar(biopsy_results, biopsy_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Abnormal Biopsy Result')
plt.ylabel('Percentage of Visits with Abnormal Biopsy Finding')
plt.title(f"""Abnormal Biopsy Result Frequency Amongst TNE Visits (n={num_rows})""")
plt.show()
fig.savefig('abnormal_biopsy_values.png', bbox_inches="tight")

abnormal_findings_dict, abnormal_findings, abnormal_values = create_dictionary_for_visit_focused_statistics(
    attribute = "abnormal_esoph_findings", 
    relevant_dictionary = esophageal_findings_legend,
    num_rows = num_rows)

fig = plt.figure()
plt.bar(abnormal_findings, abnormal_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Abnormal Esophageal Findings')
plt.ylabel('% of Visits with Abnormal Esophageal Findings')
plt.title(f"""Abnormal Esophageal Findings Frequency Amongst TNE Visits (n={num_rows})""")
plt.show()
fig.savefig('abnormal_esophageal_findings.png', bbox_inches="tight")

tne_indication_dict, tne_indications, tne_indication_values = create_dictionary_for_visit_focused_statistics(
    attribute = "tne_indication", 
    relevant_dictionary = tne_indication_legend,
    num_rows = num_rows)

fig = plt.figure()
plt.bar(tne_indications, tne_indication_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Indication for TNE')
plt.ylabel('% of Visits with TNE Indication')
plt.title(f"""Indication for TNE (n={num_rows})""")
plt.show()
fig.savefig('tne_indication_distribution.png', bbox_inches="tight")

esoph_procedures_dict, esoph_procedures, esoph_procedure_values = create_dictionary_for_visit_focused_statistics(
    attribute = "esoph_procedure", 
    relevant_dictionary = esophageal_procedure_legend,
    num_rows = num_rows)

print(type(esoph_procedures))

fig = plt.figure()
plt.bar(esoph_procedures, esoph_procedure_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Esophageal Procedure')
plt.ylabel('% of Visits with Esophageal Procedure')
plt.title(f"""Percentage of Visits with Esophageal Procedure (n={num_rows})""")
plt.show()
fig.savefig('esophageal_procedures.png', bbox_inches="tight")

complications_dict, complications, complications_values = create_dictionary_for_visit_focused_statistics(
    attribute = "complications", 
    relevant_dictionary = complications_legend,
    num_rows = num_rows)

fig = plt.figure()
plt.bar(complications, complications_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Complication')
plt.ylabel('% of Visits with Reported Complication')
plt.title(f"""TNE Complication Frequency (n={num_rows})""")
plt.show()
fig.savefig('tne_complication_frequency.png', bbox_inches="tight")

# ## Below are selected graphs IF NOT NONE

biopsy_values = list(biopsy_values)[:-1]
biopsy_values = np.array(biopsy_values)

biopsy_results = list(biopsy_results)[:-1]
biopsy_results = np.array(biopsy_results)

fig = plt.figure()
plt.bar(biopsy_results, biopsy_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Abnormal Biopsy Result (if any abnormal result reported)')
plt.ylabel('Percentage of Total Biopsies')
plt.title(f"""Abnormal Biopsy Result Frequency Amongst Total Biopsies (n={num_rows})""")
plt.show()
fig.savefig('abnormal_biopsy_values_excluding_none.png', bbox_inches="tight")

complications_values = list(complications_values)[:-1]
complications_values = np.array(complications_values)

complications = list(complications)[:-1]
complications = np.array(complications)

fig = plt.figure()
plt.bar(complications, complications_values, color=(0.2, 0.4, 0.6, 0.6))
plt.xticks(rotation=90)
plt.xlabel('Complication')
plt.ylabel('% of Visits with Reported Complication (excluding none)')
plt.title(f"""TNE Complication Frequency, Excluding None (n={num_rows})""")
plt.show()
fig.savefig('tne_complication_frequency_excluding_none.png', bbox_inches="tight")
