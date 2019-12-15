# patents-in-IDEALS
A repository for my final project for the IS 452: Foundations of Information Processing class at the iSchool at Illinois. In this project, I explored a way to get metadata and files for patents granted to the Board of Trustees of the University of Illinois into the IDEALS institutional repository. Being that IDEALS hosts scholarly work only from the Urbana-Champaign campus, a significant portion of this project involved narrowing down the patents to only those issued to inventors affiliated with the Urbana-Champaign campus. For this purpose, inventor data from the Office of Technology Management was obtained. 

## Purpose and Overview
Institutional repositories are digital repositories that house an academic institution's scholarly output, such as theses and dissertations, conference proceedings and presentations, working papers, technical reports, and more. Some universities have also started to include their institution's issued patents into their repositories, which is a current goal for IDEALS, the instituional repository of the University of Illinois at Urbana-Champaign. This project is an exploration into how to achieve this goal. It involves gathering patent metadata from the United States Patent and Trademark Office's [PatentsView API](https://developer.uspto.gov/api-catalog/patentsview), downloading patent PDFs, and exporting the processed metadata into a CSV file that follows the IDEALS conventions and that can be used for batch uploading patent information to the repository. 

## Repository Contents
This repository contains:
* This README file
* A Python script that processes patent metadata, downloads patent PDF files, and exports the processed metadata into a CSV file
(Both the final and the draft versions of the script are included)
* A manifest file describing the files and folder structures in this project
* The original and exported data from this project
* A folder containing the downloaded patent PDF files
