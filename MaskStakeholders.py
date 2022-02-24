from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

# Two lists of sentences
sentences1 = ['The cat sits outside',
             'A man is playing guitar',
             'The new movie is awesome']

sentences2 = ['The dog plays in the garden',
              'A woman watches TV',
              'The new movie is so great']

#Compute embedding for both lists
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
embeddings2 = model.encode(sentences2, convert_to_tensor=True)

#Compute cosine-similarits
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

#Output the pairs with their score
for i in range(len(sentences1)):
    print("{} \t\t {} \t\t Score: {:.4f}".format(sentences1[i], sentences2[i], cosine_scores[i][i]))

# StakeholderEval.py ------------------------------------------------------------------------------
# A simple script to evaluate how the candidate terms fit in the sentences found in the sample letters.
# The steps:
#   - Load list
#   - Load files into strings
#   - Search files for my strings and return those sentences
#
#
# Mark Moran, markdm2@illinois.edu
# November 15, 2021
# --------------------------------------------------------------------------------------------------

# Taken EXACTLY from other StakeholderScan.py ------------------------------------------------------
# Classes of stakeholders currently evaluated
ShCatList = ['employee', 'investor', 'customer', 'supplier', 'society', 'community', 'dealer',
             'stakeholder', 'environment', 'regulator', 'competitor']
ShList = ['e', 'i', 'c', 'u', 'o', 'm', 'd', 't', 'n', 'r', 'p']
MaskDic = {}
# Efficient way to merge above two lists into dictionaries.
for key in ShCatList:
   for value in ShList:
      MaskDic[key] = value
      ShList.remove(value)
      break
print (MaskDic)

ShCatBaseListDic = {}  # Holds just the base ones I identified
ShCatBaseListDic['employee'] = ['employee', 'workforce']
ShCatBaseListDic['investor'] = ['investor', 'shareholder', 'stockholder']
ShCatBaseListDic['customer'] = ['customer', 'client']
ShCatBaseListDic['supplier'] = ['supplier', 'supply base']
ShCatBaseListDic['community'] = ['community', 'city', 'communities', 'cities']
ShCatBaseListDic['society'] = ['society']
ShCatBaseListDic['dealer'] = ['dealer', 'distributor', 'wholesaler', 'retailer', 'channel']
ShCatBaseListDic['stakeholder'] = ['stakeholder', 'partner']
ShCatBaseListDic['environment'] = ['environment', 'climate']
ShCatBaseListDic['regulator'] = ['regulator', 'agency', 'agencies']
ShCatBaseListDic['competitor'] = ['competitor', 'competition']

ShCatListDic = {}  # Holds all the proposed synonyms from stakeholders.
ShCatListDic['employee'] = ['employee', 'workforce', 'worker', 'coworker', 'staffer',
                            'ex-employee', 'employer', 'employee-employer', 'customer', 'contractor',
                            'pension', 'stock taker', 'organization man', 'servants quarters', 'take home vehicle',
                            'employed person', 'serving master']
ShCatListDic['investor'] = ['investor', 'shareholder', 'stockholder', 'equity',
                            'private equity', 'investee', 'entrepreneur', 'investment', 'sentiment',
                            'confidence', 'interest', 'worries']
ShCatListDic['customer'] = ['customer', 'client']
ShCatListDic['supplier'] = ['supplier', 'supply chain', 'importer', 'maker',
                            'manufacturer', 'reseller', 'component']
ShCatListDic['community'] = ['community', 'city', 'district',
                             'area',
                             'organization', 'neighborhood',
                             'system']
ShCatListDic['society'] = ['society', 'club', 'guild', 'gild', 'lodge', 'order', 'company', 'fellowship',
                           'body politic',
                           'culture', 'institute']
ShCatListDic['dealer'] = ['dealer', 'distribution channel', 'distributor', 'wholesaler', 'trader', 'bargainer',
                          'monger', 'principal', 'dealership', 'salesman', 'non-dealer', 'broker']
ShCatListDic['stakeholder'] = ['stakeholder', 'partner', 'investor', 'shareholder', 'stockholder', 'creditor',
                               'funder', 'roundtable']
ShCatListDic['environment'] = ['environment', 'environ', 'surrounding', 'climate',
                               'development', 'ecology', 'districts']
ShCatListDic['regulator'] = ['regulator', 'agency', 'watchdog', 'legislator']
ShCatListDic['competitor'] = ['competitor', 'competition', 'rival', 'challenger', 'contender', 'adversary']
# End section taken from StakeholderScan.py -------------------------------------------------------


# Load file into a list of lists
InFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/scratch/sh1-v5.csv'
InFileColList = ['Stakeholder_Group', 'Specific_Term', 'Sentence_Text']
import pandas as pd
sentence_df = pd.read_csv(InFile, usecols= InFileColList)
print (sentence_df)

for i, row in sentence_df.iterrows():
#    print (i, row['Stakeholder'], row['Term'], row['Sentence_Text'])
    sent_split = row['Sentence_Text'].split()
#    print (sent_split)
    for w in sent_split:
        if row['Specific_Term'] in w.lower():
            print (i, row['Specific_Term'], w.lower())


import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')
text1 = "We are nothing without our world-class employees, dealers, dealer's staff, and wholesalers."
doc = nlp(text1)
print (doc.text)
for s in doc.sentences:
    for w in s.words:
        print (w.feats, w.id, w.text, w.lemma, w.upos)

import inflect
p = inflect.engine()

print (p.plural('equity'))

OutList = []

# Walk through sentences_df (loop above that does that)
# Find where word where the term matches (w.lemma) and verify w.upos
# replace that word with some unique string like [STAKEHOLDER] or [STAKEHOLDERS] depending on whether feats has sing or plur
# Actually, replace with a string that is the same length as what we are removing and indicate whether it is singular pr plural in string.
#   - Make it all asterisks,
#   - but make the third character something for the stakeholder class and
#   - and make the fourth character s for singular or p for plural.
# With goofy sentence, walk through list of candidate terms,
#   - and put the singular or plural and score it with bert sentences like above,
#   - comparing to base stakeholder term.
# I'll need to make this two passes - one identifying any candidates, and the other doing the replacements and scoring.

# Write result to a LoL to write out to a file. Each record: Stakeholder, Candidate, Sentence, score compared to base stakholder term.

for i, row in sentence_df.iterrows():
    doc = nlp(row['Sentence_Text'])

    print(doc.text)
    for s in doc.sentences:
        s_prime = s.text
        s_offsetList = []
        s_textList = []
        for w in s.words:
#            print(w.feats, w.id, w.text, w.lemma, w.upos, w.start_char, w.end_char)
            if w.lemma == row['Specific_Term'] and w.upos == 'NOUN':
                print ('MATCH:', w.lemma, row['Specific_Term'], w.text, len(w.text), w.feats, w.start_char, w.end_char)
                # Test for singular vs. plural
                wfList = w.feats.split('|')
                for f in wfList:
                    if f.startswith('Number'):
                        if f.endswith('Plur'):
                            f_bit = 'p'
                        else:
                            f_bit = 's'
                print (wfList)
                i=0
                for i in range (0,len(w.text)):
                    if i == 0:
                        t1 = '['
                    elif i == 2:
                        t1 = t1 + MaskDic[row['Stakeholder_Group']]
                    elif i == 3:
                        t1 = t1 + f_bit
                    elif i == len(w.text)-1:
                        t1 = t1 + ']'
                        s_offsetList.append(w.start_char)
                        s_textList.append(t1)
                        print('Mask:', w.text, len(w.text), '.', t1, len(t1))
                    else:
                        t1 = t1 + '*'
        print (s_offsetList, s_textList)
# Just moved this section out one level.
    for i,j in enumerate(s_offsetList):
        s_prime2 = s_prime[0:j] + s_textList[i] + s_prime[j+len(s_textList[i]):]
        s_prime = s_prime2
    print (s_prime)

    print ('---------------------------------------------------------')
    OutList.append(s_prime)
# End move
print (OutList)
OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/scratch/sh3-v6.txt'
import csv
f = open(OutFile, "w")
for el in OutList:
    f.write(el + '\n')


