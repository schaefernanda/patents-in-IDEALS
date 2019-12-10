# fschaef2_final_project_check_in.py
# This is the code I have for my final project so far.

import csv

OTM_inventors = []
with open('fschaef2_UIUC_inventors_OTM.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        OTM_inventors.append(dict(row))

csvfile.close()

OTM_inventor_first_names = []

for inventor_information in OTM_inventors:
    OTM_inventor_first_name = inventor_information['first_name']
    OTM_inventor_first_names.append(OTM_inventor_first_name)

# print(OTM_inventor_first_names)

OTM_inventor_last_names = []

for inventor_information in OTM_inventors:
    OTM_inventor_last_name = inventor_information['last_name']
    OTM_inventor_last_names.append(OTM_inventor_last_name)

# print(OTM_inventor_last_names)

OTM_inventor_full_names = []

for inventor_information in OTM_inventors:
    OTM_inventor_full_name = inventor_information['full_name']
    OTM_inventor_full_names.append(OTM_inventor_full_name)

# print(OTM_inventor_full_names)


import json

with open('fschaef2_PatentsView_API_response.json') as response:
    metadata = json.load(response)

API_inventor_first_names = []

def get_inventor_first_name():
    patents = metadata['patents']
    for patent_information in patents:
        inventors = patent_information['inventors']
        for inventor_information in inventors:
            inventor_first_name = inventor_information['inventor_first_name']
            API_inventor_first_names.append(inventor_first_name)

get_inventor_first_name()
# print(API_inventor_first_names)

API_inventor_last_names = []

def get_inventor_last_name():
    patents = metadata['patents']
    for patent_information in patents:
        inventors = patent_information['inventors']
        for inventor_information in inventors:
            inventor_last_name = inventor_information['inventor_last_name']
            API_inventor_last_names.append(inventor_last_name)

get_inventor_last_name()
# print(API_inventor_last_names)

API_inventor_full_names = []

def get_inventor_full_name():
    patents = metadata['patents']
    for patent_information in patents:
        inventors = patent_information['inventors']
        for inventor_information in inventors:
            inventor_last_name = inventor_information['inventor_last_name']
            inventor_first_name = inventor_information['inventor_first_name']
            inventor_full_name = str(inventor_first_name) + " " + str(inventor_last_name)
            API_inventor_full_names.append(inventor_full_name)

get_inventor_full_name()
# print(API_inventor_full_names)

def overlap(list1, list2):
    return list(set(list1) & set(list2))

UIUC_affiliated_inventors = overlap(OTM_inventor_full_names,API_inventor_full_names)
print(len(UIUC_affiliated_inventors))
print(UIUC_affiliated_inventors)










