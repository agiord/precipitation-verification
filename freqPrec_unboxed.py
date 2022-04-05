import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""
Script per plottare istogrammi di frequenza relativa in base ai bin definiti dagli intervalli di soglie di precipitazione
Per dati non boxati
"""


pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/preci_freq_distr_unboxed/JJAonly'

"""
PROVA 2003
"""
#Dataframe con conteggi per punto griglia divisi per bin
df_01_05 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin01-05.csv", skiprows=0, sep="\s+")
df_05_1 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin05-1.csv", skiprows=0, sep="\s+")
df_1_2 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin1-2.csv", skiprows=0, sep="\s+")
df_2_3 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin2-3.csv", skiprows=0, sep="\s+")
df_3_5 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin3-5.csv", skiprows=0, sep="\s+")
df_5_7 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin5-7.csv", skiprows=0, sep="\s+")
df_7_10 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin7-10.csv", skiprows=0, sep="\s+")
df_10_20 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin10-20.csv", skiprows=0, sep="\s+")
df_20_500 = pd.read_csv(f"{pathIn}/HISTCOUNT2_sphera2003_COMPLETE_bin20-500.csv", skiprows=0, sep="\s+")

#Dataframe con conteggi per  punto griglia per un unico bin comprendente tutti i punti
df_all01_500 = pd.read_csv(f"{pathIn}/histcount_ALL01-500_sphera2003_COMPLETE.csv", skiprows=0,sep="\s+")
#sommo tutti i conteggi su tutti i punti griglia per normalizzare poi la somma sui punti griglia per i vari bin differenziati
Ntot = sum(df_all01_500.Value)


"""
ALL: 2003-2017
"""
#sphera
df_01_05_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin01-05.csv", skiprows=0, sep="\s+")
df_05_1_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin05-1.csv", skiprows=0, sep="\s+")
df_1_2_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin1-2.csv", skiprows=0, sep="\s+")
df_2_5_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin2-5.csv", skiprows=0, sep="\s+")
df_5_75_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin5-75.csv", skiprows=0, sep="\s+")
df_75_10_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin75-10.csv", skiprows=0, sep="\s+")
df_10_20_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin10-20.csv", skiprows=0, sep="\s+")
df_20_500_sp = pd.read_csv(f"{pathIn}/HISTCOUNT_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017_bin20-500.csv", skiprows=0, sep="\s+")

#era5
df_01_05_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin01-05.csv", skiprows=0, sep="\s+")
df_05_1_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin05-1.csv", skiprows=0, sep="\s+")
df_1_2_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin1-2.csv", skiprows=0, sep="\s+")
df_2_5_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin2-5.csv", skiprows=0, sep="\s+")
df_5_75_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin5-75.csv", skiprows=0, sep="\s+")
df_75_10_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin75-10.csv", skiprows=0, sep="\s+")
df_10_20_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin10-20.csv", skiprows=0, sep="\s+")
df_20_500_er = pd.read_csv(f"{pathIn}/HISTCOUNT_ERA5_JJA_tpH_land_m1000_f01_2003-2017_bin20-500.csv", skiprows=0, sep="\s+")

#Dataframe rianalisi con conteggi per  punto griglia per un unico bin comprendente tutti i punti
df_all01_500_sp = pd.read_csv(f"{pathIn}/histcount_ALL01-500_SPHERA_hourly_JJA_tpH_land_dec_f01_2003-2017.csv", skiprows=0,sep="\s+")
df_all01_500_er = pd.read_csv(f"{pathIn}/histcountALL01-500_ERA5_JJA_tpH_land_m1000_f01_2003-2017.csv", skiprows=0,sep="\s+")

#sommo tutti i conteggi su tutti i punti griglia per normalizzare poi la somma sui punti griglia per i vari bin differenziati
Ntot_sp = sum(df_all01_500_sp.Value)
Ntot_er = sum(df_all01_500_er.Value)

#sphera
freq_hist_sp = np.zeros(8)
i=0

for df in [df_01_05_sp, df_05_1_sp, df_1_2_sp, df_2_5_sp, df_5_75_sp, df_75_10_sp, df_10_20_sp, df_20_500_sp]:

    #sommo tutti i valori per tutti i punti griglia relativi a quel bin
    summ = np.sum(df.Value)
    
    #numero di punti griglia con valori >0
    #Ngrid = len(df)
    #Numero valori in tutti gli anni = 10anni*365gg*24hh +4anniBis*366gg*24hh
    #Nval = 11*365*24 + 4*366*24 #131180 da grib count
    
    freq_hist_sp[i] = summ/Ntot_sp
    i=i+1
  
#era5 
freq_hist_er = np.zeros(8)
i=0

for df in [df_01_05_er, df_05_1_er, df_1_2_er, df_2_5_er, df_5_75_er, df_75_10_er, df_10_20_er, df_20_500_er]:

    #sommo tutti i valori per tutti i punti griglia relativi a quel bin
    summ = np.sum(df.Value)
    
    #numero di punti griglia con valori >0
    #Ngrid = len(df)
    #Numero valori in tutti gli anni = 10anni*365gg*24hh +4anniBis*366gg*24hh
    #Nval = 11*365*24 + 4*366*24 #131180 da grib count
    
    freq_hist_er[i] = summ/Ntot_er
    i=i+1


#DEWETRA -> usare il dictionary dew_df_hours_allSeas ottenuto in script obs_dbTOdailyCycle.py (runnare prima questo!)
dew_df_hours_allSeas

#cat tutti i df divisi in ore insieme:
dew_jja_pp = pd.DataFrame()
for hour in np.arange(0,24,1):
    dew_jja_pp = pd.concat([dew_jja_pp,dew_df_hours_allSeas[hour]])

dew_jja_counts = np.histogram(dew_jja_pp[0], bins=[0.1,0.5,1,2,5,7.5,10,20,500])[0]

freq_hist_dew = dew_jja_counts/sum(dew_jja_counts)


#PLOT ISTOGRAMMA
thresh_int = ["[0.1,0.5)","[0.5,1)","[1,2)","[2,5)","[5,7.5)","[7.5,10)","[10,20)", "[20,50)"]

#dataframe con obs, sphera ed era5 ai vari livelli di thresholds
df_freq = pd.DataFrame(index=range(len(freq_hist_sp)), columns=['Obs','Sphera','Era5','thresh_int'])
df_freq['Obs'] = freq_hist_dew
df_freq['Sphera'] = freq_hist_sp
df_freq['Era5'] = freq_hist_er
df_freq['thresh_int'] = thresh_int
melt_df_freq = pd.melt(df_freq, id_vars=['thresh_int'])




#HISTOGRAMS PLOT FOR THE TWO OBSERVATIVE DATASETS
sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(1, 1, figsize=(9,8))  #, ax6
    
ax1.set_title('Hourly rainfall frequency distributions (unboxed)', fontsize=20)
ax1.tick_params(axis='both', which='major', labelsize=15)
ax1.set_xlabel('Hourly precipitation [mm]',fontsize=18)

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_freq, palette=["orange", "#87489D", "#32AAB5"])

ax1.legend(title='', fontsize=16)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('Frequency', fontsize = 18)
#sns.despine(offset=10, trim=True)

handles, labels = plt.gca().get_legend_handles_labels()
labels = ['DEWETRA', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend1 = ax1.legend(by_label.values(), by_label.keys(), title='2003-2017', fontsize=18)
#ax1.set_ylim([0.0,0.02])

plt.setp(legend1.get_title(),fontsize=18)

plt.savefig(f'{pathIn}/rainfall_dist_2003-2017_NOBox.png', bbox_inches="tight", dpi=300)



#DUE GRAFICI SEPARATI PER VEDERE MEGLIO RISOLUZ SULLE Y

df_freq1 = df_freq[0:4]   df_freq1.sum(axis=0)
df_freq2 = df_freq[4:]      df_freq2.sum(axis=0)

melt_df_freq1 = pd.melt(df_freq1, id_vars=['thresh_int'])
melt_df_freq2 = pd.melt(df_freq2, id_vars=['thresh_int'])


sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(1, 1, figsize=(6,4))  #, ax6
    
#ax1.set_title('Hourly rainfall frequency distributions (unboxed)', fontsize=20)

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_freq2, 
            edgecolor="black", palette=["#023FA5", "#87489D", "#32AAB5"])

ax1.tick_params(axis='both', which='major', labelsize=15)
ax1.set_xlabel('Precipitation [mm/h]',fontsize=15)
ax1.legend(title='', fontsize=16)                                                                   
#ax1.grid(True, linestyle='--')
ax1.set_ylabel('Frequency [%]', fontsize = 15)
#sns.despine(offset=10, trim=True)

y_vals = ax1.get_yticks()
ax1.set_yticklabels(['{:3.0f}'.format(x * 100) for x in y_vals])

handles, labels = plt.gca().get_legend_handles_labels()
labels = ['DEWETRA', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend1 = ax1.legend(by_label.values(), by_label.keys(), fontsize=14)
#ax1.set_ylim([0.0,0.02])

plt.savefig(f'{pathIn}/rainfall_dist_2003-2017_NOBox_bins_2.pdf', bbox_inches="tight", dpi=300)





























