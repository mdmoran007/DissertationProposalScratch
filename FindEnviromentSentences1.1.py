# A simple file to find forms of "environment" and "climate" not near "economic"
# Will deliver results in same format as other searches (after a little work).

# Now need to get to the good bits from FindStakeholderSentences.py incorporated.
# This is the lay-out of the outfile.
import os
import csv

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/'
LettersList = []
OutList = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Specific_Term', 'Stakeholder_Group']] # Salutation
fnl = os.listdir(BaseLetterDir)
print (fnl)

for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)
        ffn = BaseLetterDir + fn
        f = open(ffn, "r")
        data = f.read()
        words = data.split()
        print (words)
        for i in range(0,len(words)):
            if ("environment" in words[i].lower() or "climate" in words[i].lower() or "sustainab" in words[i].lower()) \
                    and not ("econom" in words[i-1].lower() or "economic" in words[i-2].lower() or "economic" in words[i-3].lower())\
                    and not ("politic" in words[i-1].lower() or "politic" in words[i-2].lower() or "politic" in words[i-3].lower()):
                print(fn, fn.split('-')[0], fn.split('-')[2][2:6], words[i], 'Environment')
                if i > 5:
                    print(words[i-5:i+1])
                OutList.append([fn, fn.split('-')[0], fn.split('-')[2][2:6], words[i], 'Environment'])

OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/env-v1.csv'
with open(OutFile, "w") as f:
    wr2 = csv.writer(f)
    wr2.writerows(OutList)
