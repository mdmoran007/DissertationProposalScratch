# FindStakeholderSentences.py ------------------------------------------------------------------------------
# A simple script to find sentences containing stakeholders in the 15 candidate letters and evaluate with BERT
# The steps:
#   - Load up base lists
#   - Load files into strings
#   - Search files for my strings and return those sentences
#   - Write those sentences out to a csv that is picked up by BertSemanticSentenceSimilarity.py in the M3 Dissertation PyCharm project
# That files searches through and masks the base term in a way that does not alter any sentence lengths.
#
# Mark Moran, markdm2@illinois.edu
# November 15, 2021
# --------------------------------------------------------------------------------------------------
# February 2022
# Now I need to expand this to simply pull every file from a directory for Paper 1,
# instead of a discrete list of files. That is not too hard.
# Copied from cfg.py until I get that working
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
# End copied section


# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Letters/09-CL-txt/'
SampleLettersList = ['XEL-CL1-FY2007.txt', 'MRK-CL1-FY2008.txt', 'CSCO-CL1-FY2008.txt', 'ABC-CL2-FY2006.txt', 'CVS-CL1-FY2006.txt',
                     'BEN-CL1-FY2013.txt', 'SWK-CL1-FY2012.txt', 'NUE-CL1-FY2014.txt', 'ETFC-CL1-FY2011.txt', 'DIS-CL1-FY2012.txt',
                     'HAL-CL1-FY2017.txt', 'COST-CL1-FY2019.txt', 'D-CL1-FY2019.txt', 'COST-CL1-FY2016.txt', 'EQR-CL1-FY2016.txt']
# Each row will be letter, sentence id, total letter sentence count, base stakeholder, stakeholder term, and sentence text.
OutList = [['Letter_File_Name', 'Sentence_Token_Count', 'Sent_ID','Total_Letter_Sentences', 'Specific_Term', 'Stakeholder_Group', 'Sentence_Text']]

# Load Letters into strings
import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')

# Load up Stanza and turn documents into sentences.
for ltr in SampleLettersList:
    full_infile_path = BaseLetterDir + ltr

    inputfile = open(full_infile_path, mode='r', encoding='utf-8', errors='ignore')
    text1 = inputfile.read()
#    print (text1)
    doc = nlp(text1)
    print('--------------------', ltr, '-----------------------')
    for i, sent in enumerate(doc.sentences):
#        print (ltr, i, len(sent.tokens), sent.text)
        for sh in ShCatList:
            for w in ShCatBaseListDic[sh]:
                if w in (sent.text).lower() and len (sent.words) > 9 :
                    # These lines catch the cases where the plural and singular terms end differently.
                    # I should really re-write the whole section to move to detecting lemmas.
                    # More processor-intensive, but more reliable.
                    # That said, I can capture these with nothing in the lists in the next file and not write them.
                    if w == 'communities':
                        w_prime = 'community'
                    elif w == 'cities':
                        w_prime = 'city'
                    elif w == 'agencies':
                        w_prime = 'agency'
                    else:
                        w_prime = w
                    print (ltr, ':', len(sent.tokens), ';', i, '/', len(doc.sentences), '.', w_prime, '(', sh, ')', ':', sent.text)
                    OutList.append([ltr, len(sent.tokens), i, len(doc.sentences), w_prime, sh, sent.text])

print (OutList)

# Write OutList to a file
OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/scratch/sh1-v5.csv'
import csv
with open(OutFile, "w") as f:
    wr = csv.writer(f)
    wr.writerows(OutList)


# This picks up in the M3 - Dissertation project
# I made some manual changes in sh2 to get it ready (calculated position)...I could bring that in here if I wanted to.