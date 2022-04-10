# gib.py --------------------------------------------------------------------------------------------------------------
# Removed gibberish characters from text files.
# Meant as a last resort when hand-editing is still missing some invisible character.
# Part of the manual CEO's Letter pipeline.

import os

sample_string_1 = 'résumé'
sample_string_2 = '• This is a journey into ••• sound.'
sample_string_3 = '!@#$%^&*()'

ps_1 = sample_string_3.isascii()
print (ps_1)

string_with_nonASCII = "àa string withé fuünny charactersß."

encoded_string = string_with_nonASCII.encode("ascii", "ignore")
decode_string = encoded_string.decode()

print(decode_string)

# It looks like simple logic like this might do the job.
# I wonder about expanding this to "scrub files" is viable.
scrub_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Letters/09-CL-txt'
scrub_ext = 'zzz'
scrubbed_ext = 'txt'
scrub_list = []
scrubbed_dic = {}
# Set a directory and a list of files.

fnl = os.listdir(scrub_dir)
for fn in fnl:
    if fn.lower().endswith(scrub_ext):
        scrub_list.append(fn)

# Recurse the files.
for ltr in scrub_list:
    full_infile_path = scrub_dir + '/' + ltr

# load it into a string
# Do the encode/decode above
    inputfile = open(full_infile_path, mode='r', encoding='utf-8', errors='ignore')
    text_in = inputfile.read()

    encoded_string = text_in.encode("ascii", "ignore")
    text_out = encoded_string.decode()

    print(text_out)
    scrubbed_dic[ltr] = text_out

# Write new stringS out to a file with .txt extension
for k, v in scrubbed_dic.items():
    out_name = k.split('.')[0] + '.' + scrubbed_ext
    fon = scrub_dir + '/' + out_name
    print (fon)

    fon_h = open(fon, 'w')
    fon_h.write(v)
    fon_h.close()
