# SynList.py ----------------------------------------------------------------------------------------
# A Simple script to find and evaluate synonyms for stakeholder groups in my PhD studies
# Will find synonyms from:
#   - WordNet (via NLTK)
#   - Fasttext (via Gensim Word2Vec)
#   - Glove (via Gensim Word2Vec)
#   - GoogleNews (via Gensim Word2Vec)
#   - ConceptNet (via Gensim Word2Vec)
# Mark Moran, markdm2@illinois.edu
# November 12, 2021
# ---------------------------------------------------------------------------------------------------

import pickle #So I don't have to keep running this...

# Master List of words that need synonyms
StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
wv_SourceList = ['wv_googlenews', 'wv_fasttext', 'wv_glove', 'wv_conceptnet']
other_SourceList = ['mark', 'nltk_wordnet']
SourceList = other_SourceList + wv_SourceList
SynDic = {}
for sh in StakeholderList:
    SynDic[sh] = {}
    for src in SourceList:
        SynDic[sh][src] =[]

print(SynDic)


# ---------------------------------------------------------------------------------------------------


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Gensim word2vec models:
from gensim.models import KeyedVectors
from gensim import models
import gensim.downloader as api


print (' *** Beginning WordNet via NLTK ***')
from nltk.corpus import wordnet
for sh in StakeholderList:
    for syn in wordnet.synsets(sh):
        for l in syn.lemmas():
            syn_tuple = (l.name(),0)
            SynDic[sh]['nltk_wordnet'].append(syn_tuple)
    print (sh, ':', SynDic[sh]['nltk_wordnet'])
print (SynDic)
print (' *** Completing WordNet via NLTK ***')


print (' *** Beginning GoogleNews via Gensim ***')
wv_googlenews = api.load('word2vec-google-news-300')
for sh in StakeholderList:
    syns = wv_googlenews.most_similar(sh)
    print(syns)
    for syn_tuple in syns:
        SynDic[sh]['wv_googlenews'].append(syn_tuple)
    print(sh, ':', SynDic[sh]['wv_googlenews'])
print(SynDic)
print (' *** Completing GoogleNews via Gensim ***')

print (' *** Beginning Glove via Gensim ***')
wv_glove = api.load('glove-wiki-gigaword-300')
for sh in StakeholderList:
    syns = wv_glove.most_similar(sh)
    print(syns)
    for syn_tuple in syns:
        SynDic[sh]['wv_glove'].append(syn_tuple)
    print(sh, ':', SynDic[sh]['wv_glove'])
print(SynDic)
print (' *** Completing Glove via Gensim ***')

print (' *** Beginning ConceptNet via Gensim ***')
wv_conceptnet = models.KeyedVectors.load_word2vec_format('/Users/moranmarkd/gensim-data/numberbatch-en-19-08-300/numberbatch-en-19.08.txt.gz')

for sh in StakeholderList:
    syns = wv_conceptnet.most_similar(sh)
    print(syns)
    for syn_tuple in syns:
        SynDic[sh]['wv_conceptnet'].append(syn_tuple)
    print(sh, ':', SynDic[sh]['wv_conceptnet'])
print(SynDic)
print (' *** Completing ConceptNet via Gensim ***')

print (' *** Beginning FastText via Gensim ***')
wv_fasttext = api.load('fasttext-wiki-news-subwords-300')
for sh in StakeholderList:
    syns = wv_fasttext.most_similar(sh)
    print(syns)
    for syn_tuple in syns:
        SynDic[sh]['wv_fasttext'].append(syn_tuple)
    print(sh, ':', SynDic[sh]['wv_fasttext'])
print(SynDic)
print (' *** Completing FastText via Gensim ***')

print (SynDic)

print (' *** Beginning Mark via Mark ***')
SynDic['employee']['mark'] = [('employee', 0), ('workforce', 0), ('our people', 0), ('personnel', 0), ('associate', 0), ('worker', 0), ('co-worker', 0)]
SynDic['investor']['mark'] = [('investor', 0), ('shareholder', 0), ('stockholder', 0), ('financier', 0), ('lender', 0),('bondholder', 0)]
SynDic['customer']['mark'] = [('customer', 0), ('client', 0), ('consumer', 0), ('clientele', 0), ('buyer', 0)]
SynDic['supplier']['mark'] = [('supplier', 0), ('supply chain', 0), ('supply base', 0), ('business partner', 0)]
SynDic['community']['mark'] = [('community', 0), ('city', 0), ('town', 0), ('society', 0)]
SynDic['stakeholder']['mark'] = [('stakeholder', 0)]
print (' *** Completing Mark via Mark ***')

print (' *** Review Data Structure by Stakeholder')
for sh in StakeholderList:
    print (SynDic[sh])

f = '/Users/moranmarkd/Downloads/SynDic-v3.pkl'
outfile = open (f,'wb')
pickle.dump (SynDic, outfile)
outfile.close()