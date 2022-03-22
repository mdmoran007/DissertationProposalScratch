# This file will build the records to be added into the MasterStakeholderSheet for the ESG data.
# It will be keyed from Ticker and Fiscal Year
# It will contain one average value from each of the five files per ticker per year.
# It will build the CSV

# Load modules -----------------------------------------------------------------------------------
import pandas as pd

# Declare variables ------------------------------------------------------------------------------
TickerList = ['BA', 'CAT', 'CMI', 'CSX', 'CTAS', 'DE', 'DOV', 'EFX', 'EMR', 'FDX', 'GD',
              'GE', 'GWW', 'HON', 'ITW', 'LMT', 'LUV', 'MAS', 'MMM', 'NOC', 'NSC', 'PCAR',
              'PH', 'RHI', 'ROK', 'RTX', 'SNA', 'SWK', 'TXT', 'UNP', 'UPS', 'WM']

# Matches to Ticker List above.
OffsetList = [0, 0, 0, 0, 5, -2, 0, 0, -3, 5, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              -6, 0, -3, 0, 0, 0, 0, 0, 0, 0]

StartYear = 2009
EndYear = 2020

# Will need to calculate these values for each record.
# Will start the outfile with this row
Header = ['Ticker', 'Fiscal_Year', 'T-FY', 'Age', 'CSR_ESG', 'CSR_Env', 'CSR_Com', 'CSR_Emp', 'CSR_Gov']

# Where to find the input files. Will have to work through all five at once I suppose?
BaseDir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData'
InFileList = ['CSR-ESG-1.csv', 'CSR-Env-1.csv', 'CSR-Com-1.csv', 'CSR-Emp-1.csv', 'CSR-Gov-1.csv']

OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out/esg-v1.csv'

#Might want to add this too, not sure.
# Just seems good to have as another potentially moderating variable.
# Could use this to add company age at each point.
FoundedList = [1916, 1925, 1919, 1980, 1929, 1837, 1955, 1899, 1890, 1971, 1899,
               1892, 1927, 1906, 1912, 1995, 1967, 1929, 1902, 1930, 1881, 1905,
               1917, 1948, 1903, 1922, 1920, 1843, 1923, 1862, 1907, 1968]

# Build dictionary from two lists
TickerOffsetDic = {TickerList[i]: OffsetList[i] for i in range(len(TickerList))}
TickerFoundedDic = {TickerList[i]: FoundedList[i] for i in range(len(TickerList))}

print(TickerOffsetDic)
print(TickerFoundedDic)

# Begin function definitions ----------------------------------------------------------------------------

def fisc_list_fxn(fy, om): # --------------------------------------------------------------------------------
    # fy = fiscal year, om = offset month
    # Used to find which months are in a fiscal year
    # Returns a list of 12 items in the format YYYY.M
    # Used to set point in list
    fm_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # Three cases: Offset is negative, offset is zero, offset is positive.
    # Logic establishes start and end point for all cases.
    # The end logic is only used for the narrative print statement. Could actually be removed otherwise
    # Computation of the list is based off of the start points.
    if om < 0:
        fys = fy -1
        fye = fy
        fms = 13 + om
        fme = 12 + om
    if om < 0:
        fys = fy -1
        fye = fy
        fms = 13 + om
        fme = 12 + om
    elif om > 0:
        fys = fy
        fye = fy + 1
        fms = om + 1
        fme = om
    else:
        fys = fy
        fye = fy
        fms = 1
        fme = 12
#    print('offset', om, 'means fy', fy, 'start', fys, fms, 'end', fye, fme, ':')
    tys_list = []  # Ticker Year List: the 12 months that make up the fiscal year.
    for i in range(0, 12):
        if i + fms < 13:
            y = fys
        else:
            y = fys + 1
        #        print(y, fm_list[i+ fms])
        tys_list.append(str(y) + '.' + str(fm_list[i + fms]))
#    print(tys_list)
#    print('\n')
    return(tys_list)
# End fisc_list_fxn() -----------------------------------------------------------------------------------

InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-ESG-1.csv'

# Loads in dataframe
esg_df = pd.read_csv(InFile) # Can change to list or whatever when I am ready for that logic.
esg_df['Month']= esg_df.Month.astype(str) # Makes sure that Month columns is not treated as a number.
print (esg_df)

# Here's the actual logic to work through the list of companies and the ranage of years.
for tkr in TickerList:
    for fy in range(StartYear, EndYear + 1):
        fl = fisc_list_fxn(fy, TickerOffsetDic[tkr])
#        print (tkr, fy, TickerOffsetDic[tkr], ':', fl)
        foo2 = esg_df[esg_df.Month.isin(fl)]
        foo3 = (foo2[tkr])
        mf = foo3.mean()
        ta = fy - TickerFoundedDic[tkr]
        print(tkr, fy, TickerOffsetDic[tkr], fl, mf, ta)
