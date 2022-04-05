import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns


dataset='DEWETRA'  #'DEWETRA'

aggr='max'   #'max'

if dataset == 'ARCIS':
    all_seas_fold = 'all_seasons_2003-2014'
else:
    all_seas_fold = 'all_seasons_2003-2017'

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{dataset}'

pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_{dataset}/box_60_{aggr}/seasons_boxplot'



#build dataframe for plotting boxplot depending on the threshold of interest (based on index thr_ind), and score (TS,POD,FAR):
def df_seasons_thr(thr_ind, aggr, score='ts'):
    
    if dataset == 'DEWETRA':
    
        trances = ['2003-2006', '2007-2010', '2011-2014', '2015-2017']
   
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14', 'MAM15', 'MAM16', 'MAM17']
        summers = ['JJA04', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14', 'JJA15', 'JJA16', 'JJA17']
        falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14', 'SON15', 'SON16', 'SON17']
        winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']
        
        years = ['2003','2004','2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
        
    else:
    
        trances = ['2003-2006', '2007-2010', '2011-2014']#, '2015-2017']
       
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14']#, 'MAM15', 'MAM16', 'MAM17']
        summers = ['JJA04', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14']#, 'JJA15', 'JJA16', 'JJA17']
        falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14']#, 'SON15', 'SON16', 'SON17']
        winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13']#, 'DJF15', 'DJF16']
        
        years = ['2003','2004','2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014']#, '2015', '2016', '2017']
        
    MAM_sphera = {}
    MAM_era5 = {}
    
    JJA_sphera = {}
    JJA_era5 = {}
    
    SON_sphera = {}
    SON_era5 = {}
    
    DJF_sphera = {}
    DJF_era5 = {}
    
    
    for season in springs:
        
        MAM_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        MAM_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in summers:
        
        JJA_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        JJA_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in falls:
        
        SON_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        SON_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in winters:
        
        DJF_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        DJF_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{all_seas_fold}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    
    #build dataframe to contain all values of e.g. TS at a certain threshold for all the seasons and the two reanalysis:
    df_seasons = pd.DataFrame(index=np.arange(0,2*len(MAM_sphera),1) ,columns=['MAM', 'JJA', 'SON', 'DJF', 'year', 'dataset'])
    
    for ind in df_seasons.index[1::2]:    
        df_seasons['dataset'][ind] = 'ERA5'
        df_seasons['dataset'][ind-1] = 'SPHERA'
        
    for i,j in zip(df_seasons.index[0::2], np.arange(0,len(years),1)):
        df_seasons['year'][i] = years[j]
        df_seasons['year'][i+1] = years[j]
    
    for ind, s_ind in zip(df_seasons.index[1::2], np.arange(0,len(springs),1)):
        df_seasons['MAM'][ind] = MAM_era5[springs[s_ind]][score][thr_ind]
        df_seasons['MAM'][ind-1] = MAM_sphera[springs[s_ind]][score][thr_ind]
        
        df_seasons['JJA'][ind] = JJA_era5[summers[s_ind]][score][thr_ind]
        df_seasons['JJA'][ind-1] = JJA_sphera[summers[s_ind]][score][thr_ind]
        
        df_seasons['SON'][ind] = SON_era5[falls[s_ind]][score][thr_ind]
        df_seasons['SON'][ind-1] = SON_sphera[falls[s_ind]][score][thr_ind]
        

    #winters for SPHERA
    j=0
    for i in df_seasons.index[0::2]:
        if (df_seasons['year'][i] == '2006' or df_seasons['year'][i] == '2010' or df_seasons['year'][i] == '2014' or df_seasons['year'][i] == '2017'):
            df_seasons['DJF'][i] = np.nan
            continue
        else:
            df_seasons['DJF'][i] = DJF_sphera[winters[j]][score][thr_ind]
            j=j+1
    
    #winters for ERA5
    j=0
    for i in df_seasons.index[1::2]:
        if (df_seasons['year'][i] == '2006' or df_seasons['year'][i] == '2010' or df_seasons['year'][i] == '2014' or df_seasons['year'][i] == '2017'):
            df_seasons['DJF'][i] = np.nan
            continue
        else:
            df_seasons['DJF'][i] = DJF_era5[winters[j]][score][thr_ind]
            j=j+1
    
    #check for -999.9 values and substitute with np.nan
    for seas in ['MAM','JJA', 'SON', 'DJF']:
        for i in df_seasons.index:
            if df_seasons[seas][i] == -999.9:
                df_seasons[seas][i] = np.nan
    
    #prepare data for boxplot:
    melted_df_seasons = pd.melt(df_seasons.drop(['year'],axis=1), id_vars=['dataset'])
    melted_df_seasons.value = melted_df_seasons.value.astype(float)    
    
    return df_seasons, melted_df_seasons



"""""""""""""""""""""""""""""""""""""""""""""""""""""
GRAFICI PARAGONE VALORI MEDI SUL PERIODO LUNGO TRA MEDIE E MAX NELLE BOX
"""""""""""""""""""""""""""""""""""""""""""""""""""""

pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_{dataset}/box60_max_VS_mean'


df_1mm_max = df_seasons_thr(0,'max')[1]
df_5mm_max = df_seasons_thr(1,'max')[1]
df_10mm_max = df_seasons_thr(2,'max')[1]
df_15mm_max = df_seasons_thr(3,'max')[1]
df_25mm_max = df_seasons_thr(4,'max')[1]
df_50mm_max = df_seasons_thr(5,'max')[1]
df_80mm_max = df_seasons_thr(6,'max')[1]
df_150mm_max = df_seasons_thr(7,'max')[1]

df_1mm_mean = df_seasons_thr(0,'mean')[1]
df_5mm_mean = df_seasons_thr(1,'mean')[1]
df_10mm_mean = df_seasons_thr(2,'mean')[1]
df_15mm_mean = df_seasons_thr(3,'mean')[1]
df_25mm_mean = df_seasons_thr(4,'mean')[1]
df_50mm_mean = df_seasons_thr(5,'mean')[1]
df_80mm_mean = df_seasons_thr(6,'mean')[1]
df_150mm_mean = df_seasons_thr(7,'mean')[1]



#do the mean for a spec thresh and season on all the seasons for the years considered 
sphera_seasonal_means_MAX = pd.DataFrame(index=np.arange(0,8), columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])
era5_seasonal_means_MAX = pd.DataFrame(index=np.arange(0,8), columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])    

sphera_seasonal_means_MAX['thr'] = [1.0,5.0,10.0,15.0,25.0,50.0,80.0,150.0]
era5_seasonal_means_MAX['thr'] = [1.0,5.0,10.0,15.0,25.0,50.0,80.0,150.0]

thr_ind=0
for df in [df_1mm_max, df_5mm_max, df_10mm_max, df_15mm_max, df_25mm_max, df_50mm_max, df_80mm_max, df_150mm_max]:
    
    for season in ['MAM', 'JJA', 'SON', 'DJF']:
        
        #np.nanmean -> np.mean but ignoring nan values
        sphera_seasonal_means_MAX[f'ts_{season}'][thr_ind] = np.nanmean(df['value'].loc[(df['dataset'] == 'SPHERA') &
                                                                                 (df['variable'] == f'{season}')])
        era5_seasonal_means_MAX[f'ts_{season}'][thr_ind] = np.nanmean(df['value'].loc[(df['dataset'] == 'ERA5') &
                                                                                 (df['variable'] == f'{season}')])

    thr_ind = thr_ind + 1


sphera_seasonal_means_MEAN = pd.DataFrame(index=np.arange(0,8), columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])
era5_seasonal_means_MEAN = pd.DataFrame(index=np.arange(0,8), columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])    

sphera_seasonal_means_MEAN['thr'] = [1.0,5.0,10.0,15.0,25.0,50.0,80.0,150.0]
era5_seasonal_means_MEAN['thr'] = [1.0,5.0,10.0,15.0,25.0,50.0,80.0,150.0]

thr_ind=0
for df in [df_1mm_mean, df_5mm_mean, df_10mm_mean, df_15mm_mean, df_25mm_mean, df_50mm_mean, df_80mm_mean, df_150mm_mean]:
    
    for season in ['MAM', 'JJA', 'SON', 'DJF']:
        
        #np.nanmean -> np.mean but ignoring nan values
        sphera_seasonal_means_MEAN[f'ts_{season}'][thr_ind] = np.nanmean(df['value'].loc[(df['dataset'] == 'SPHERA') &
                                                                                 (df['variable'] == f'{season}')])
        era5_seasonal_means_MEAN[f'ts_{season}'][thr_ind] = np.nanmean(df['value'].loc[(df['dataset'] == 'ERA5') &
                                                                                 (df['variable'] == f'{season}')])

    thr_ind = thr_ind + 1







matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['xtick.minor.width'] = 0

#DJF and JJA plot
fig, ax = plt.subplots(figsize=(11,5))
ax.set_xscale('log')
ax.set_title('Average TS vs daily rainfall thresholds, ' + r'$\bf{ERA5 vs ' + dataset + '}$ (2003-2017)' , fontsize=17)
ax.set_ylim([-0.05,0.7])

#ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_JJA'], '-o',  markersize=8, color='#7F000D', label='Summer')
#ax.plot(sphera_seasonal_means_MEAN['thr'], sphera_seasonal_means_MEAN['ts_JJA'], '--o',  markersize=8, mfc='none', color='#7F000D')
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_JJA'], '-o',  markersize=8, color='#7F000D', label='Summer')
ax.plot(era5_seasonal_means_MEAN['thr'], era5_seasonal_means_MEAN['ts_JJA'], '--o',  markersize=8, mfc='none', color='#7F000D')

#ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_DJF'], '-o',  markersize=8, color='#023FA5', label='Winter')
#ax.plot(sphera_seasonal_means_MEAN['thr'], sphera_seasonal_means_MEAN['ts_DJF'], '--o',  markersize=8, mfc='none', color='#023FA5')
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_DJF'], '-o',  markersize=8, color='#023FA5', label='Winter')
ax.plot(era5_seasonal_means_MEAN['thr'], era5_seasonal_means_MEAN['ts_DJF'], '--o',  markersize=8, mfc='none', color='#023FA5')

ax.set_xticks(sphera_seasonal_means_MAX['thr'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=16)
ax.set_ylabel('Threat Score', fontsize=16)
legend = plt.legend(fontsize=15, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])

l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, color='black', 
           label='Max',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, mfc='none', color='black', 
           label='Mean', scaley=False)
leg = ax1.legend(handles=[l1,l2], loc='best', fontsize=15, title='Box aggregation')
plt.setp(leg.get_title(),fontsize=15)

plt.savefig(f'{pathOut}/TS_JJA-DJF_2003-2017_ERA5_v_{dataset}_max_VS_mean.png', bbox_inches="tight", dpi=300)





matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['xtick.minor.width'] = 0

#DJF and JJA plot
fig, ax = plt.subplots(figsize=(11,5))
ax.set_xscale('log')
ax.set_title('Average TS vs daily rainfall thresholds, ' + r'$\bf{ERA5 vs ' + dataset + '}$ (2003-2017)' , fontsize=17)
ax.set_ylim([-0.05,0.7])

#ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_MAM'], '-o',  markersize=8, color='#006027', label='Spring')
#ax.plot(sphera_seasonal_means_MEAN['thr'], sphera_seasonal_means_MEAN['ts_MAM'], '--o',  markersize=8, mfc='none', color='#006027')
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_MAM'], '-o',  markersize=8, color='#006027', label='Spring')
ax.plot(era5_seasonal_means_MEAN['thr'], era5_seasonal_means_MEAN['ts_MAM'], '--o',  markersize=8, mfc='none', color='#006027')

#ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_SON'], '-o',  markersize=8, color='#73243C', label='Fall')
#ax.plot(sphera_seasonal_means_MEAN['thr'], sphera_seasonal_means_MEAN['ts_SON'], '--o',  markersize=8, mfc='none', color='#73243C')
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_SON'], '-o',  markersize=8, color='#73243C', label='Fall')
ax.plot(era5_seasonal_means_MEAN['thr'], era5_seasonal_means_MEAN['ts_SON'], '--o',  markersize=8, mfc='none', color='#73243C')

ax.set_xticks(sphera_seasonal_means_MAX['thr'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=16)
ax.set_ylabel('Threat Score', fontsize=16)
legend = plt.legend(fontsize=15, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])

l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, color='black', 
           label='Max',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, mfc='none', color='black', 
           label='Mean', scaley=False)
leg = ax1.legend(handles=[l1,l2], loc='best', fontsize=15, title='Box aggregation')
plt.setp(leg.get_title(),fontsize=15)

plt.savefig(f'{pathOut}/TS_MAM-SON_2003-2017_ERA5_v_{dataset}_max_VS_mean.png', bbox_inches="tight", dpi=300)
    
