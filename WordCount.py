# A simple file to count words per file
import os
import csv

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/'
LogFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/CleanLog.txt'
LettersList = []
OutList = [['Letter_File_Name', 'File_Word_Count']]
OutList2 = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Investor', 'Employee', 'Customer', 'Community', 'Supplier', 'Stakeholder']] # Salutation
OutList3 = [['LetterFileName', 'Ticker', 'Fiscal_Year', 'Investor', 'Employee', 'Customer', 'Community', 'Supplier', 'Stakeholder']] # Valediction
fnl = os.listdir(BaseLetterDir)

# A very simple re-usable function for testing for a string in a substring.
def fxnCheckForStakeholder(text_range, stakeholder_text_list):
# A function that takes the following inputs:
#   - text_range: string to be searched
#   - stakeholder_text: string to search for
# and returns the following outputs:
#   - find_state: returns 1 if yes, 0 if no
    print (stakeholder_text_list)
    chkval = 0
    for sh in stakeholder_text_list:
        print (sh)
        if sh.lower() in text_range.lower():
            chkval = 1
        print (chkval)
    return chkval

# 'Investor', 'Employee', 'Customer', 'Community', 'Supplier', 'Stakeholder'
sh_lol = [['investor', 'shareholder', 'stockholder'], ['employee', 'people', 'team'], ['customer'], ['communit'], ['supplier'], ['stakeholder']]
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)
        ffn = BaseLetterDir + fn
        f = open(ffn, "r")
        data = f.read()
        words = data.split()
#        print (fn, len(words))
# First Outlist: Word Count per letter
        OutList.append([fn, len(words)])
#        print (words[0:20])
# Second OutList: saluation stakeholder count:
        or2 = [fn, fn.split('-')[0], fn.split('-')[2][2:6]]
        print (data[0:100])
        for sh_list in sh_lol:
            or2.append(fxnCheckForStakeholder(data[0:100], sh_list))
        OutList2.append(or2)
# Third OutList: valediction stakeholder count:
        or3 = [fn, fn.split('-')[0], fn.split('-')[2][2:6]]
        print (data[-200:])
        for sh_list in sh_lol:
            or3.append(fxnCheckForStakeholder(data[-200:], sh_list))
        OutList3.append(or3)

print (OutList2)
print (OutList3)

#OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/wrd_cnt-v1.csv'
#with open(OutFile, "w") as f:
#    wr = csv.writer(f)
#   wr.writerows(OutList)

OutFile2 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/salutation_count-v2.csv'
with open(OutFile2, "w") as f:
    wr2 = csv.writer(f)
    wr2.writerows(OutList2)

OutFile3 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/valediction_count-v1.csv'
with open(OutFile3, "w") as f:
    wr3 = csv.writer(f)
    wr3.writerows(OutList3)

#test_string = 'Stakeholder communities investors shareholder customer suppliers employees. ' \
#              'Now is the time for all good people to come to the aid of their country. ' \
#              'The quick brown fox jumped over the lazy dog. ' \
#              'Stakeholder community investors stockholder, shareholder customer suppliers employees.'

# A couple of demo statements.
#print (fxnCheckForStakeholder(test_string[0:100], ["stockholder"]))
#print (fxnCheckForStakeholder(test_string[-100:], ["stockholder"]))
