# ----------------------------------------------------------------------------------------------------------------------
# ExecucompTransform1.py
# A utility to transform the extract from WRDS Execucomp and transform the data to prep for Stakeholder analysis.
# Columns: EXEC_FULLNAME, GVKEY, EXECID, YEAR, TICKER, BECAMECEO, JOINED_CO, GENDER, TITLE
#   - Load Csv into data structure (Done)
#   - Select only with BECAMECEO NE “” (Done)
#   - Make Key (Done)
#   - Calculate YearsWithCo <= This data is pretty incomplete. Going to drop it instead.
#   - Calculate YearsAsCEO (Done)
#   - Rename Columns: Gender, Ticker, FiscYear, CEO_FullName, GvKey (Done)
#   - Make empty columns: Age, CeoChairmanDuality, EdBackground1, EdBackground2, EdBackground3, EdLevel (Done)

# Load libraries -------------------------------------------------------------------------------------------------------
import os
import pandas as pd

# Set variables --------------------------------------------------------------------------------------------------------
execucomp_infile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper2/TestData/ExecucompTest6.csv'
execucomp_outfile = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper2/TestData/ExecucompOut1.csv'

# Load Csv into Pandas DataFrame
execucomp_df = pd.read_csv(execucomp_infile)
print(execucomp_df)

# Rename Columns
execucomp_df.rename(columns = {'EXEC_FULLNAME':'CeoFullName',
                               'GENDER':'Gender',
                               'GVKEY':'gvkey',
                               'YEAR':'FiscYear',
                               'TICKER':'Ticker',
                               'EXECID':'ExecId',
                               'BECAMECEO':'BecameCeo',
#                               'JOINED_CO':'Joined',
                               'PCEO':'PCeo',
                               'TITLE':'Title',
                               }, inplace = True)
print(execucomp_df)

# Drop columns:
# EXEC_LNAME, EXEC_FNAME, EXEC_MNAME, CONAME, CO_PER_ROL
execucomp_df = execucomp_df.drop('EXEC_LNAME',axis=1)
execucomp_df = execucomp_df.drop('EXEC_MNAME',axis=1)
execucomp_df = execucomp_df.drop('EXEC_FNAME',axis=1)
execucomp_df = execucomp_df.drop('CONAME',axis=1)
execucomp_df = execucomp_df.drop('CO_PER_ROL',axis=1)
execucomp_df = execucomp_df.drop('JOINED_CO',axis=1)

print (execucomp_df)

# Add empty columns
# Age, CeoChairmanDuality, EdBackground1, EdBackground2, EdBackground3, EdLevel
execucomp_df['Age'] = ''
execucomp_df['CeoChairmanDuality'] = ''
execucomp_df['EdBackground1'] = ''
execucomp_df['EdBackground2'] = ''
execucomp_df['EdBackground3'] = ''
execucomp_df['EdBackground4'] = ''
execucomp_df['EdLevel'] = ''

print (execucomp_df)
print(list(execucomp_df))

# Merge two columns
execucomp_df['Key'] = execucomp_df['Ticker'] + '.' + execucomp_df['FiscYear'].astype('str')
print(execucomp_df)

# Drop rows that has NaN values on selected columns
execucomp_df=execucomp_df.dropna(subset=['BecameCeo'])

print(execucomp_df)
print(execucomp_df['BecameCeo'])

# YearsWithCo
#print(execucomp_df['Joined'])
#execucomp_df['JoinedYear'] = execucomp_df['Joined'].astype('str')

# YearsAsCeo
execucomp_df['BecameCeoYear'] = execucomp_df['BecameCeo'].astype('str').str[0:4]
execucomp_df['YearsAsCeo'] = execucomp_df['FiscYear'].astype('int') - execucomp_df['BecameCeoYear'].astype('int')
print(execucomp_df)
execucomp_df.to_csv(execucomp_outfile)

