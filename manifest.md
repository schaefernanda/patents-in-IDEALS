# Manifest File
The following are the files and folder structures in this project.

**Folders**:
* patent_PDFs

**Files**:
* .DS Store
* .gitignore
* LICENSE
* README
* IDEALS_batch_upload.csv
* PatentsView_API_response.json
* UIUC_inventors_OTM.csv
* UIUC_patents.json
* final_project.py
* final_project_check_in.py

## Descriptions

### patent_PDFs folder
This folder contains the 1,068 patent PDF files that were downloaded using the *get_patent_PDFs()* function in the Python script. Each file is named as *patent_number.pdf*.


### .DS Store
This file was automatically generated at some point while running my Python script. I am not entirely sure of its purpose, but I think it stores information about the folder in which it resides. This file was likely generated because I worked on this project using a Mac computer. 


### .gitignore
This file was generated when I ignored the first "UIUC_patents.json" export because it was almost 10 GB in size. It is currently empty because I am not ignoring anything.


### LICENSE
This file contains the MIT License that I granted for this project. 


### README
This Markdown file contains information about the project, the contents in the repository, and the requirements of the project.  


### IDEALS_batch_upload.csv *(Outfile)*
This CSV file was exported at the end of the Python script, and it contains the metadata necessary to batch upload patent information to the IDEALS institutional repository. The columns include:
* BUNDLE_ORIGINAL
(The file name of the PDF file associated with the patent metadata)
* dc_title
(The title of the patented invention)
* dc_creator
(The named inventors of the patented invention)
* dc_date_issued
(The date when the patent was issued)
* dc_description_abstract
(The abstract of the patented invention)
* dc_identifier
(The patent number of the patented invention)


### PatentsView_API_response.json *(Infile)*
This JSON file contains the response that was returned from a call to the United States Patent and Trademark Office's PatentsView API using Postman. The file was read into the script in order to process the patent metadata.


### UIUC_inventors_OTM.csv *(Infile)*
This CSV file contains the first, last, and full names of the inventors who are affiliated with the University of Illinois at Urbana-Champaign and who have been named on issued patents. The file was read into the script in order to crossreference the inventors who were listed in the PatentsView API so that I could narrow down the patents to only those that are affiliated with the University of Illinois at Urbana-Champaign campus. 


### UIUC_patents.json *(Outfile)*
This JSON file contains only the metadata for unique patents that are affiliated with the University of Illinois at Urbana-Champaign campus. It was generated using the *get_patent_information()* function in the Python script and the for loop in lines 49-53. Please see lines 31-57 for the entire process of narrowing down the patents and exporting the patent metadata into a JSON file.


### final_project.py
This is the Python script written to process patent metadata, download patent PDF files, and export the processed metadata into a CSV file. 


### final_project_check_in.py
This file is the first version of the code, which was turned in as part of the check-in portion of the final project. It contains my first explorations into how to solve this patent processing problem.
