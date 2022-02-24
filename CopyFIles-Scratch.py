import shutil
import os
from os.path import exists

base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation'
src_dir = base_dir + '/Letters/09-CL-txt'
dst_dir =  base_dir + '/Paper1/Letters/09-CL-txt'
fnf = 'tttt-CL1-FYyyyy.txt'

tkr_list = ['BA', 'CAT', 'CMI', 'CSX', 'CTAS', 'DE', 'DOV', 'EFX', 'EMR', 'FDX',
            'GD', 'GE', 'GWW', 'HON', 'ITW', 'LMT', 'LUV', 'MAS', 'MMM', 'NOC',
            'NSC', 'PCAR', 'PH', 'RHI', 'ROK', 'RTX', 'SNA', 'SWK', 'TXT',
            'UNP', 'UPS', 'WM']

for yr in range(2004, 2020):
    print (yr)
    for tkr in tkr_list:
        fnt = fnf.replace('tttt', tkr)
        fn = fnt.replace('yyyy', str(yr))
        src_f = src_dir + '/' + fn
        dst_f = dst_dir + '/' + fn
#        print (fnf, fnt, fn)
        if  exists(src_f):
            print (fn, 'exists.')
            shutil.copyfile(src_f, dst_f)
        else:
            print (fn, "does not exist.")


