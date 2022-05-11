# This file will take a supplied list of candidate terms and present ten random examples of each of them.
# It will grab 15 words before and ten after.
# it will write that all to an out file, without including the file names.
# The search logic will be exactly like the code that generated the list (CountTerms.py)

import os
import csv
import random
import re


eval_list = ['staff', 'headcount', 'colleague', 'labor force', 'our people',
            'shareowner', 'creditor', 'bondholder',
            'guest', 'subscriber', # Commented out 'patron' because it was returning all but two as 'patronage'.
            'buyer', 'wholesaler', 'supply chain', 'business partner',
            'village', 'neighborhood', 'municipalities']
wc_list = {}


# Initialise dictionary of lists of all usages.
eval_sents = {}
for t in eval_list:
    eval_sents[t] = [] # Each term will be a list of all sentences where it is used.

# Find all examples and put them in TermSamples
# Lift this code from CountTerms.py as a place to start.
# Can start by just adding a print statement to print from ten words before to five after.


# Randomly select terms and place them in eval_samples
eval_samples = {}
for t in eval_list:
    eval_samples[t] = []

# Find usages of terms and put them into list of eval_sents[t]
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt/'
fnl = os.listdir(BaseLetterDir)
print (fnl) # file name list
for i in range (0, len(eval_list)):
    print (eval_list[i])
    wc = 0
    for fn in fnl: # Recurse through files in a directory
        if fn.lower().endswith('txt'):
            ffn = BaseLetterDir + fn
            f = open(ffn, "r", encoding='latin-1')
            data = f.read()
            words = data.split()
#            print (words)
            for j in range(0, len(words)):
                eval_term = eval_list[i].lower()
                str_len = len(eval_list[i].split(' '))
                if str_len == 4:
                    ltr_txt = words[j-3].lower() + ' ' + words[j-2].lower() + ' ' + words[j-1].lower() + ' ' + words[j].lower()
                elif str_len == 3:
                    ltr_txt = words[j - 2].lower() + ' ' + words[j - 1].lower() + ' ' + words[j].lower()
                elif str_len == 2:
                    ltr_txt = words[j - 1].lower() + ' ' + words[j].lower()
                else:
                    ltr_txt = words[j].lower()
#                    print (eval_term, str_len, ltr_txt)
#                    print (fn, words[j], eval_list[i][1])
                if (re.search('^' + eval_term, ltr_txt) != None):
                    print ('MATCH', eval_term, ltr_txt)
                    wc = wc + 1
                    sample_text = ''
#                    print ('MATCH', fn, ltr_txt, eval_list[i])
                    for k in range(-10, 5):
                        if (j + k + 1 > 0) and (j + k < len(words)):
                            sample_text = sample_text + words[j + k] + ' '
                    print (j, len(words), sample_text)
#                    print('')
                    eval_sents[eval_list[i]].append(sample_text)
    wc_list[eval_list[i]] = wc

# How many of each candidate term?
for t in eval_list:
    print(t, wc_list[t])

# Select ten random sentences for each term.
for t in eval_list:
    used_list = []
    while len(used_list) < 10: # Get ten sentences per term
        j = random.randint(0, len(eval_sents[t]) - 1)
        print (t, len(eval_sents[t]), j)
        if j not in used_list:
            eval_samples[t].append(eval_sents[t][j])
            used_list.append(j)
        else:
            print (j, 'in', used_list)

for t in eval_list:
    for s in eval_samples[t]:
        print(t + ': ' + s)

