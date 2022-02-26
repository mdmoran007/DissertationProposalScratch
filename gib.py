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