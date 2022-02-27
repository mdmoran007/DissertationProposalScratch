# A simple file to count words per file
import os

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/'
LogFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/CleanLog.txt'
LettersList = []
OutList = [['Letter_File_Name', 'File_Word_Count']]
fnl = os.listdir(BaseLetterDir)
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)
        ffn = BaseLetterDir + fn
        f = open(ffn, "r")
        data = f.read()
        words = data.split()
        print (fn, len(words))
        OutList.append([fn, len(words)])

OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/wrd_cnt-v1.csv'
import csv
with open(OutFile, "w") as f:
    wr = csv.writer(f)
    wr.writerows(OutList)