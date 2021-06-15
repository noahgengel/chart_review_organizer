"""
File is used to define a class that should enable storage of the
different columns of an entry
"""


class tne_row:
    """
    Class is used to store the information for each row in the
    SLP data sheet.
    """

    def __init__(
        self, name, mrn, dob, age, sex, race,
        procedure_date, co_morbidities, prev_barium_swallow,
        tne_indication, surgeon, slp, completion, complications,
        esoph_procedure, laryngeal_procedure, abnormal_esoph_findings,
        cpt_code, icd_code):

        """
        This class should contain all of the relevant data from a row
        of information from the TNE SLP data sheet.


        :param name (str):
            patient name

        :param mrn (int):
            mrn of the patient

        :param dob (datetime):
            patient's date of birth

        :param age (int):
            patient age at time of procedure

        :param sex (int)
            age of patient (1 = male, 2 = female)

        :param race (int)
            race of patient
                1 = white, non-hispanic
                2 = other, hispanic
                3 = black
                4 = asian

        :param procedure_date (datetime):
            date of the procedure

        :param co_morbidities (list):
            list of the relevant co-morbidities of the patient

        :param prev_barium_swallow (int):
            number that represents whether or not the patient
            had a previous barium study

        :param tne_indication (list):
            list of the indications for the TN

        :param surgeon (str):
            name of the surgeon

        :param slp (str):
            name of the SLP for the procedure

        :param completion (int):
            number that represents whether the study was
            successfully completed

        :param complications (list):
            list of numbers that represents the complications
            encountered during the TNE

        :param esoph_procedure (list):
            list of numbers that represents the performed
            esophageal procedures

        :param laryngeal_procedure (list):
            list of numbers that represents the performed
            laryngeal procedures

        :param abnormal_esoph_findings (list):
            list of numbers that represents abnormal
            findings within the TNE

        :param cpt_code (int):
            cpt codes billed

        :param icd_code (str):
            icd billing code
        """

        self.name = name,
        self.mrn = mrn,
        self.dob = dob,
        self.age = age,
        self.sex = sex,
        self.race = race,
        self.procedure_date = procedure_date,
        self.co_morbidities = co_morbidities,
        self.prev_barium_swallow = prev_barium_swallow,
        self.tne_indication = tne_indication,
        self.surgeon = surgeon,
        self.slp = slp,
        self.completion = completion,
        self.complications = complications,
        self.esoph_procedure = esoph_procedure,
        self.laryngeal_procedure = laryngeal_procedure,
        self.abnormal_esoph_findings = abnormal_esoph_findings,
        self.cpt_code = cpt_code,
        self.icd_code = icd_code
