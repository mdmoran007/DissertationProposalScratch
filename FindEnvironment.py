# A simple file to find forms of "environment" and "climate" not near "economic"
# Will deliver results in same format as other searches (after a little work).
import os
import csv

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/'
LogFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/CleanLog.txt'
LettersList = []
print ('h1')
OutList = [['Letter_File_Name', 'File_Word_Count']]
OutList2 = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Investor', 'Employee', 'Customer', 'Community', 'Supplier', 'Stakeholder']] # Salutation
OutList3 = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Investor', 'Employee', 'Customer', 'Community', 'Supplier', 'Stakeholder']] # Valediction
print ('h2')
fnl = os.listdir(BaseLetterDir)
print (fnl)
print ('h3')
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)
        ffn = BaseLetterDir + fn
        f = open(ffn, "r")
        data = f.read()
        words = data.split()
        print (words)