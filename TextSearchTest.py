# A simple test script to look for text within a directory. Need to integrate into Nltk-Scratch.py
# Could incorporate wordnet output into here to get something working for Nltk-Scratch.py

# A simple file to generate a synonym list using WordNet via NLTK.
# Driven by an LoL
# Expanded to include the Word2Vec WE's as well.

from nltk.corpus import wordnet as wn

# Build list of terms to be expanded
SynDic = {}
StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
SynDic['employee'] = ['employee', 'workforce', 'work force', 'our people', 'personnel', 'associate', 'worker', 'co-worker']
SynDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'lender', 'bondholder']
SynDic['customer'] = ['customer', 'client', 'consumer', 'clientele', 'buyer']
SynDic['supplier'] = ['supplier', 'supply chain', 'supply base', 'business partner']
SynDic['community'] = ['community', 'city', 'town', 'society']
SynDic['environment'] = ['environment', 'sustainability', 'climate']
SynDic['stakeholder'] = ['stakeholder']

# This is the base set of terms that I developed through deep-reading and thesauruses.
print( 'mark synonyms')
for sg in StakeholderList:
    print ('mark', sg, len(SynDic[sg]), SynDic[sg] )

print ('')

sim_num = 10 # How many similar words to return # arbitrary chaice. Ten is default

# These values are based on the mechanics of how Word2Vec runs in GenSim.
# They allow it to be a shared subroutine even though the calling of ConceptNumberbatch is a bit different
wv_api_list = ['word2vec-google-news-300', 'glove-wiki-gigaword-300', 'fasttext-wiki-news-subwords-300', 'conceptnet-numberbatch-300']
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

# End the code that I brough straight over and begin experimentation ---------------------------------------------------
# These next few are just moved up...no changes
from nltk.corpus import words
import os
LettersList = []
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt/'
fnl = os.listdir(BaseLetterDir)
wct = 0 # word count total
# End moved up

ShDiff = {} # Initializing the array to hold the new terms that we want to find
for sg in StakeholderList:
    ShDiff[sg] = []

ShNewCount = {} # Dictionary to hold new terms and their final count.
for sg in StakeholderList:
    ShNewCount[sg] = {}

import pickle
base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1'
pfl = base_dir + '/Logs/out1.pkl'

# First I want to make sure I am just testing new terms, not the existing terms. Want to find a difference in the list.
# Need to take what is in WordNet that is not in SynDic.
s_ct = 0 # stakeholder count (was gct)
g_ct = 0 # stakeholder group count (was tct)
t_ct = 0 # stakehoder term count (was occ)


# This code takes the lists, makes them all lower case, gets rid of duplication, and removes the original SynDic terms so we are really looking at new terms
for sg in StakeholderList:
    l1a = ShOut['wordnet'][sg]
    l1 = []
    for st in l1a:
        st = st.lower().replace('_', ' ')
#        st = st.replace('_', ' ')
        l1.append(st)
    l2 = SynDic[sg]
    s2 = set (l2)
    l3 = [x for x in l1 if not x in s2]
    print ('wordnet', sg, l1)
    print ('SynDic', sg, l2)
    print ('diff', sg, l3)
    print ('')
    ShDiff[sg] = l3

# Start the code to search and tabulate with a prepped set of terms
for sg in StakeholderList:
    for s in ShDiff[sg]:
        print (sg, s, s.lower() in words.words()) # Test if this is a valid word based on NLTK
        for fn in fnl:
            if fn.lower().endswith('txt'):
                LettersList.append(fn)
                ffn = BaseLetterDir + fn
                f = open(ffn, "r", encoding='latin-1')
                data = f.read()
                data = data.lower()
                #        data = data_temp.encode("ascii", "ignore")
                t_ct = data.count(s)
                if t_ct > 0:
                    g_ct = g_ct + t_ct
                    s_ct = s_ct + t_ct
#                    print(fn, fn.split('-')[0], fn.split('-')[2][2:6], s_ct, g_ct, t_ct, sg, s.lower() in words.words(), s)
        ShNewCount[sg][s] = g_ct
#        print (sg, ShNewCount[sg])
#        print (sg, s, g_ct)
        g_ct = 0 # re-set counter per term

# print (ShNewCount)
for sg in StakeholderList:
    print (sg)
    for st in ShNewCount[sg].keys():
        print ('\t', st, ShNewCount[sg][st])

# open a file, where you ant to store the data
p_f = open(pfl, 'wb')

# dump information to that file
pickle.dump(ShNewCount, p_f)

# close the file
p_f.close()

p_f2 = open(pfl, 'rb') # read binary because write binary (no encoding scheme)
# If this works, I add the pickle logic to the Nltk-Scratch file, and let it run.
foo = pickle.load(p_f2)
print (foo)
