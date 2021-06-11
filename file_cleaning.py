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

import xlrd
import os
from constants import file_name
from comorbidities_dictionaries import co_morbidities

cwd = os.getcwd()
full_file_name = cwd + "/" + file_name

wb = xlrd.open_workbook(full_file_name)
sheet = wb.sheet_by_index(0)
print(type(sheet))

def replace_numbers_in_cell(sheet, row_idx, column_idx, dictionary):
    """
    Function is used to:
        - select a particular cell
        - replace the 'numbers' in the cell with the
            more appropriate 'updated' nubmers

    :param
    sheet (sheet): sheet of data

    :param
    row_idx (int): row to indicate the patient record

    :param
    column_idx (int): index of the column to be changed

    :param
    dictionary (dict): dictionary with the appropriate 'old
        to new' conversions

    :return:
    sheet (sheet): sheet of data - now with updated information
    """

    # values is a string
    values = sheet.cell_value(row_idx, column_idx)
    values = values.splitlines()

    replacement_string = ""

    for value in values:
        new_number = dictionary[value]
        new_number = str(new_number)
        replacement_string += new_number + "\n"

    # sheet.cell_value(row_idx, column_idx) = replacement_string



