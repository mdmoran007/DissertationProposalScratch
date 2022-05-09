# A simple file to generate a synonym list using WordNet via NLTK.
# Driven by an LoL
# Expanded to include the Word2Vec WE's as well.

from nltk.corpus import wordnet as wn

import pickle
pfl = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Logs/new_st.pkl'
pfl2 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Logs/ShOut.pkl'

# Build list of terms to be expanded
SynDic = {}
StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
SynDic['employee'] = ['employee', 'workforce', 'work force', 'our people',
                      'personnel', 'associate', 'worker', 'co-worker']
SynDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'lender', 'bondholder']
SynDic['customer'] = ['customer', 'client', 'consumer', 'clientele', 'buyer']
SynDic['supplier'] = ['supplier', 'supply chain', 'supply base', 'business partner']
SynDic['community'] = ['community', 'city', 'town', 'society']
SynDic['environment'] = ['environment', 'sustainability', 'climate']
SynDic['stakeholder'] = ['stakeholder']

# This is the base set of terms that I developed through deep-reading and thesauruses.
print('mark synonyms')
for sg in StakeholderList:
    print('mark', sg, len(SynDic[sg]), SynDic[sg])

print('')

sim_num = 10 # How many similar words to return # arbitrary chaice. Ten is default

# These values are based on the mechanics of how Word2Vec runs in GenSim.
# They allow it to be a shared subroutine even though the calling of ConceptNumberbatch is a bit different
wv_api_list = ['word2vec-google-news-300',
               'glove-wiki-gigaword-300',
               'fasttext-wiki-news-subwords-300',
               'conceptnet-numberbatch-300']
cnnb_loc = '/Users/moranmarkd/gensim-data/numberbatch-en-19-08-300/numberbatch-en-19.08.txt.gz'

# The list of sources for synonyms
s_list = ['wordnet']
s_list = s_list + wv_api_list

ShOut = {} # A dictionary for the output of the different synonmys from different sources

# Builds the dictionary. to contain the output
for ss in s_list: # ss for synonym source
    ShOut[ss] = {} # An out list for each synonym source
    for sg in StakeholderList:
        ShOut[ss][sg] = [] # Stakeholder list per Synonm Source

#for ss in ShOut:
#    print (ss, ShOut[ss]) # This structure is a place to store lists for each Stakeholder group for each synonym source.

# Here the set-up is done and the actual work begins. WordNet is a totally separate beast from the others
print ('wordnet synsets:')
#print ("stakeholder group ['stakeholder terms'] {'synonyms'}")
for i in StakeholderList:
    synonyms = []
#    print ('Stakeholder Group', i)
    for j in SynDic[i]:
#        print('Stakeholder Group:', i, '/ Stakeholder Term:', j)
        for syn in wn.synsets(j, pos=wn.NOUN):
#            print (j, syn)
            for l in syn.lemmas():
                synonyms.append(l.name())
    ShOut['wordnet'][i] = list(set(synonyms))
#    print(i, SynDic[i], set(synonyms))

for sh in StakeholderList:
    print('wordnet', sh, len(ShOut['wordnet'][sh]), ShOut['wordnet'][sh])

# Here begins the code to work through the different WE's in GenSim
#import logging
#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Gensim word2vec models:
from gensim import models
import gensim.downloader as api

# These three have the same format. ConceptNet Numberbatch is a little different deal.
# Will use the same general structure a with WordNet
# What I would like is if I could give a range of scores afterward. Maybe the scores don't matter?

for a in wv_api_list:
    print ('')
    print(a, 'most_similar:')
#    print("stakeholder group ['stakeholder terms'] {'synonyms'}")
    if a == 'conceptnet-numberbatch-300': # Handling that ConceptNet Numberbatch loads differently, but is the same after that.
        wv = models.KeyedVectors.load_word2vec_format(cnnb_loc)
    else: # otherwise, just a standard load
        wv = api.load(a)
    for i in StakeholderList: # list of stakeholder groups
        synonyms = []
        for j in SynDic[i]: # j = List of terms for i list of groups
#            print('api', a, '/ stakeholder group', i, '/ stakeholder term', j)
            if j in list(wv.index_to_key): # Test for term to make sure it is in vocab.
                syns = wv.most_similar(j, topn=sim_num)
                for l in syns:
                    synonyms.append(l[0])
#                print(i, j, syns)
#        print(i, SynDic[i], set(synonyms))
#        MasterSynDic[i].extend(list(set(synonyms)))
        ShOut[a][i] = list(set(synonyms))
#        print (a, i, ShOut[a][i])

#    print('ShOut -', a, ShOut[a])
    for sh in StakeholderList:
        print (a, sh, len(ShOut[a][sh]), ShOut[a][sh])

# Printing Summary reslts.
print('')
for sg in StakeholderList:
    print ('mark', sg, len(SynDic[sg]), SynDic[sg])
for a in s_list:
    for sg in StakeholderList:
        print (a, sg, len(ShOut[a][sg]), ShOut[a][sg])

# Holds the summary results for everything.
new_st = {}
for sg in StakeholderList:
    new_st[sg] = []

for s in s_list:
    for sg in StakeholderList:
        new_st[sg] = new_st[sg] + ShOut[s][sg]

# Get rid of duplicates
for sg in StakeholderList:
    new_st[sg] = list(set(new_st[sg]))

# Print final results.
print()
for sg in StakeholderList:
    print (sg, len(new_st[sg]), new_st[sg])

pf = open(pfl, 'wb')
pickle.dump(new_st, pf)

pf2 = open(pfl2, 'wb')
pickle.dump (ShOut, pf2)




