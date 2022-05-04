# A simple file to generate a synonym list using WordNet via NLTK.
# Driven by an LoL
# Expanded to include the Word2Vec WE's as well.

from nltk.corpus import wordnet as wn

SynDic = {}

StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
SynDic['employee'] = ['employee', 'workforce', 'work force', 'our people', 'personnel', 'associate', 'worker', 'co-worker']
SynDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'lender', 'bondholder']
SynDic['customer'] = ['customer', 'client', 'consumer', 'clientele', 'buyer']
SynDic['supplier'] = ['supplier', 'supply chain', 'supply base', 'business partner']
SynDic['community'] = ['community', 'city', 'town', 'society']
SynDic['environment'] = ['environment', 'sustainability', 'climate']
SynDic['stakeholder'] = ['stakeholder']

MasterSynDic = SynDic

sim_num = 10 # How many similar words to return

print ('wordnet synsets:')
print ("stakeholder group ['stakeholder terms'] {'synonyms'}")
for i in StakeholderList:
    synonyms = []
#    print ('Stakeholder Group', i)
    for j in SynDic[i]:
#        print('Stakeholder Group:', i, '/ Stakeholder Term:', j)
        for syn in wn.synsets(j, pos=wn.NOUN):
#            print (j, syn)
            for l in syn.lemmas():
                synonyms.append(l.name())

    print(i, SynDic[i], set(synonyms))
    MasterSynDic[i].extend(list(set(synonyms)))

print ("MSD")
for s in StakeholderList:
    MasterSynDic[s] = list(set(MasterSynDic[s]))
    print (s, len(MasterSynDic[s]), MasterSynDic[s])

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Gensim word2vec models:
from gensim import models
import gensim.downloader as api

# These three have the same format. ConceptNet Numberbatch is a little different deal.
# Will use the same general structure a with WordNet
# What I would like is if I could give a range of scores afterward. Maybe the scores don't matter?
wv_api_list = ['word2vec-google-news-300', 'glove-wiki-gigaword-300', 'fasttext-wiki-news-subwords-300', 'conceptnet-numberbatch-300']
cnnb_loc = '/Users/moranmarkd/gensim-data/numberbatch-en-19-08-300/numberbatch-en-19.08.txt.gz'

for a in wv_api_list:
    print(a, 'most_similar:')
    print("stakeholder group ['stakeholder terms'] {'synonyms'}")
    if a == 'conceptnet-numberbatch-300': # Handling that ConceptNet Numberbatch loads differently, but is the same after that.
        wv = models.KeyedVectors.load_word2vec_format(cnnb_loc)
    else:
        wv = api.load(a)
    for i in StakeholderList:
        synonyms = []
        for j in SynDic[i]:
            if j in list(wv.index_to_key): # Test for term to make sure it is in vocab. Different WE's handle OOV differently
                syns = wv.most_similar(j, topn=sim_num)
                for l in syns:
                    synonyms.append(l[0])
            print(syns)
        print(i, SynDic[i], set(synonyms))
        MasterSynDic[i].extend(list(set(synonyms)))
        print('MSD:', s, len(MasterSynDic[s]), MasterSynDic[s])
    for s in StakeholderList:
        MasterSynDic[s] = list(set(MasterSynDic[s]))
        print(s, len(MasterSynDic[s]), MasterSynDic[s])

#print (MasterSynDic)
print ('MSD Final:')
for s in StakeholderList:
    MasterSynDic[s] = list(set(MasterSynDic[s]))
    print (s, len(MasterSynDic[s]), MasterSynDic[s])
