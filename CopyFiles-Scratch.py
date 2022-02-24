import shutil
import os
from os.path import exists

base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation'
src_dir = base_dir + '/Letters/09-CL-txt'
dst_dir = base_dir + '/Paper1/Letters/09-CL-txt' # May need to add other dir's over time, but will start here.
fnf = 'tttt-CL1-FYyyyy.txt' # File Name Format

# This is the list of the Industrial Tickers that are in the S&P 500 for that whole time.
tkr_list = ['BA', 'CAT', 'CMI', 'CSX', 'CTAS', 'DE', 'DOV', 'EFX', 'EMR', 'FDX',
            'GD', 'GE', 'GWW', 'HON', 'ITW', 'LMT', 'LUV', 'MAS', 'MMM', 'NOC',
            'NSC', 'PCAR', 'PH', 'RHI', 'ROK', 'RTX', 'SNA', 'SWK', 'TXT',
            'UNP', 'UPS', 'WM']

for yr in range(2004, 2020): # Letters through 2019...add one to get to the end...
    print(yr)
    for tkr in tkr_list:
        fnt = fnf.replace('tttt', tkr)
        fn = fnt.replace('yyyy', str(yr))
        src_f = src_dir + '/' + fn
        dst_f = dst_dir + '/' + fn
        #        print (fnf, fnt, fn)
        if exists(src_f):
            print(fn, 'exists.')
            shutil.copyfile(src_f, dst_f)
        else:
            print(fn, "does not exist.")
