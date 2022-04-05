import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


pathIn = '/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/articoloInes/freqHistograms'

data_max = pd.read_csv(f'{pathIn}/frequenza_preci_fewThresholds_MAX.txt', sep=" ", header=None,  names=['obs','SPHERA','ERA5'])
data_mean = pd.read_csv(f'{pathIn}/frequenza_preci_fewThresholds_MEAN.txt', sep=" ", header=None,  names=['obs','SPHERA','ERA5'])

#sum first two rows to get data for <1mm/day:  
data_max.loc[0] = data_max.loc[0] + data_max.loc[1]
data_max = data_max.drop([1]).reset_index(drop=True)

data_mean.loc[0] = data_mean.loc[0] + data_mean.loc[1]
data_mean = data_mean.drop([1]).reset_index(drop=True)

#sum also last two rows to get data for >80 mm/day
data_max.loc[7] = data_max.loc[7] + data_max.loc[8]
data_max = data_max.drop([8]).reset_index(drop=True)

data_mean.loc[7] = data_mean.loc[7] + data_mean.loc[8]
data_mean = data_mean.drop([8]).reset_index(drop=True)


thresh_int = ["<1","1-5","5-10","10-15","15-25","25-50","50-80",">80"]

data_max['thresh_int'] = thresh_int
data_mean['thresh_int'] = thresh_int

melt_df_freq_max = pd.melt(data_max, id_vars=['thresh_int'])
melt_df_freq_mean = pd.melt(data_mean, id_vars=['thresh_int'])










#HISTOGRAMS PLOT FOR THE TWO OBSERVATIVE DATASETS
sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(1, 1, figsize=(9,5))  #, ax6

ax1.tick_params(axis='y', which='major', labelsize=15)
#ax2.set_title('DEWETRA')

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_freq_mean, palette=["#494949", "#929292", "#E2E2E2"], edgecolor='black')

ax1.legend(title='', fontsize=16)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('Normalized frequency', fontsize = 18)
ax1.set_xlabel('Precipitation threshold [mm/day]', fontsize=18)
sns.despine(offset=10, trim=True)
ax1.tick_params(axis='x', which='major', labelsize=16)
#ax2.set_ylim([0.0,0.02])


handles, labels = plt.gca().get_legend_handles_labels()
labels = ['Observations', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend = ax1.legend(by_label.values(), by_label.keys(), fontsize=14)

plt.setp(legend.get_title(),fontsize=14)

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/freqHist/freqHist_allThresh_mean.pdf', bbox_inches="tight", dpi=300)




#ZOOM PLOT ON HIGHER THRESHOLDS


data_max_ZOOM = data_max[5:]
data_mean_ZOOM = data_mean[5:]

melt_df_freq_max_ZOOM = pd.melt(data_max_ZOOM, id_vars=['thresh_int'])
melt_df_freq_mean_ZOOM = pd.melt(data_mean_ZOOM, id_vars=['thresh_int'])



sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(1, 1, figsize=(5,3))  #, ax6
    
ax1.tick_params(axis='both', which='major', labelsize=15)

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_freq_mean_ZOOM, palette=["#494949", "#929292", "#E2E2E2"], edgecolor='black')

ax1.grid(True, linestyle='--')
ax1.set_ylabel('Normalized frequency', fontsize = 18)
#ax1.set_ylim([0.0,0.015])
sns.despine(offset=1, trim=True)

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/freqHist/freqHist_ZOOM_mean.pdf', bbox_inches="tight", dpi=300)



