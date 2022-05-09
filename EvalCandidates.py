# This file will read in the evaluated candidate terms and do two main things:
#   * Determine which synonym source contained each term
#   * Count how often each term appears in the corpus

# I think I need to re-write the pickle from Nltk-Scratch to capture the original Sources.
# I think maybe I need to just write out a file that I have already made?

# Base Datasets
SynDic = {}
StakeholderList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder', 'environment']
SynDic['employee'] = ['employee', 'workforce', 'work force', 'our people', 'personnel', 'associate', 'worker', 'co-worker']
SynDic['investor'] = ['investor', 'shareholder', 'stockholder', 'financier', 'lender', 'bondholder']
SynDic['customer'] = ['customer', 'client', 'consumer', 'clientele', 'buyer']
SynDic['supplier'] = ['supplier', 'supply chain', 'supply base', 'business partner']
SynDic['community'] = ['community', 'city', 'town', 'society']
SynDic['environment'] = ['environment', 'sustainability', 'climate']
SynDic['stakeholder'] = ['stakeholder']

base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1'

# Load in text file

from csv import reader

cfl = base_dir + '/Out/TermList-10-Edited.csv'
# read csv file as a list of lists
with open(cfl, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)
    for row in list_of_rows:
        print(row)


# Load in Pickle file

import pickle

pfl = base_dir + '/Logs/new_st_10.pkl'
new_st = pickle.load(open(pfl, 'rb'))


print('')
for sg in StakeholderList:
    print (sg, len(new_st[sg]), new_st[sg])
# Recurse through text and pickle. Build list of which source synset or most_similar contains each work in the list.



