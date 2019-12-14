# fschaef2_final_project.py
# This is the code I have for my final project.

import csv
import json
import pathlib
import requests
from progressbar import ProgressBar

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

# def get_patent_PDFs():
# #     target = pathlib.Path('fschaef2_patent_PDFs')
# #     pbar = ProgressBar()
# #     for item in pbar(unique_patents):
# #         patent_number = item['patent_number']
# #         first_portion = patent_number[-2:]
# #         second_portion = patent_number[2:5]
# #         third_portion = str(0) + patent_number[:2]
# #         url = "http://pimg-fpiw.uspto.gov/fdd/" + str(first_portion) + "/" + str(second_portion) + "/" + third_portion + "/0.pdf"
# #         myfile = requests.get(url)
# #         filename = patent_number + ".pdf"
# #         p = str(target / filename)
# #         with open(p, 'wb') as file:
# #             file.write(myfile.content)
# #
# # get_patent_PDFs()
# #
with open('fschaef2_UIUC_patents.json', 'w') as file_out:
    json.dump(unique_patents, file_out, indent=4)

allrows = []

for record in unique_patents:
    row = []
    BUNDLE_ORIGINAL = record['patent_number'] + ".pdf"
    inventors = record['inventors']
    dc_creator = []
    for inventor_information in inventors:
        inventor_last_name = inventor_information['inventor_last_name']
        inventor_first_name = inventor_information['inventor_first_name']
        IDEALS_creator = str(inventor_last_name) + ", " + str(inventor_first_name)
        dc_creator.append(IDEALS_creator)
    dc_title = record['patent_title']
    dc_date_issued = record['patent_date']
    dc_description_abstract = record['patent_abstract']
    dc_identifier = record['patent_number']
    row.append(BUNDLE_ORIGINAL)
    row.append(dc_title)
    row.append(dc_creator)
    row.append(dc_date_issued)
    row.append(dc_description_abstract)
    row.append(dc_identifier)
    allrows.append(row)

outfile = open('fschaef2_IDEALS_batch_upload.csv', 'w')
csvout = csv.writer(outfile)
csvout.writerow(['BUNDLE:ORIGINAL', 'dc_title', 'dc_creator', 'dc_date_issued', 'dc_description_abstract', 'dc_identifier'])
csvout.writerows(allrows)




