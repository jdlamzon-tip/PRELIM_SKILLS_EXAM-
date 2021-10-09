#date reported = dateRep
#countries and territories = countriesAndTerritories
#no. of cases = cases
#no. of deaths = deaths

import json
import csv

with open('/home/devasc/Lamzon_Prelim_Skills/TEST_C/covid_cases.json') as covid:
    covid_data = json.loads(covid.read())

with open('/home/devasc/Lamzon_Prelim_Skills/TEST_C/parsed_json.csv', 'w') as parsed_json:
    csv.file = csv.writer(parsed_json)
    csv.file.writerow([
        "dateRep",
        "countriesAndTerritories",
        "cases",
        "deaths"
        ])
    for data in covid_data["records"]:
        csv.file.writerow([
            data["dateRep"],
            data["countriesAndTerritories"],
            data["cases"],
            data["deaths"],
        ])
