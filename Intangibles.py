# Intangibles.py -------------------------------------------------------------------------------------------------------
# This is a draft script working toward my dissertation proposal, looking at changes in intangible assets
# and and changes in reading level.
#
# If this goes well, I'll get some demo Pandas code and demo graphing code.
# I think I am going to try Bokeh for the graphing. Maybe GGplot as well?

# Load the reading levels into a dataframe. Look at how reading level has changed over from 2005 to 2019.

import pandas as pd

base_dir = '~/OneDrive/Academics/Illinois/Dissertation'
fn = base_dir + '/FinData/WRDS-TkrOpsData.csv'

TkrOpsData_df = pd.read_csv(fn)
print(TkrOpsData_df)
intan_df = TkrOpsData_df[['tic', 'fyear', 'at', 'gdwl', 'intano', 'TotDepXad', 'TotDepXrd', 'TotIntan', 'PercentIntan']]

print (intan_df.dtypes)
print (intan_df)

# Add column that sums all of the intangibles
# Add a column that



