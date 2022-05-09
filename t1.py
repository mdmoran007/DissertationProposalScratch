SynDic = {}
StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
SynDic['employee'] = ['employee', 'workforce', 'work force', 'our people', 'personnel', 'associate', 'worker', 'co-worker']
SynDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'lender', 'bondholder']
SynDic['customer'] = ['customer', 'client', 'consumer', 'clientele', 'buyer']
SynDic['supplier'] = ['supplier', 'supply chain', 'supply base', 'business partner']
SynDic['community'] = ['community', 'city', 'town', 'society']
SynDic['environment'] = ['environment', 'sustainability', 'climate']
SynDic['stakeholder'] = ['stakeholder']


s_list = ['wordnet',
               'word2vec-google-news-300',
               'glove-wiki-gigaword-300',
               'fasttext-wiki-news-subwords-300',
               'conceptnet-numberbatch-300']

import pickle
base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1'
pfl = base_dir + '/Logs/new_st_10.pkl'
pfl2 = base_dir + '/Logs/ShOut.pkl'

new_st = pickle.load(open(pfl, 'rb'))

print('')
for sg in StakeholderList:
    print (sg, len(new_st[sg]), new_st[sg])


clean_st = {}
for sg in StakeholderList:
    clean_st[sg] = []

# Also need to make lower case, replace underscores with spaces, build arrach
for sg in StakeholderList:
    l1a = new_st[sg] # ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    l2 = SynDic[sg] # ["one", "two", "three", "four", "nine"]
    l1 = []
    for st in l1a:
        st = st.lower().replace('_', ' ')
        l1.append(st)
    s2 = set(l2)
    s1 = set(l1)
    l3 = [x for x in l1 if not x in s2]
    l4 = [x for x in l2 if not x in s1]
    l5 = l3 + l4
    print (l1)
    print (s1)
    print (l2)
    print (s2)
    print (l3)
    print (l4)
    print (l5)
    clean_st[sg] = l5

print('')
for sg in StakeholderList:
    print (sg, len(clean_st[sg]), clean_st[sg])

for sg in StakeholderList:
    for st in clean_st[sg]:
        print (sg, st)

# Now write out two-by-row
import csv
CsvHeader = ['STG', 'STT']
CsvFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/TermList-10a.csv'
f = open(CsvFile, 'w')
writer = csv.writer(f)
writer.writerow(CsvHeader)
for sg in StakeholderList:
    for st in clean_st[sg]:
        tl = [sg, st]
        print(tl)
        writer.writerow(tl)
f.close()

ShOut = pickle.load(open(pfl2, 'rb'))


    #for s in s_list:
        #for sg in StakeholderList:
            #print (r, s, sg, len(ShOut[s][sg]), ShOut[s][sg])
            #if "hamlet" in ShOut[s][sg]:
            #    print ("hamlet in", s, sg)