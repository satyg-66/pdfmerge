#!/bin/env python3

# AUTHOR: Jonas Ingemarsson
# DESC: A script to merge PDF-files to one single PDF.
# DATE: August 2, 2022
# DEPENDENCIES: PyPDF2

import os
from PyPDF2 import PdfMerger
from sys import argv
from glob import glob

pdfs = []

if len(argv) == 1:
    print("No valid argument given. Try --help")
    quit()

if argv[1] == ".":
    allFiles = os.listdir()
    for isPdf in allFiles:
        if isPdf in glob("*.pdf"):
            pdfs.append(isPdf)
    pdfs.sort()
elif argv[1] == "-h" or argv[1] == "--help":
    print("list PDF-files as arguments or use period (.) to merge all PDF-files in current directory.")
    quit()
else:
    for argument in argv[1:]:
        if argument in glob("*.pdf"):
            pdfs.append(argument)
    
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close