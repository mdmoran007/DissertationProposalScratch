# InvestorDataBuild.py ----------------------------------------------------------------------------
# File Takes input from WRDS-Tkr-StockData-13F.csv, WRDS-Tkr-StockData-ISS-Largeblock.csv
# and builds a dataframe that gets written out to a file.



# Load modules -----------------------------------------------------------------------------------
import pandas as pd

# Declare variables ------------------------------------------------------------------------------
TickerList = ['BA', 'CAT', 'CMI', 'CSX', 'CTAS', 'DE', 'DOV', 'EFX', 'EMR', 'FDX', 'GD',
              'GE', 'GWW', 'HON', 'ITW', 'LMT', 'LUV', 'MAS', 'MMM', 'NOC', 'NSC', 'PCAR',
              'PH', 'RHI', 'ROK', 'RTX', 'SNA', 'SWK', 'TXT', 'UNP', 'UPS', 'WM']

StartYear = 2004
EndYear = 2020

owner_out_list = [["Ticker", "Fiscal_Year", "Large_Blockholder_Count", "Large_Blockholder_Perc",
              "Inst_Own_Perc"]]

base_dir = "/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation"
lb_file = base_dir + "/FinData/WRDS-Tkr-StockData-LargeBlock.csv"
io_file = base_dir + "/FinData/WRDS-Tkr-StockData-13F.csv"
out_file = base_dir + "/Paper1/Out/owners.csv"

lb_df = pd.read_csv(lb_file)
io_df = pd.read_csv(io_file)

print (lb_df)
print (io_df)

for tkr in TickerList:
    for fy in range(StartYear, EndYear):
#        print (tkr, fy)
        out_df1 = lb_df[(lb_df["Fiscal_Year"] == fy) & (lb_df["Ticker"] == tkr)]
        lbc = out_df1["Large_Blockholder_Percentage"].mean()
        lbp = out_df1["Large_Blockholder_Count"].mean()
        out_df2 = io_df[(io_df["Year"] == fy) & (io_df["ticker"] == tkr)]
        iop = out_df2["InstOwn_Perc"].max()
#        print (out_df1)
#        print (out_df2)

#        print (len(out_df1), len(out_df2))
        print (tkr, fy, lbc, lbp, iop)
        owner_out_list.append([tkr, fy, lbc, lbp, iop])

print (owner_out_list)
out_df = pd.DataFrame(owner_out_list)
out_df.fillna(0)
print (out_df)
out_df.to_csv(out_file)



