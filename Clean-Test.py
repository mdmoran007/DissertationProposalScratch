
# A simple file to sort through what's gonna choke Stanza.
import os

# The letters to be searched
BaseLetterDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/'
LogFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/CleanLog.txt'
LettersList = []
fnl = os.listdir(BaseLetterDir)
for fn in fnl:
    if fn.lower().endswith('txt'):
        LettersList.append(fn)

# Load Letters into strings
import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')


ft = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Letters/09-CL-txt/NSC-CL1-FY2016.txt'
inputfile = open(ft, mode='r', encoding='utf-8', errors='ignore')
text1 = inputfile.read()
print(text1)
doc = nlp(text1)


# Load up Stanza and turn documents into sentences.
j = 0
for ltr in LettersList:
    j = j + 1
    full_infile_path = BaseLetterDir + ltr

    inputfile = open(full_infile_path, mode='r', encoding='utf-8', errors='ignore')
    text1 = inputfile.read()
#    print (text1)
    print(j, ltr)
    doc = nlp(text1)
