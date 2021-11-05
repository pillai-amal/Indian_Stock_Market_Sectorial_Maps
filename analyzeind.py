import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import requests
import numpy as np

# request = requests.get('https://www.bloombergquint.com/feapi/markets/indices/indian-indices?duration=1D&tab=all').json()
con = sqlite3.connect('indindices.db')
cur = con.cursor()
indexlis, change = [], []
chnage_index_dict = {}
nifty_sect = ["BANKNIFTY","NIFTYIT","NIFTYPHARMA","NIFTYFINANCE","NIFTYFMCG","NIFTYMNC","NIFTYSERVICE","NIFTYENERGY","NIFTYREALTY","NIFTYPSUBANK","NIFTYPSE","NIFTYCONSUMP","NIFTYAUTO","NIFTYMETAL","NIFTYMEDIA","NIFTYCDTY"]

# for i in range(0, len(request['data'])-11): #16
for each_sect in nifty_sect:
        DF = pd.read_sql(f"SELECT * FROM {each_sect}", con)
        pd.to_datetime(DF['date'])
        DF.set_index('date', inplace= True)
        DF.sort_index(inplace= True)
        chnage_index_dict[each_sect] = [DF['change'][indx] for indx in DF.index]
        indexlis.append(each_sect)
        change.append(DF['change'].iloc[-1])

LASTEST = pd.DataFrame({'INDEX' : indexlis, 'CHANGE': change})
LASTEST.to_csv("index.csv")
print(chnage_index_dict)
# stackplot
plt.stackplot(DF.index, chnage_index_dict.values(), labels= chnage_index_dict.keys())
legend = plt.legend(loc='upper left')
legend.get_frame()

# #heatmap
data = list(chnage_index_dict.values())
nump_array = np.array(data)
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(nump_array, cmap="RdYlGn")
ax.set_xticks(np.arange(len(DF.index)))
ax.set_yticks(np.arange(len(chnage_index_dict.keys())))

ax.set_xticklabels(DF.index,rotation=-90)
ax.set_yticklabels(chnage_index_dict.keys())
ax.spines[:].set_visible(False)
ax.grid(which="minor", color="b", linestyle='-', linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)

for i in range(len(nifty_sect)):
    for j in range(len(DF.index)):
        text = ax.text(j, i, nump_array[i, j], ha="center", va="center", color="w")

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Change', rotation=-90, va="bottom")

#showing the plot
plt.tight_layout()

plt.show()

