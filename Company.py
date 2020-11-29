# Author    : Lucero Rodriguez
# Date      : Tuesday November 24, 2020
# Assumption: The JSON data returned in the object consists of:
#             State, Company, and NumOfEmployees
# Purpose   : This class will be used to store the deserialized version of the JSON

class Company:
    __state = ""
    __company = ""
    __numberOfEmployees = 0

    def __init__(self):
        pass

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_number_of_employees(self):
        return self.__numberOfEmployees

    def set_number_of_employees(self, number_of_employees):
        self.__numberOfEmployees = number_of_employees
