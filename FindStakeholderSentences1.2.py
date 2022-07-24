# FindStakeholderSentences.py ------------------------------------------------------------------------------
# A simple script to find sentences containing stakeholders in the 15 candidate letters and evaluate with BERT
# The steps:
#   - Load up base lists
#   - Load files into strings
#   - Search files for my strings and return those sentences
#   - Write those sentences out to a csv that is picked up by BertSemanticSentenceSimilarity.py in
#     the M3 Dissertation PyCharm project
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
# May 2022 - v 1.2
# Expanding this based on what I have learned. Major goals:
#   - Integrate environment stakeholder group into same file.
#   - Add logic (from environment) to look for preceding words that change meaning
#   - Add logic to process two-word phrases
#   - Improve overall flow and logic to increase ease of future extensibility.

import os  # for finding files
import csv  # for writing csv's
from datetime import datetime  # for console-logging
import stanza  # for finding sentences.

out_file = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/sh4-v1.csv'

ShCatBaseListDic = {'employee': ['employee', 'workforce', 'work force', 'personnel', 'our people', 'associate',
                                 'worker',
                                 'staff', 'headcount', 'colleague'],
                    'investor': ['investor', 'shareholder', 'stockholder', 'financier', 'bondholder', 'lender',
                                 'shareowner', 'creditor'],
                    'customer': ['customer', 'client', 'clientele', 'consumer', 'buyer',
                                 'guest', 'subscriber', 'policyholder'],
                    'supplier': ['supplier', 'supply base', 'business partner'],
                    'community': ['community', 'city', 'communities', 'cities', 'town', 'society', 'societies',
                                  'neighborhood'],
                    'stakeholder': ['stakeholder'],
                    'environment': ['environment', 'climate', 'sustainability']}  # Added back in with v1.2
ShCatList = list(ShCatBaseListDic.keys())  # This is also a re-work. More Pythonic, I think.
print (ShCatList)
# End var's brought straight from v1.2
MatchList = []
FailList = []
# New var's required for enhanced match: -------------------------------------------------------------------------------
st_suffix_list = ['city']  # These stakeholder terms can also be suffixes and require a space before them to count.
st_wordforms_dic = {'associate': ['associated', 'associating'], 'staff': ['staffed', 'staffing']}
st_polysemy_dic = {'environment': ['econom', 'financ', 'business', 'invest', 'legal', 'interest', 'work', 'politic'],
                   'climate': ['econom', 'financ', 'business', 'invest', 'legal', 'interest', 'work', 'politic']}

# Assemble all of the odd terms into one list to test later. If new categories were added, this would need to change.
# I need to move over these lines.
odd_terms_list = st_suffix_list + list(st_wordforms_dic.keys()) + list(st_polysemy_dic.keys())
print(odd_terms_list) # Make sure it looks right.
# A few lines to test that the structures are correct...prolly don't need these in the new file
for k in st_wordforms_dic.keys():
    for wf in st_wordforms_dic[k]:
        print(k, wf)
for k in st_polysemy_dic.keys():
    for p in st_polysemy_dic[k]:
        print(k, p)

dfl = []  # done files list

# See if log file exist. If it does, load its content into a list. If not, create a new empty one.
log_file = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Logs/sh_log4-v1.txt'
if os.path.exists(log_file):  # Log file exists
    fl = open(log_file, 'r', encoding='latin1')
    done_files_list = fl.readlines()
    for i in done_files_list:
        dfl.append(i.strip('\n'))
    print(dfl)
else:  # No log file...make a new one.
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
out_list = []
out_header = ['Letter_File_Name', 'Sentence_Token_Count', 'Sent_ID', 'Total_Letter_Sentences', 'Specific_Term',
              'Stakeholder_Group', 'Sentence_Text']
if not os.path.exists(out_file):
    fo = open(out_file, "w")
    fo_csv = csv.writer(fo)
    fo_csv.writerow(out_header)
    fo.close()

# Load up Stanza and turn documents into sentences.
stanza.download('en')
nlp = stanza.Pipeline('en')

# Just some accounting variables
match_count = 0
fail_count = 0
total_count = 0

j = 0
for ltr in LettersList:
    if ltr in dfl:
        print(ltr, "in", dfl)
    else:
        print(ltr, "not in", dfl)
        dfl.append(ltr)
        j = j + 1
        full_infile_path = BaseLetterDir + ltr

        inputfile = open(full_infile_path, mode='r', encoding='utf-8', errors='ignore')
        text1 = inputfile.read()
        print(j, '--------------------', datetime.now(), ltr, '-----------------------')
        doc = nlp(text1)
        for i, sent in enumerate(doc.sentences):
            for sh in ShCatList:  # sh is the stakeholder groups
                for w in ShCatBaseListDic[sh]:  # w is the words we are looking for, the stakeholder terms
                    if w in sent.text.lower() and len(
                            sent.words) >= 6:  # Changed from nine previously. Basic gateway test
                        # The above tells us that there is a match, so if it's not an edge case, it's simple.
                        total_count = total_count + 1
                        match_flag = False
                        match_term = ''
                        match_type = 'none'
                        if w not in odd_terms_list:
                            print(w, 'not in', odd_terms_list)
                            match_flag = True
                            match_term = w
                            match_type = 'basic'
                        # Here's the logic to work through the three edge cases.
                        else:
                            print(w, 'in', odd_terms_list)
                            match_flag = False
                            match_term = 'none'
                            match_type = 'none'
                            # Leading space test
                            if w in st_suffix_list:
                                w_prime = ' ' + w
                                if w_prime in sent.text.lower():
                                    match_flag = True
                                    match_term = w
                                    match_type = 'prefix'
                            # Word form test
                            elif w in st_wordforms_dic.keys():
                                print('wordforms test:', w, st_wordforms_dic[w])
                                test_match = False
                                for t in st_wordforms_dic[w]:
                                    if t in sent.text.lower():
                                        test_match = True  # True match = bad news
                                if not test_match:
                                    match_flag = True
                                    match_term = w
                                    match_type = 'word forms'
                            elif w in st_polysemy_dic.keys():
                                print('polysemy text', w, st_polysemy_dic[w])
                                test_match = False
                                w_loc = sent.text.lower().find(w)
                                print(sent.text.lower()[w_loc - 20:w_loc])
                                for pw in st_polysemy_dic[w]:
                                    if pw in sent.text.lower()[w_loc - 20:w_loc]:
                                        print("Polysemy Bad News:", pw, sent.text)
                                        test_match = True
                                if not test_match:
                                    match_flag = True
                                    match_term = w
                                    match_type = 'polysemy'
                        if match_flag:
                            match_count = match_count + 1
                            MatchList.append([i, total_count, match_count, sent.text, w, match_flag, match_term, match_type])
                        else:
                            fail_count = fail_count + 1
                            FailList.append([i, total_count, fail_count, sent.text, w, match_flag, match_term, match_type])
                        print(i, total_count, match_count, fail_count, sent.text, w, match_flag, match_term, match_type)
                        print(ltr, ':', len(sent.tokens), ';', i, '/', len(doc.sentences), '.', w, '/', w, '(', sh, ')',
                              ':', sent.text)
                        out_list.append([ltr, len(sent.tokens), i, len(doc.sentences), w, sh, sent.text])
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

print('Matches:')
for r in MatchList:
    print(r)

print('No Matches:')
for r in FailList:
    print(r)