# Author    : Lucero Rodriguez
# Date      : Tuesday November 24, 2020
# Assumption:
# Purpose   : This is the Stub class to test the classes written
#             and display the averages of the JSON string provided

from JSONDeserializer import JSONDeserializer


def find_and_display_average(sum_total, total, state):
    # average by state
    average = float(sum_total / total)
    print("The average number of employees per company in " + state + " is: " '%.2f' % average)


CA = 'CA'
AZ = 'AZ'

deserializer = JSONDeserializer("files/companyDetails.json")
deserialized_companies = deserializer.deserialize_json_to_object()

total_ca_emps = 0   # total number of employees in CA
ca_count = 0        # total number of object with reference to CA

total_az_emps = 0   # total number of employees in AZ
az_count = 0        # total number of object with reference to AZ

if len(deserialized_companies) > 0:
    for icompany in deserialized_companies:
        current_state = icompany.get_state()
        if CA == current_state:
            total_ca_emps += icompany.get_number_of_employees()
            ca_count += 1
        elif AZ in current_state:
            total_az_emps += icompany.get_number_of_employees()
            az_count += 1

    # california average
    find_and_display_average(total_ca_emps, ca_count, CA)

    # AZ average
    find_and_display_average(total_az_emps, az_count, AZ)
