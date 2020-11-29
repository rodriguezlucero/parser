from Company import Company


# Author    : Lucero Rodriguez
# Date      : Tuesday November 24, 2020
# Assumption: The "string" data provided is in valid JSON form
# Purpose   : This deserializer was written without any external libraries
#             as requested. It deserializes a JSON file into the Company equivalent Object

class JSONDeserializer:
    MAX_OBJECTS = 3  # max objects in json array file
    LEFT_BRACE = "{"  # the left curly brace to indicate the start of a json object
    RIGHT_BRACE = "}"  # the right curly brace to indicate the end of a json object

    # the json file path
    __file_name = None

    def __init__(self, in_file):
        self.__file_name = in_file

    # Purpose    :  To deserialize a json file to it's Company object equivalent
    # Assumptions:  The data in the json file is 1 array of 3 objects.
    #               Each object has 3 key/value pairs composed with the
    #               following 3 keys: State, Company, NumOfEmployees
    # Params     :  N/A
    # Returns    :  companies the list of deserialized Company objects
    def deserialize_json_to_object(self):
        raw_items = []
        companies = []
        ending_brace = False
        with open(self.__file_name, "r") as file:
            for line in file:
                if self.LEFT_BRACE in line:
                    ending_brace = False
                elif self.RIGHT_BRACE in line:
                    ending_brace = True

                if not ending_brace and self.LEFT_BRACE not in line and "[" not in line:
                    raw_items.append((line.replace('\n', '').replace('"', '').replace(',', '').strip()).split(':'))

                    if len(raw_items) == self.MAX_OBJECTS:
                        company = Company()
                        for iRawItem in raw_items:
                            if "State" in iRawItem:
                                company.set_state(iRawItem[1].strip())
                            elif "Company" in iRawItem:
                                company.set_company(iRawItem[1].strip())
                            elif "NumOfEmployees" in iRawItem:
                                company.set_number_of_employees(int(iRawItem[1].strip()))
                        companies.append(company)
                        raw_items.clear()
        return companies
