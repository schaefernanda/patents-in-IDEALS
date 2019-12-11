# fschaef2_final_project.py
# This is the code I have for my final project.

import csv
import json

OTM_inventors = []
with open('fschaef2_UIUC_inventors_OTM.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        OTM_inventors.append(dict(row))

csvfile.close()

with open('fschaef2_PatentsView_API_response.json') as response:
    metadata = json.load(response)

OTM_inventor_full_names = []

for inventor_information in OTM_inventors:
    OTM_inventor_full_name = inventor_information['full_name']
    OTM_inventor_full_names.append(OTM_inventor_full_name)

# print(OTM_inventor_full_names)

def get_patent_information():
    patents = metadata['patents']
    UIUC_affiliated_patents = list(set())
    for patent_information in patents:
        inventors = patent_information['inventors']
        for inventor_information in inventors:
            inventor_last_name = inventor_information['inventor_last_name']
            inventor_first_name = inventor_information['inventor_first_name']
            inventor_full_name = str(inventor_first_name) + " " + str(inventor_last_name)
            if inventor_full_name in OTM_inventor_full_names:
                UIUC_affiliated_patents.append(patent_information)
            else:
                pass # print("This patent is from another campus.")
    return UIUC_affiliated_patents

UIUC_patents = get_patent_information()

unique_patents = []

for record in UIUC_patents:
    if record not in unique_patents:
        unique_patents.append(record)

PDF_URLs = []

for item in unique_patents:
    patent_number = item['patent_number']
    first_portion = patent_number[-2:]
    second_portion = patent_number[2:5]
    third_portion = str(0) + patent_number[:2]
    URL = "http://pimg-fpiw.uspto.gov/fdd/" + str(first_portion) + "/" + str(second_portion) + "/" + third_portion + "/0.pdf"
    PDF_URLs.append(URL)

print(PDF_URLs)

# with open('fschaef2_UIUC_patents.json', 'w') as file_out:
#     json.dump(unique_patents, file_out, indent=4)



