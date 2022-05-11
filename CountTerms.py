import pickle
import os
from csv import reader
import csv


StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt/'
LettersList = []
#OutList = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Specific_Term', 'Stakeholder_Group']] # Salutation
fnl = os.listdir(BaseLetterDir)
print (fnl)


base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1'
pfl = base_dir + '/Logs/new_st_10.pkl'
pfl2 = base_dir + '/Logs/ShOut.pkl'
cfl = base_dir + '/Out/TermList-10-Edited.csv'
efl = base_dir + '/Out/TermList-10-Full_v2.csv'

new_st = pickle.load(open(pfl, 'rb'))
print (new_st)
print('')

ShOut = pickle.load(open(pfl2, 'rb'))
print (ShOut)

for sg in StakeholderList:
    print (sg, len(new_st[sg]), new_st[sg])

with open (cfl, 'r') as cf:
    csv_reader = reader(cf)
    eval_list = list(csv_reader)

s_list = ['wordnet',
          'word2vec-google-news-300',
          'glove-wiki-gigaword-300',
          'fasttext-wiki-news-subwords-300',
          'conceptnet-numberbatch-300']

ef = open(efl, 'w')
writer = csv.writer(ef)

print (eval_list[0])
new_cols = ['WordNet', 'Word2Vec', 'GloVe', 'FastText', 'ConceptNet-Numberbatch', 'Count']
eval_list[0] = eval_list[0] + new_cols
writer.writerow(eval_list[0])
print (eval_list)
for i in range (0, len(eval_list)):
    print (eval_list[i])
    if i == 0:
        eval_list[i] = eval_list[i] + new_cols
    else:
        if eval_list[i][1].lower().replace(' ', '_') in ShOut['wordnet'][eval_list[i][0]]:
            eval_list[i].append(1)
        else:
            eval_list[i].append(0)
        if eval_list[i][1].lower().replace(' ', '_') in ShOut['word2vec-google-news-300'][eval_list[i][0]]:
            eval_list[i].append(1)
        else:
            eval_list[i].append(0)
        if eval_list[i][1].lower().replace(' ', '_') in ShOut['glove-wiki-gigaword-300'][eval_list[i][0]]:
            eval_list[i].append(1)
        else:
            eval_list[i].append(0)
        if eval_list[i][1].lower().replace(' ', '_') in ShOut['fasttext-wiki-news-subwords-300'][eval_list[i][0]]:
            eval_list[i].append(1)
        else:
            eval_list[i].append(0)
        if eval_list[i][1].lower().replace(' ', '_') in ShOut['conceptnet-numberbatch-300'][eval_list[i][0]]:
            eval_list[i].append(1)
        else:
            eval_list[i].append(0)
        # Now the logic to count the term in the presence of all of the files and append that.
        wc = 0
        for fn in fnl: # Recurse through files in a directory
            if fn.lower().endswith('txt'):
                LettersList.append(fn)
                ffn = BaseLetterDir + fn
                f = open(ffn, "r", encoding='latin-1')
                data = f.read()
                words = data.split()
#                print (words)
                for j in range(0, len(words)):
                    eval_term = eval_list[i][1].lower()
                    str_len = len(eval_list[i][1].split(' '))
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
                    if eval_term i== ltr_txt:
                        wc = wc + 1
                        print ('MATCH', ltr_txt, eval_list[i][1])
        eval_list[i].append(wc)
        print (i, eval_list[i])
        writer.writerow(eval_list[i])

print (eval_list)

ef.close()


