# THis is a guide file for implementing some simple checksum logic to make sure I am able to capture the files as I go.
# There are two main elements: reading in and incrementing a log file
# Appending to a csv file

# At the beginning of the process, see if the log file exists.
# If so, laod its contents into a list to be appended.
# If not, create an empty file.
# Now it's just adding to the file with a file name when the search is done.

# At the beginning of the process, see if the outfile exists.
# If it does, do nothing.
# If it does not, write the header.
# Now it's just adding the statements to the csv with a writerows statement.

import csv
import os

base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1'
log_file = base_dir + '/Out/log.txt'
out_file = base_dir + '/Out/temp.csv'
out_header = ['1', 'Two', 'III']


# See if log file exist. If it does, load its cotent into a list. If not, create a new empty one.
if os.path.exists(log_file):
    print ("log file exists")
    f1 = open(log_file, 'r')
    cl = f1.readlines()
    f1.close()
    f1 = open(log_file, 'a')
    print (cl)

else:
    f1 = open(log_file, 'w')

f1.write("This is a test")
f1.write('\n')
f1.close()

# See if out_file exists. If it does, open in append mode. Else open new one.
if os.path.exists(out_file):
    print("out file exists")
    f2 = open(out_file, 'a')


else:
    f2 = open(out_file, 'w')
    f2_out = csv.writer(f2)
    f2_out.writerow(out_header)
    f2.close()

f2 = open(out_file, 'a')
ol = [["winky", "dinky", "dog"], ["run", "dmc", "jmj"]]
f2_out = csv.writer(f2)
f2_out.writerows(ol)
f2.close()