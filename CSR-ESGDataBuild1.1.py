# I think I need to add the list of tickers and then the offset of their fiscal year. I might re-work those structures.
# I think the easier way at this scale is to use one of the existing master files as an input to build the right structures.

# Need to check directories and file locations.
# Need to see if i really need the founded data...I think I have that already.


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

OutFile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1.1/Out/esg-v1.csv'

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

ESG_InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-ESG-1.csv'
Env_InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-Env-1.csv'
Com_InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-Com-1.csv'
Emp_InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-Emp-1.csv'
Gov_InFile =  '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/ESGData/CSR-Gov-1.csv'

# I think there is a better way to do all of this.
# Loads in dataframe
esg_df = pd.read_csv(ESG_InFile) # Can change to list or whatever when I am ready for that logic
env_df = pd.read_csv(Env_InFile)
com_df = pd.read_csv(Com_InFile)
emp_df = pd.read_csv(Emp_InFile)
gov_df = pd.read_csv(Gov_InFile)
esg_df['Month']= esg_df.Month.astype(str) # Makes sure that Month columns is not treated as a number.
env_df['Month']= env_df.Month.astype(str)
com_df['Month']= com_df.Month.astype(str)
emp_df['Month']= emp_df.Month.astype(str)
gov_df['Month']= gov_df.Month.astype(str)
print (esg_df)
print (env_df)
print (com_df)
print (emp_df)
print (gov_df)

# Here's the actual logic to work through the list of companies and the ranage of years.
# I think this probably demo's everything I need to do.
esg_out_list = [['Key', "CSR_ESG_Mean"]]
env_out_list = [['Key', "CSR_Env_Mean"]]
com_out_list = [['Key', "CSR_Com_Mean"]]
emp_out_list = [['Key', "CSR_Emp_Mean"]]
gov_out_list = [['Key', "CSR_Gov_Mean"]]
age_out_list = [['Key', 'Age']]

# tkr and fl are global values. I can drive out of the five CSR files with those values.

for tkr in TickerList:
    for fy in range(StartYear, EndYear + 1):
        fl = fisc_list_fxn(fy, TickerOffsetDic[tkr])
#        print (tkr, fy, TickerOffsetDic[tkr], ':', fl)
        ta = fy - TickerFoundedDic[tkr]
        key_string = tkr + "-" + str(fy)
        age_out_list.append([key_string, ta])

        esg_foo2 = esg_df[esg_df.Month.isin(fl)]
        env_foo2 = env_df[env_df.Month.isin(fl)]
        com_foo2 = com_df[com_df.Month.isin(fl)]
        emp_foo2 = emp_df[emp_df.Month.isin(fl)]
        gov_foo2 = gov_df[gov_df.Month.isin(fl)]

        esg_foo3 = (esg_foo2[tkr])
        env_foo3 = (env_foo2[tkr])
        com_foo3 = (com_foo2[tkr])
        emp_foo3 = (emp_foo2[tkr])
        gov_foo3 = (gov_foo2[tkr])

        esg_mf = esg_foo3.mean()
        env_mf = env_foo3.mean()
        com_mf = com_foo3.mean()
        emp_mf = emp_foo3.mean()
        gov_mf = gov_foo3.mean()

        esg_out_list.append([key_string, esg_mf])
        env_out_list.append([key_string, env_mf])
        com_out_list.append([key_string, com_mf])
        emp_out_list.append([key_string, emp_mf])
        gov_out_list.append([key_string, gov_mf])

        print(tkr, fy, TickerOffsetDic[tkr], fl, esg_mf, ta)
        print(tkr, fy, TickerOffsetDic[tkr], fl, env_mf, ta)
        print(tkr, fy, TickerOffsetDic[tkr], fl, com_mf, ta)
        print(tkr, fy, TickerOffsetDic[tkr], fl, emp_mf, ta)
        print(tkr, fy, TickerOffsetDic[tkr], fl, gov_mf, ta)

print(age_out_list)
print (esg_out_list)
print (env_out_list)
print (com_out_list)
print (emp_out_list)
print (gov_out_list)

esg_df2 = pd.DataFrame(esg_out_list).T.set_index(0).T
env_df2 = pd.DataFrame(env_out_list).T.set_index(0).T
com_df2 = pd.DataFrame(com_out_list).T.set_index(0).T
emp_df2 = pd.DataFrame(emp_out_list).T.set_index(0).T
gov_df2 = pd.DataFrame(gov_out_list).T.set_index(0).T
age_df2 = pd.DataFrame(age_out_list).T.set_index(0).T

print (esg_df2)
print (env_df2)
print (com_df2)
print (emp_df2)
print (gov_df2)
print (age_df2)

# Just start stacking together the values into a single dataframe
out_df = pd.merge(esg_df2, env_df2, how = 'outer')
out_df = pd.merge(out_df, com_df2, how = 'outer')
out_df = pd.merge(out_df, emp_df2, how = 'outer')
out_df = pd.merge(out_df, gov_df2, how = 'outer')
out_df = pd.merge(out_df, age_df2, how = 'outer')

print (out_df)
out_df.to_csv(OutFile)