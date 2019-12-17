# patents-in-IDEALS
A repository for my final project for the IS 452: Foundations of Information Processing class at the iSchool at Illinois. In this project, I explored a way to get metadata and files for patents granted to the Board of Trustees of the University of Illinois into the [IDEALS institutional repository](https://www.ideals.illinois.edu). Being that IDEALS hosts scholarly work only from the Urbana-Champaign campus, a significant portion of this project involved narrowing down the patents to only those issued to inventors affiliated with the Urbana-Champaign campus. For this purpose, inventor data from the [Office of Technology Management](https://otm.illinois.edu) was obtained. 

## Purpose and Overview
Institutional repositories are digital repositories that house an academic institution's scholarly output, such as theses and dissertations, conference proceedings and presentations, working papers, technical reports, and more. Some universities have also started to include their institution's issued patents into their repositories, which is a current goal for IDEALS, the institutional repository of the University of Illinois at Urbana-Champaign. This project is an exploration into how to achieve this goal. It involves gathering patent metadata from the United States Patent and Trademark Office's [PatentsView API](https://developer.uspto.gov/api-catalog/patentsview), downloading patent PDF files, and exporting the processed metadata into a CSV file that follows the IDEALS conventions and that can be used for batch uploading patent information to the institutional repository. 

## Repository Contents
This repository contains:
* This README file
* A Python script that processes patent metadata, downloads patent PDF files, and exports the processed metadata into a CSV file
(Both the final and the draft versions of the script are included)
* A manifest file describing the files and folder structures in this project
* The original and exported data from this project
* A folder containing the downloaded patent PDF files

## Project Requirements
The Python script uses the progressbar2 package when downloading the patent PDF files. The package can be installed through pip (`pip install progressbar2`). Documentation for the progressbar2 package can be found in the [package's Python Package Index page](https://pypi.org/project/progressbar2/).

## Overview of How the Code Works
The code is broken down into several steps. First, it reads in the *UIUC_inventors_OTM.csv* and *PatentsView_API_response.json* files. Then, there is a list accumulator to gather the full names of the inventors that are affiliated with the University of Illinois at Urbana-Champaign. After that, the *get_patent_information()* function narrows down the patents in the JSON file to only those whose inventors are affiliated with the Urbana-Champaign campus. There is a list accumulator that follows to make sure that only the unique patents are saved and then exported to a new JSON file. Then, the *get_patent_PDFs()* function constructs the URLs for the patent PDF files and downloads them. The last section of the code exports the processed patent metadata to a CSV file. 

## Notes on How to Run the Code
The Python script can be run as is, but please make sure that the *UIUC_inventors_OTM.csv* and *PatentsView_API_response.json* files are in the same directory as the Python script. Because the script downloads 1,068 PDF files, you may choose to comment out the *get_patent_PDFs()* function to save yourself a lot of waiting time. 
