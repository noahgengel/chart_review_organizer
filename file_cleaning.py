"""
File is used to do the following:
    1. Clean up the file by replacing 'old' numbers with 'new' numbers:
        - Comorbidities
        - Indications for TNE
        - Complications
        - Associated Esophageal Procedure
        - Abnormal Esophageal Endoscopic Findings
        - Abnormal Esophageal Biopsy Results

    2. Create 'tne' objects for each row for use in analysis
"""

import math
import pandas as pd
import os
from constants import file_name, columns_dictionary, \
    sheet_name, associated_dictionary, value_error_msg, \
    output_file

cwd = os.getcwd()
full_file_name = cwd + "/" + file_name

xl = pd.ExcelFile(full_file_name)
df = xl.parse(sheet_name)


def replace_numbers_in_cell(df, row_idx, column_idx, dictionary):
    """
    Function is used to:
        - select a particular cell
        - replace the 'numbers' in the cell with the
            more appropriate 'updated' numbers

    :param
    df (df): pandas df with the information

    :param
    row_idx (int): row to indicate the patient record

    :param
    column_idx (int): index of the column to be changed

    :param
    dictionary (dict): dictionary with the appropriate 'old
        to new' conversions

    :return:
    df (df): df of data - now with updated information
    """

    values = df.iloc[row_idx][column_idx]

    if isinstance(values, int):  # only one number
        values = str(values)  # convert to a string to match keys
        values = [values]  # convert to a list for iteration

    elif isinstance(values, str):
        values = values.splitlines()

    elif math.isnan(values):  # blank space - return immediately
        return df

    else:
        raise ValueError(
            value_error_msg.format(row_idx=row_idx, column_idx=column_idx,
                                   values=values, type=type(values)))

    replacement_string = ""
    new_values = []

    for value in values:

        new_number = dictionary[value]

        if new_number is None:  # original is deleted
            pass
        else:
            new_number = str(new_number)

            if new_number not in new_values:
                replacement_string += new_number + "\n"
                new_values.append(new_number)
            else:  # do not want duplicate values
                pass

    df.iat[row_idx, column_idx] = replacement_string  # replace

    return df


num_records = len(df.index) - 1  # take off headers

comorbities_idx = columns_dictionary["comorbidities_col"]
tne_indications_idx = columns_dictionary["tne_indication_col"]
complications_idx = columns_dictionary["complications_col"]
esophageal_procedure_idx = columns_dictionary["esophageal_procedure_col"]
laryngeal_procedure_idx = columns_dictionary["laryngeal_procedure_col"]
abnormal_esoph_findings_idx = columns_dictionary["abnormal_esoph_findings_col"]
biopsy_idx = columns_dictionary["abnormal_esophageal_biopsy_results"]

columns_to_replace = [
    comorbities_idx, tne_indications_idx, complications_idx,
    esophageal_procedure_idx, laryngeal_procedure_idx,
    abnormal_esoph_findings_idx, biopsy_idx]


for row in range(num_records):
    for column in columns_to_replace:

        # print(column)  # column for the associated dict
        dictionary = associated_dictionary[column]

        row_idx = row  # 1 below - skip headers

        df = replace_numbers_in_cell(
            df=df, row_idx=row_idx,
            column_idx=column, dictionary=dictionary)

df.to_excel(output_file)
