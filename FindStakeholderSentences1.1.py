# FindStakeholderSentences.py ------------------------------------------------------------------------------
# A simple script to find sentences containing stakeholders in the 15 candidate letters and evaluate with BERT
# The steps:
#   - Load up base lists
#   - Load files into strings
#   - Search files for my strings and return those sentences
#   - Write those sentences out to a csv that is picked up by BertSemanticSentenceSimilarity.py in the M3 Dissertation PyCharm project
# That files searches through and masks the base term in a way that does not alter any sentence lengths.
#
# Mark Moran, markdm2@illinois.edu
# November 15, 2021
# --------------------------------------------------------------------------------------------------
# February 2022
# Now I need to expand this to simply pull every file from a directory for Paper 1,
# instead of a discrete list of files. That is not too hard.
# Copied from cfg.py until I get that working
# Classes of stakeholders currently evaluated
# ---------------------------------------------------------------------------------------------------
import os
import csv
from datetime import datetime

OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/sh1-v2.csv'
out_file = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/sh1-v2.csv'

#ShCatList = ['employee', 'investor', 'customer', 'supplier', 'society', 'community', 'dealer',
#             'stakeholder', 'environment', 'regulator', 'competitor']
ShCatList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder']
#ShList = ['e', 'i', 'c', 'u', 'o', 'm', 'd', 't', 'n', 'r', 'p']
ShList = ['e', 'i', 'c', 'u', 'm', 't']
MaskDic = {}
dfl = []
# Efficient way to merge above two lists into dictionaries.
for key in ShCatList:
   for value in ShList:
      MaskDic[key] = value
      ShList.remove(value)
      break
print (MaskDic)

ShCatBaseListDic = {}  # Holds just the base ones I identified
ShCatBaseListDic['employee'] = ['employee', 'workforce', 'work force', 'personnel', 'our people', 'associate', 'worker']
ShCatBaseListDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'bondholder', 'lender' ]
ShCatBaseListDic['customer'] = ['customer', 'client', 'clientele', 'consumer', 'buyer']
ShCatBaseListDic['supplier'] = ['supplier', 'supply base', 'business partner']
ShCatBaseListDic['community'] = ['community', 'city', 'communities', 'cities', 'town', 'society', 'societies']
#ShCatBaseListDic['society'] = ['society']
#ShCatBaseListDic['dealer'] = ['dealer', 'distributor', 'wholesaler', 'retailer', 'channel']
ShCatBaseListDic['stakeholder'] = ['stakeholder']
#ShCatBaseListDic['environment'] = ['environment', 'climate']
#ShCatBaseListDic['regulator'] = ['regulator', 'agency', 'agencies']
#ShCatBaseListDic['competitor'] = ['competitor', 'competition']

# See if log file exist. If it does, load its cotent into a list. If not, create a new empty one.
log_file = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Logs/sh_log2.txt'
if os.path.exists(log_file): # Log file exists
    fl = open(log_file, 'r', encoding = 'latin1')
    done_files_list = fl.readlines()
    for i in done_files_list:
        dfl.append(i.strip('\n'))
    print (dfl)
    if 'IBM-CL1-FY2018.txt' in dfl:
        print ('IBM-CL1-FY2018.txt in dfl')
else: # No log file...make a new one.
    fl = open(log_file, 'w')
    fl.write('Files Complete\n')
    fl.close()

# Build list of letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt/'
LettersList = []
fnl = os.listdir(BaseLetterDir)
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)

# Check for outfile. Build header if it does not exist.
OutList = [['Letter_File_Name', 'Sentence_Token_Count', 'Sent_ID','Total_Letter_Sentences', 'Specific_Term', 'Stakeholder_Group', 'Sentence_Text']]
out_list = []
out_header = ['Letter_File_Name', 'Sentence_Token_Count', 'Sent_ID','Total_Letter_Sentences', 'Specific_Term', 'Stakeholder_Group', 'Sentence_Text']
if not os.path.exists(out_file):
    fo = open(out_file, "w")
    fo_csv = csv.writer(fo)
    fo_csv.writerow(out_header)
    fo.close()

import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')

# Load up Stanza and turn documents into sentences.
j = 0
for ltr in LettersList:
    if ltr in dfl:
        print (ltr, "in", dfl)
    else:
        print (ltr, "not in", dfl)
        dfl.append(ltr)
        j = j + 1
        full_infile_path = BaseLetterDir + ltr

        inputfile = open(full_infile_path, mode='r', encoding='utf-8', errors='ignore')
        text1 = inputfile.read()
        print(j, '--------------------', datetime.now(), ltr, '-----------------------') # Moving this forward to improve de-bug. Likely just puking on gibberish characters.
        doc = nlp(text1)
        for i, sent in enumerate(doc.sentences):
            for sh in ShCatList:
                for w in ShCatBaseListDic[sh]:
                    if w in (sent.text).lower() and len (sent.words) > 9 :
                        # These lines catch the cases where the plural and singular terms end differently.
                        # I should really re-write the whole section to move to detecting lemmas.
                        # More processor-intensive, but more reliable.
                        # That said, I can capture these with nothing in the lists in the next file and not write them.
                        if w == 'communities':
                            w_prime = 'community'
                        elif w == 'cities':
                            w_prime = 'city'
                        elif w == 'societies':
                            w_prime = 'society'
                        elif w == 'agencies':
                            w_prime = 'agency'
                        else:
                            w_prime = w
                        print (ltr, ':', len(sent.tokens), ';', i, '/', len(doc.sentences), '.', w_prime, '(', sh, ')', ':', sent.text)
                        out_list.append([ltr, len(sent.tokens), i, len(doc.sentences), w_prime, sh, sent.text])
        fo = open(out_file, "a")
        fo_csv = csv.writer(fo)
        fo_csv.writerows(out_list)
        fo.close()
        out_list = []
# Append file name to log file
        fl = open(log_file, 'a')
        fl.write(ltr)
        fl.write('\n')
        fl.close()


# Write OutList to a file
#OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/sh1-v1.csv'
#import csv
#with open(OutFile, "w") as f:
#    wr = csv.writer(f)
#    wr.writerows(OutList)


# This picks up in the M3 - Dissertation project
# I made some manual changes in sh2 to get it ready (calculated position)...I could bring that in here if I wanted to.