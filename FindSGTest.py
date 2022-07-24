import stanza

# Variables brought strait from v1.2
#ShCatList = ['employee', 'investor', 'customer', 'supplier', 'community', 'stakeholder',
#             'environment']  # Added environment with v1.2
# This is re-built and I should probably move it over.
ShCatBaseListDic = {'employee': ['employee', 'workforce', 'work force', 'personnel', 'our people', 'associate',
                                 'worker',
                                 'staff', 'headcount', 'colleague'],
                    'investor': ['investor', 'shareholder', 'stockholder', 'financier', 'bondholder', 'lender',
                                 'shareowner', 'creditor'],
                    'customer': ['customer', 'client', 'clientele', 'consumer', 'buyer',
                                 'guest', 'subscriber', 'policyholder'],
                    'supplier': ['supplier', 'supply base', 'business partner'],
                    'community': ['community', 'city', 'communities', 'cities', 'town', 'society', 'societies',
                                  'neighborhood'],
                    'stakeholder': ['stakeholder'],
                    'environment': ['environment', 'climate', 'sustainability']}  # Added back in with v1.2
ShCatList = list(ShCatBaseListDic.keys())  # This is also a re-work. More Pythonic, I think.
print (ShCatList)
# End var's brought straight from v1.2
MatchList = []
FailList = []
# New var's required for enhanced match: -------------------------------------------------------------------------------
st_suffix_list = ['city']  # These stakeholder terms can also be suffixes and require a space before them to count.
st_wordforms_dic = {'associate': ['associated', 'associating'], 'staff': ['staffed', 'staffing']}
st_polysemy_dic = {'environment': ['econom', 'financ', 'business', 'invest', 'legal', 'interest', 'work', 'politic'],
                   'climate': ['econom', 'financ', 'business', 'invest', 'legal', 'interest', 'work', 'politic']}

# Assemble all of the odd terms into one list to test later. If new categories were added, this would need to change.
# I need to move over these lines.
odd_terms_list = st_suffix_list + list(st_wordforms_dic.keys()) + list(st_polysemy_dic.keys())
print(odd_terms_list) # Make sure it looks right.
# A few lines to test that the structures are correct...prolly don't need these in the new file
for k in st_wordforms_dic.keys():
    for wf in st_wordforms_dic[k]:
        print(k, wf)
for k in st_polysemy_dic.keys():
    for p in st_polysemy_dic[k]:
        print(k, p)
# End new var's --------------------------------------------------------------------------------------------------------

# Some test sentences -- Not to be ported
text1 = 'We have staffed up for the new business climate. ' \
        'Our staff loves the environment and all of the things associated with it. ' \
        'Our associates prefer living in the city.' \
        'Our people have the innate capacity for greatness.' \
        'Climate change is real, no matter what the political environment tells us.' \
        'Dear shareholders, we gave you all of our money again this year because you are our favorites.' \
        'We fired all of our employees and shat on the environment.' \
        'The city has employees and bondholders who hate the business freaking climate.' \
        'Dear shareowners, you will be proud of your company: we have screwed our employees and our neighborhoods ' \
        'while pillaging the environment.'

print(text1)

# Load up Stanza and turn documents into sentences.
stanza.download('en')
nlp = stanza.Pipeline('en')

doc = nlp(text1)

match_count = 0
fail_count = 0
total_count = 0
for i, sent in enumerate(doc.sentences):
    print(sent.text)
    for sh in ShCatList:  # sh is the stakeholder groups
        for w in ShCatBaseListDic[sh]:  # w is the words we are looking for, the stakeholder terms
            if w in sent.text.lower() and len(sent.words) >= 6:  # Changed from nine previously. Basic gateway test
            # The above tells us that there is a match, so if it's not an edge case, it's simple.
                total_count = total_count + 1
                match_flag = False
                match_term = ''
                match_term = 'none'
                if w not in odd_terms_list:
                    print(w, 'not in', odd_terms_list)
                    match_flag = True
                    match_term = w
                    match_type = 'basic'
                # Here's the logic to work through the three edge cases.
                else:
                    print (w, 'in', odd_terms_list)
                    match_flag = False
                    match_term = 'none'
                    match_type = 'none'
                    # Leading space test
                    if w in st_suffix_list:
                        w_prime = ' ' + w
                        if w_prime in sent.text.lower():
                            match_flag = True
                            match_term = w
                            match_type = 'prefix'
                    # Word form test
                    elif w in st_wordforms_dic.keys():
                        print('wordforms test:', w, st_wordforms_dic[w])
                        test_match = False
                        for t in st_wordforms_dic[w]:
                            if t in sent.text.lower():
                                test_match = True  # True match = bad news
                        if not test_match:
                            match_flag = True
                            match_term = w
                            match_type = 'word forms'
                    elif w in st_polysemy_dic.keys():
                        print ('polysemy text', w, st_polysemy_dic[w])
                        test_match = False
                        w_loc = sent.text.lower().find(w)
                        print(sent.text.lower()[w_loc-20:w_loc])
                        for pw in st_polysemy_dic[w]:
                            if pw in sent.text.lower()[w_loc-20:w_loc]:
                                print("Polysemy Bad News:", pw, sent.text)
                                test_match = True
                        if not test_match:
                            match_flag = True
                            match_term = w
                            match_type = 'polysemy'
                if match_flag:
                    match_count = match_count + 1
#                    MatchList.append([i, total_count, match_count, sent.text, w, match_flag, match_term, match_type])
                else:
                    fail_count = fail_count + 1
#                    FailList.append([i, total_count, fail_count, sent.text, w, match_flag, match_term, match_type])
                print (i, total_count, match_count, fail_count, sent.text, w, match_flag, match_term, match_type)
# End logic that drives matching ---------------------------------------------------------------------------------------
print('Matches:')
for r in MatchList:
    print(r)

print('No Matches:')
for r in FailList:
    print(r)
