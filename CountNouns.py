import stanza
from datetime import datetime
import os
import csv

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
# upos tags can be found here: https://universaldependencies.org/u/pos/
# NOUN, PRONOUN, PROPN are the three categories.
upos_list = ['NOUN', 'PRON', 'PROPN']
ShCatBaseListDic = {}  # Holds just the base ones I identified
ShCatBaseListDic['employee'] = ['employee', 'workforce']
upos_dic = {}
for u in upos_list:
    upos_dic[u] = 0

BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt/'
out_header = ['FileName', 'NOUN', 'PROPN', 'PRON']
out_file = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/Noun_count.csv'

LettersList = []
fnl = os.listdir(BaseLetterDir)
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)

out_list = []
out_header = ['FileName', 'Key', 'NOUN', 'PROPN', 'PRON']
if not os.path.exists(out_file):
    fo = open(out_file, "w")
    fo_csv = csv.writer(fo)
    fo_csv.writerow(out_header)
    fo.close()

j = 0
for ltr in LettersList:
    Key = ltr.split('-')[0] + '-' + ltr.split('-')[2][2:6]
    for u in upos_list:
        upos_dic[u] = 0
    j = j + 1
    fip = BaseLetterDir + ltr
    inputfile = open(fip, mode='r', encoding='latin1', errors='ignore')
    text1 = inputfile.read()
    print(j, datetime.now(), ltr) # Moving this forward to improve de-bug. Likely just puking on gibberish characters.
    doc = nlp(text1)
    # doc = nlp('Barack Obama was born in Hawaii. I want a sandwich. The automobile is broken. She is taller than me.')
    for sent in doc.sentences:
        for word in sent.words:
#            print (word.text, word.upos)
            if word.pos in upos_list:
                upos_dic[word.pos] = upos_dic[word.pos] + 1
    print (ltr, Key, upos_dic['NOUN'], upos_dic['PROPN'], upos_dic['PRON'])
    out_list.append([ltr, Key, upos_dic['NOUN'], upos_dic['PROPN'], upos_dic['PRON']])
    fo = open(out_file, "a")
    fo_csv = csv.writer(fo)
    fo_csv.writerows(out_list)
    fo.close()
    out_list = []

#    print (datetime.now())