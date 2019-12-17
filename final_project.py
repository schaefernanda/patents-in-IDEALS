# final_project.py
# The Python script for my final project.

import csv
import json
import pathlib
import requests
from progressbar import ProgressBar

# Read in the CSV file obtained from the Office of Technology Management that contains all the inventors affiliated with the Urbana-Champaign campus.
OTM_inventors = []
with open('UIUC_inventors_OTM.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        OTM_inventors.append(dict(row))

csvfile.close()

# Read in the JSON response from the USPTO's PatentsView API containing metadata for all the patents issued to the Board of Trustees of the University of Illinois.
with open('PatentsView_API_response.json') as response:
    metadata = json.load(response)

# Create a list of the full names of the inventors in the OTM CSV file.
OTM_inventor_full_names = []

for inventor_information in OTM_inventors:
    OTM_inventor_full_name = inventor_information['full_name']
    OTM_inventor_full_names.append(OTM_inventor_full_name)

# Create a function that will return only the patents from the PatentsView API response whose inventors are in the OTM CSV file. This narrows down the patents to only those affiliated with the Urbana-Champaign campus.
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

# I was getting a lot of duplicates through the function, and the file was close to 10 GB in size, so refined the function and did the following list accumulator to get only the unique patents, and it worked!
unique_patents = []

for record in UIUC_patents:
    if record not in unique_patents:
        unique_patents.append(record)

# Save the unique patents affiliated with the Urbana-Champaign campus to a JSON file.
with open('UIUC_patents.json', 'w') as file_out:
    json.dump(unique_patents, file_out, indent=4)

# Download the patent PDF files. There are 1,068 files, so I included a progress bar to keep track of the time. This function involved creating the URL for the patent PDFs, which I did by consulting a formula mentioned in the narrative.
def get_patent_PDFs():
    target = pathlib.Path('patent_PDFs')
    pbar = ProgressBar()
    for item in pbar(unique_patents):
        patent_number = item['patent_number']
        first_portion = patent_number[-2:]
        second_portion = patent_number[2:5]
        third_portion = str(0) + patent_number[:2]
        url = "http://pimg-fpiw.uspto.gov/fdd/" + str(first_portion) + "/" + str(second_portion) + "/" + third_portion + "/0.pdf"
        myfile = requests.get(url)
        filename = patent_number + ".pdf"
        p = str(target / filename)
        with open(p, 'wb') as file:
            file.write(myfile.content)

get_patent_PDFs()

# Save the patent metadata into CSV file that could then be used for batch uploads to IDEALS. This followed the conventions for IDEALS.
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

outfile = open('IDEALS_batch_upload.csv', 'w')
csvout = csv.writer(outfile)
csvout.writerow(['BUNDLE:ORIGINAL', 'dc_title', 'dc_creator', 'dc_date_issued', 'dc_description_abstract', 'dc_identifier'])
csvout.writerows(allrows)


