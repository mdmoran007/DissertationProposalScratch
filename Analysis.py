import pandas as pd
import matplotlib.pyplot as plt

base_dir = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Out'
stake_f = base_dir + '/MasterStakeholderSheet.csv'
stake_df = pd.read_csv(stake_f)

print (stake_df)

stake_df['Fiscal_Year'] = pd.to_datetime(stake_df['Fiscal_Year'])
stake_df.set_index(stake_df['Fiscal_Year'], inplace = True)
ts = stake_df['Inv_Group_Count_Full']

plt.plot (stake_df['Fiscal_Year'], stake_df['Inv_Group_Count_Full'], "or")
plt.show()

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Example 1: contant variance
ts1 = []
mu, sigma, seg = 0.0, 1.0, 1000
for i in range(10):
    ts = np.random.normal(mu, sigma, seg) + np.random.randint(low=-10, high=10)
    ts1 = np.append(ts1, ts, axis=0)

plt.figure(figsize=(16, 4))
plt.plot(ts1)

# Example 2: varying variance
ts2 = []
mu, sigma, seg = 0.0, 1.0, 1000
for i in range(10):
    sig = np.random.randint(low=1, high=50)
    ts = np.random.normal(mu, sigma * sig, seg)
    ts2 = np.append(ts2, ts, axis=0)

plt.figure(figsize=(16, 4))
plt.plot(ts2)
plt.show()

import ruptures as rpt

# Detect the change points
algo1 = rpt.Pelt(model="rbf").fit(ts1)
change_location1 = algo1.predict(pen=10)

# Point the change points:
def plot_change_points(ts,ts_change_loc):
    plt.figure(figsize=(16,4))
    plt.plot(ts)
    for x in ts_change_loc:
        plt.axvline(x,lw=2, color='red')

plot_change_points(ts1,change_location1)
plt.show()