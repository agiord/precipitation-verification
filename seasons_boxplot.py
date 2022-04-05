import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns
from matplotlib import rc
rc('text', usetex=False)

#SCEGLIERE MEDIE O MASSIMI DELLE BOX (avg O max)
aggr='avg'   # o max

#SCEGLIERE DATASET OSSERVATE:
obs='ARCIS'  #DEWETRA


pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{obs}'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_{obs}/box60_{aggr}/seasons_boxplot'

if aggr == 'avg':
    aggregation='average'
elif aggr == 'max':
    aggregation='maximum'
    
if obs == 'ARCIS':
    period = '2003-2014'
elif obs == 'DEWETRA':
    period = '2003-2017'


#build dataframe for plotting boxplot depending on the threshold of interest (based on index thr_ind), and score (TS,POD,FAR):
def df_seasons_thr(thr_ind, score='ts'):
    
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
        
        MAM_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        MAM_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in summers:
        
        JJA_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        JJA_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in falls:
        
        SON_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        SON_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    
    for season in winters:
        
        DJF_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        DJF_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_{period}/{season}/scores_per_scad.dat",
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
        if (df_seasons['year'][i] == '2006' or df_seasons['year'][i] == '2010' or df_seasons['year'][i] == '2014'): # or df_seasons['year'][i] == '2017'):
            df_seasons['DJF'][i] = np.nan
            continue
        else:
            df_seasons['DJF'][i] = DJF_sphera[winters[j]][score][thr_ind]
            j=j+1
    
    #winters for ERA5
    j=0
    for i in df_seasons.index[1::2]:
        if (df_seasons['year'][i] == '2006' or df_seasons['year'][i] == '2010' or df_seasons['year'][i] == '2014'): # or df_seasons['year'][i] == '2017'):
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

#TS
df_5mm = df_seasons_thr(1)[1]
df_15mm = df_seasons_thr(3)[1]
df_25mm = df_seasons_thr(4)[1]
df_50mm = df_seasons_thr(5)[1]
df_80mm = df_seasons_thr(6)[1]
df_150mm = df_seasons_thr(7)[1]

#POD
df_5mm_pod = df_seasons_thr(1,'pod')[1]
df_15mm_pod = df_seasons_thr(3,'pod')[1]
df_25mm_pod = df_seasons_thr(4,'pod')[1]
df_50mm_pod = df_seasons_thr(5,'pod')[1]
df_80mm_pod = df_seasons_thr(6,'pod')[1]
df_150mm_pod = df_seasons_thr(7,'pod')[1]

#FAR
df_5mm_far = df_seasons_thr(1,'fa')[1]
df_15mm_far = df_seasons_thr(3,'fa')[1]
df_25mm_far = df_seasons_thr(4,'fa')[1]
df_50mm_far = df_seasons_thr(5,'fa')[1]
df_80mm_far = df_seasons_thr(6,'fa')[1]
df_150mm_far = df_seasons_thr(7,'fa')[1]


#Boxplot for a single threshold
def boxplot_single_thr(df, thr_ind, score='TS'):
    
    thresholds = [1.0,5.0,10.0,15.0,25.0,50.0,80.0,150.0]
    
    sns.set(style="ticks", palette="pastel")
    
    fig, ax1 = plt.subplots(1, 1, figsize=(13,8), dpi=100)
    
    sns.swarmplot(x="variable", y="value", data=df, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    
    sns.despine(offset=5, trim=True)
    
    ax1.grid(True, linestyle='--')
    ax1.set_ylabel(f'{score}', fontsize=17)
    ax1.set_xlabel('Season', fontsize=17)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    
    ax1.set_title(f'{score} seasonal distributions for the period 2003-2017, threshold = {int(thresholds[thr_ind])} mm', 
                  fontsize=20)
    #legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, [handles[0],handles[1]]))
    ax1.legend(by_label.values(), by_label.keys(), title='', fontsize=17)
    
    


boxplot_single_thr(df_15mm, 3, score='TS')


boxplot_single_thr(df_15mm_pod, 3, score='POD')


boxplot_single_thr(df_15mm_far, 3, score='FAR')


#PLOT MANY THRESHOLDS
def boxplot_many_thresh(df1, df2, df3, df4, df5, df6, score='TS'):
    
    sns.set(style="ticks", palette="pastel")
    
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(13,18))  #, ax6
    
    fig.subplots_adjust(hspace=0.0)
    fig.suptitle(f"{score} seasonal distributions ({period}) \n using the {aggregation} on the box, vs" + rf" $\bf{{{obs}}}$", 
                 fontsize=27, y=0.92)
    
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    sns.swarmplot(x="variable", y="value", data=df1, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df1, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    sns.despine(offset=5, trim=True)
    ax1.grid(True, linestyle='--')
    ax1.set_ylabel('5 mm/day', fontsize=22)
    ax1.set_xlabel('')
    ax1.xaxis.set_ticklabels([])
    ax1.yaxis.set_major_locator(plt.MaxNLocator(4))
    #ax1.set_yticks([0.3,0.4,0.5,0.6])
    ax1.tick_params(axis='y', which='major', labelsize=16)
    ax1.legend([])
        
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=1, colspan=1)
    sns.swarmplot(x="variable", y="value", data=df2, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df2, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    sns.despine(offset=5, trim=True)
    ax2.grid(True, linestyle='--')
    ax2.set_ylabel('15 mm/day', fontsize=22)
    ax2.set_xlabel('')
    ax2.xaxis.set_ticklabels([])
    ax2.tick_params(axis='y', which='major', labelsize=16)
    ax2.legend([])
    
    ax3 = plt.subplot2grid((6,1), (2,0), rowspan=1, colspan=1)
    sns.swarmplot(x="variable", y="value", data=df3, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df3, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    sns.despine(offset=5, trim=True)
    ax3.grid(True, linestyle='--')
    ax3.set_ylabel('25 mm/day', fontsize=22)
    ax3.set_xlabel('')
    ax3.xaxis.set_ticklabels([])
    ax3.tick_params(axis='y', which='major', labelsize=16)
    ax3.legend([])
    
    ax4 = plt.subplot2grid((6,1), (3,0), rowspan=1, colspan=1)
    sns.swarmplot(x="variable", y="value", data=df4, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df4, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    sns.despine(offset=5, trim=True)
    ax4.grid(True, linestyle='--')
    ax4.set_ylabel('50 mm/day', fontsize=22)
    ax4.set_xlabel('')
    ax4.xaxis.set_ticklabels([])
    ax4.tick_params(axis='y', which='major', labelsize=16)
    ax4.legend([])
    
    ax5 = plt.subplot2grid((6,1), (4,0), rowspan=1, colspan=1)
    sns.swarmplot(x="variable", y="value", data=df5, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
    sns.boxplot(data=df5, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
    sns.despine(offset=5, trim=True)
    ax5.grid(True, linestyle='--')
    ax5.set_ylabel('80 mm/day', fontsize=22)
    ax5.set_xlabel('Season', fontsize=22)
    #ax5.xaxis.set_ticklabels([])
    #ax5.legend([])
    ax5.tick_params(axis='x', which='major', labelsize=20)
    ax5.tick_params(axis='y', which='major', labelsize=16)
        
  #  ax6 = plt.subplot2grid((7,1), (5,0), rowspan=1, colspan=1)
  #  sns.swarmplot(x="variable", y="value", data=df6, hue='dataset', palette=["#87489D", "#32AAB5"], dodge=True, label='')
  #  sns.boxplot(data=df6, x="variable", y='value', hue='dataset', palette=["#E4CBF9", "#9AE1E1"], width=0.65)
  #  sns.despine(offset=5, trim=True)
  #  ax6.grid(True, linestyle='--')
  #  ax6.set_ylabel('150 mm', fontsize=17)
  #  ax6.set_xlabel('Season', fontsize=19)
  #  ax6.tick_params(axis='x', which='major', labelsize=16)
  #  ax6.tick_params(axis='y', which='major', labelsize=13)
    
    #legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, [handles[0],handles[1]]))
    ax5.legend(by_label.values(), by_label.keys(), title='', fontsize=22)


boxplot_many_thresh(df_5mm, df_15mm, df_25mm, df_50mm, df_80mm, df_150mm)
plt.savefig(f'{pathOut}/boxplot_TS_{period}_box60_{aggr}.png', bbox_inches="tight", dpi=300)


boxplot_many_thresh(df_5mm_pod, df_15mm_pod, df_25mm_pod, df_50mm_pod, df_80mm_pod, df_150mm_pod, score='POD')
plt.savefig(f'{pathOut}/boxplot_POD_{period}_box60_{aggr}.png', bbox_inches="tight", dpi=300)


boxplot_many_thresh(df_5mm_far, df_15mm_far, df_25mm_far, df_50mm_far, df_80mm_far, df_150mm_far, score='FAR')
plt.savefig(f'{pathOut}/boxplot_FAR_{period}_box60_{aggr}.png', bbox_inches="tight", dpi=300)
