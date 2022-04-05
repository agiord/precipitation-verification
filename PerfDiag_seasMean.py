import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns

import rpy2.robjects as ro
import rpy2.robjects.packages as r

import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()

#import verification library from R
ver = ro.packages.importr("verification")

#Script per fare perf diagram aggregando su stagioni e anni

dataset='DEWETRA'  #'DEWETRA'
aggr='max' 




pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{dataset}'

springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14', 'MAM15', 'MAM16', 'MAM17']
summers = ['JJA04', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14', 'JJA15', 'JJA16', 'JJA17']
falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14', 'SON15', 'SON16', 'SON17']
winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']

years = ['2003','2004','2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']

MAM_sphera = {}
MAM_era5 = {}

JJA_sphera = {}
JJA_era5 = {}

SON_sphera = {}
SON_era5 = {}

DJF_sphera = {}
DJF_era5 = {}


for season in springs:
    
    MAM_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")
    MAM_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")

for season in summers:
    
    JJA_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")
    JJA_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")

for season in falls:
    
    SON_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")
    SON_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")

for season in winters:
    
    DJF_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")
    DJF_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                       skiprows=4, sep="\s+")
    
def build_scores_df(thr_ind):
    #build dictionary to contain 3 dataframes relative to the three scores, which contain all the values
    #at a certain threshold for all the seasons and the two reanalysis:
    df_seasons = {} 
    
    df_seasons['ts'] = pd.DataFrame(index=np.arange(0,2*len(MAM_sphera),1) ,columns=['MAM', 'JJA', 'SON', 'DJF', 'year', 'dataset'])
    df_seasons['pod'] = pd.DataFrame(index=np.arange(0,2*len(MAM_sphera),1) ,columns=['MAM', 'JJA', 'SON', 'DJF', 'year', 'dataset'])
    df_seasons['fa'] = pd.DataFrame(index=np.arange(0,2*len(MAM_sphera),1) ,columns=['MAM', 'JJA', 'SON', 'DJF', 'year', 'dataset'])
    
    for score in ['ts','pod','fa']:
        for ind in df_seasons[score].index[1::2]:    
            df_seasons[score]['dataset'][ind] = 'ERA5'
            df_seasons[score]['dataset'][ind-1] = 'SPHERA'
            
        for i,j in zip(df_seasons[score].index[0::2], np.arange(0,len(years),1)):
            df_seasons[score]['year'][i] = years[j]
            df_seasons[score]['year'][i+1] = years[j]
        
        for ind, s_ind in zip(df_seasons[score].index[1::2], np.arange(0,len(springs),1)):
            df_seasons[score]['MAM'][ind] = MAM_era5[springs[s_ind]][score][thr_ind]
            df_seasons[score]['MAM'][ind-1] = MAM_sphera[springs[s_ind]][score][thr_ind]
            
            df_seasons[score]['JJA'][ind] = JJA_era5[summers[s_ind]][score][thr_ind]
            df_seasons[score]['JJA'][ind-1] = JJA_sphera[summers[s_ind]][score][thr_ind]
            
            df_seasons[score]['SON'][ind] = SON_era5[falls[s_ind]][score][thr_ind]
            df_seasons[score]['SON'][ind-1] = SON_sphera[falls[s_ind]][score][thr_ind]
        
        #winters for SPHERA
        j=0
        for i in df_seasons[score].index[0::2]:
            if (df_seasons[score]['year'][i] == '2006' or df_seasons[score]['year'][i] == '2010' or df_seasons[score]['year'][i] == '2014' or df_seasons[score]['year'][i] == '2017'):
                df_seasons[score]['DJF'][i] = np.nan
                continue
            else:
                df_seasons[score]['DJF'][i] = DJF_sphera[winters[j]][score][thr_ind]
                j=j+1
        
        #winters for ERA5
        j=0
        for i in df_seasons[score].index[1::2]:
            if (df_seasons[score]['year'][i] == '2006' or df_seasons[score]['year'][i] == '2010' or df_seasons[score]['year'][i] == '2014' or df_seasons[score]['year'][i] == '2017'):
                df_seasons[score]['DJF'][i] = np.nan
                continue
            else:
                df_seasons[score]['DJF'][i] = DJF_era5[winters[j]][score][thr_ind]
                j=j+1
                
        #check for -999.9 values and substitute with np.nan
        for seas in ['MAM','JJA', 'SON', 'DJF']:
            for i in df_seasons[score].index:
                if df_seasons[score][seas][i] == -999.9:
                    df_seasons[score][seas][i] = np.nan
       
    return df_seasons

#build a dictionary containing the dictionaries of the scores for all the thresholds considered
df_all_thresh = {}
thresholds = [1,5,10,15,25,50,80,150]  #150

for thr_ind in np.arange(0,8,1):   #(0,8,1)
    
    df_all_thresh[thresholds[thr_ind]] = build_scores_df(thr_ind)
    
    
#dictionary containing average values of scores over the years


df_avg = {}
for thr_ind in np.arange(0,8,1):    #8
    df_avg[thresholds[thr_ind]] = {}
    
    for score in ['fa','pod','ts']:
        
        df_avg[thresholds[thr_ind]][score] = pd.DataFrame(index=[0,1] ,columns=['MAM', 'JJA', 'SON', 'DJF', 'dataset'])
        df_avg[thresholds[thr_ind]][score]['dataset'][0] = 'SPHERA'
        df_avg[thresholds[thr_ind]][score]['dataset'][1] = 'ERA5'
        
        for season in ['MAM', 'JJA', 'SON', 'DJF']:
            
            df_all_vals = df_all_thresh[thresholds[thr_ind]][score]
            
            #per sphera
            df_avg[thresholds[thr_ind]][score][season][0] = np.nanmean(df_all_vals.loc[df_all_vals['dataset'] == 'SPHERA'][season])
            
            #per era5
            if df_all_vals.loc[df_all_vals['dataset'] == 'ERA5'][season].isnull().all() == False:
                df_avg[thresholds[thr_ind]][score][season][1] = np.nanmean(df_all_vals.loc[df_all_vals['dataset'] == 'ERA5'][season])
            else:
                df_avg[thresholds[thr_ind]][score][season][1] = np.nan
        
        df_avg[thresholds[thr_ind]][score]['AVG'] = df_avg[thresholds[thr_ind]][score][['MAM','JJA','SON','DJF']].mean(axis=1)
        
        
""""""""""""""""""""""""""""" 
PERF DIAGRAM A PARTIRE DALLE CONT TABLE
""""""""""""""""""""""""""""   


pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/DEWETRA'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_DEWETRA/PerfDiagrams'

springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14', 'MAM15', 'MAM16', 'MAM17']
summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14', 'JJA15', 'JJA16', 'JJA17']
falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14', 'SON15', 'SON16', 'SON17']
winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']

cont_sphera = {}
cont_era5 = {}

#upload contingency tables and extract them for each threshold   
for season in springs + summers + falls + winters:

    cont_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")

#sum cont tables over all seasons:
cont_seas_sums_sphera = {}
cont_seas_sums_era5 = {}

all_seas = [springs,summers,falls,winters]

#inizializzare i df vuoti
for season in ['MAM','JJA','SON','DJF']:
    cont_seas_sums_sphera[season] = pd.DataFrame(index=np.arange(0,23,1),columns=['0','1'])    
    cont_seas_sums_era5[season] = pd.DataFrame(index=np.arange(0,23,1),columns=['0','1'])

for seasons in [springs, summers, falls, winters]:
    
    if seasons == springs:
        ss = 'MAM'
    elif seasons == summers:
        ss = 'JJA'
    elif seasons == falls:
        ss = 'SON'
    else:
        ss = 'DJF'
    
    for seas in seasons:
        
        temp_sphera = cont_seas_sums_sphera[ss]
        temp_era5 = cont_seas_sums_era5[ss]
    
        cont_seas_sums_sphera[ss] = temp_sphera.add(cont_sphera[seas], fill_value=0)
        cont_seas_sums_sphera[ss] = cont_seas_sums_sphera[ss][cont_seas_sums_sphera[ss].columns[::-1]]
            
        cont_seas_sums_era5[ss] = temp_era5.add(cont_era5[seas], fill_value=0)
        cont_seas_sums_era5[ss] = cont_seas_sums_era5[ss][cont_seas_sums_era5[ss].columns[::-1]]
        
    cont_seas_sums_sphera[ss] = cont_seas_sums_sphera[ss].where(pd.notnull(cont_seas_sums_sphera[ss]), None)
    cont_seas_sums_era5[ss] = cont_seas_sums_era5[ss].where(pd.notnull(cont_seas_sums_era5[ss]), None)
    
    
cont_seas_sums = {}
cont_seas_sums['SPHERA'] = cont_seas_sums_sphera
cont_seas_sums['ERA5'] = cont_seas_sums_era5

#cont tables aggregating all seasons together
cont_all_sums = {}
cont_all_sums['SPHERA'] = pd.DataFrame(index=np.arange(0,23,1),columns=['0','1'])    
cont_all_sums['ERA5'] = pd.DataFrame(index=np.arange(0,23,1),columns=['0','1'])

#NON FUNZIONA BENE; FARE A MANO
for seas in ['MAM','JJA','SON','DJF']:
    temp_s = cont_all_sums['SPHERA']
    temp_e = cont_all_sums['ERA5']

    cont_all_sums['SPHERA'] = temp_s.add(cont_seas_sums_sphera[seas], fill_value=0)
    cont_all_sums['ERA5'] = temp_s.add(cont_seas_sums_era5[seas], fill_value=0)

    #cont_all_sums['SPHERA'] =  cont_all_sums['SPHERA'][ cont_all_sums['SPHERA'].columns[::-1]]
    #cont_all_sums['ERA5'] =  cont_all_sums['ERA5'][ cont_all_sums['ERA5'].columns[::-1]]
        
    cont_all_sums['SPHERA'] = cont_all_sums['SPHERA'].where(pd.notnull(cont_all_sums['SPHERA']), None)
    cont_all_sums['ERA5'] = cont_all_sums['ERA5'].where(pd.notnull(cont_all_sums['ERA5']), None)



#SET THE SEASON TO PLOT:
season='AVG'

def PerformanceDiagram(season):
    
    #plot perf diag
    plt.figure(figsize=(10, 7))
    grid_ticks = np.arange(0, 1.01, 0.01)
    sr_g, pod_g = np.meshgrid(grid_ticks, grid_ticks)
    bias = pod_g / sr_g
    csi = 1.0 / (1.0 / sr_g + 1.0 / pod_g - 1.0)
    csi_contour = plt.contourf(sr_g, pod_g, csi, np.arange(0.1, 1.1, 0.1), extend="max", cmap='Greys')
    b_contour = plt.contour(sr_g, pod_g, bias, [0.3, 0.5, 0.8, 1, 1.3, 1.5, 2, 4], colors="k", linestyles="dashed", linewidths=0.5)
    plt.clabel(b_contour, fmt="%1.1f", manual=[(0.23, 0.95), (0.43, 0.95), (0.63, 0.95), (0.72,0.95), (0.8, 0.8), (0.85, 0.67), (0.9, 0.45), (0.75,0.22)])
    
    markers = itertools.cycle(['o','^','s','D','h','8','v','p']) 
       
    for thr_ind in np.arange(0,8,1):   #8
        
        marker = next(markers)
        
        colors = itertools.cycle(['#87489D', '#32AAB5',]) 
        
        ct_rean = {}
        cont_vec = {}
        m = {}
        bootstrap = {}
        error_bars = {}
        x = {}
        y = {}
        yerr = {}
        xerr = {}
        
        for rean in ['SPHERA', 'ERA5']:   #[15,25,35,45,60,100,200]:
            
            color = next(colors)
            
            #cont_sphera[f'{box}'] = cont_sphera[f'{box}'].fillna(0)
    
            if (thr_ind == 0):
                ct_rean[rean] = cont_all_sums[rean].loc[0:1] # cont_seas_sums[rean][season].loc[0:1]
                aaa = cont_all_sums[rean].loc[0:1]['0'][0]  #cont_seas_sums[rean][season].loc[0:1]['0'][0]
            elif (thr_ind == 1):
                ct_rean[rean] = cont_all_sums[rean].loc[3:4]  #cont_seas_sums[rean][season].loc[3:4] 
                aaa = cont_all_sums[rean].loc[3:4]['0'][3] #cont_seas_sums[rean][season].loc[3:4]['0'][3]
            elif (thr_ind == 2):
                ct_rean[rean] = cont_all_sums[rean].loc[6:7]  #cont_seas_sums[rean][season].loc[6:7]  
                aaa = cont_all_sums[rean].loc[6:7]['0'][6]   #cont_seas_sums[rean][season].loc[6:7]['0'][6]
            elif (thr_ind == 3):
                ct_rean[rean] = cont_all_sums[rean].loc[9:10]   #cont_seas_sums[rean][season].loc[9:10] 
                aaa = cont_all_sums[rean].loc[9:10]['0'][9]   #cont_seas_sums[rean][season].loc[9:10]['0'][9]
            elif (thr_ind == 4):
                ct_rean[rean] = cont_all_sums[rean].loc[12:13]   #cont_seas_sums[rean][season].loc[12:13]  
                aaa = cont_all_sums[rean].loc[12:13]['0'][12]   #cont_seas_sums[rean][season].loc[12:13]['0'][12]
            elif (thr_ind == 5):
                ct_rean[rean] = cont_all_sums[rean].loc[15:16]   #cont_seas_sums[rean][season].loc[15:16]  
                aaa = cont_all_sums[rean].loc[15:16]['0'][15]  # cont_seas_sums[rean][season].loc[15:16]['0'][15]
            elif (thr_ind == 6):
                ct_rean[rean] = cont_all_sums[rean].loc[18:19]  #cont_seas_sums[rean][season].loc[18:19]  
                aaa = cont_all_sums[rean].loc[18:19]['0'][18]   #cont_seas_sums[rean][season].loc[18:19]['0'][18]
            elif (thr_ind == 7) :
                ct_rean[rean] = cont_all_sums[rean].loc[21:22]   #cont_seas_sums[rean][season].loc[21:22] 
                aaa = cont_all_sums[rean].loc[21:22]['0'][21]   #cont_seas_sums[rean][season].loc[21:22]['0'][21]
            
            if aaa != None:
                    
                #read the contingency table as R matrix
                cont_vec[rean] = ro.IntVector([int(ct_rean[rean].iloc[0,0]),int(ct_rean[rean].iloc[1,0]),
                                         int(ct_rean[rean].iloc[0,1]),int(ct_rean[rean].iloc[1,1])])
                m[rean] = ro.r.matrix(cont_vec[rean],nrow=2, ncol = 2)
                
                #apply bootstrap resampling to the contingency table to calculate the confidence intervals of POD and FAR 
                boot = ro.r('table.stats.boot')
                bootstrap[rean] = boot(m[rean], R=1000)
                        
                #extract values from R bootstrap function to save in a pd.DataFrame
                error_bars[rean] = pd.DataFrame(columns=['pod','sr'])
                
                error_bars[rean].loc[0,'pod'] = bootstrap[rean][0]
                error_bars[rean].loc[1,'pod'] = bootstrap[rean][1]
                error_bars[rean].loc[0,'sr'] = 1-bootstrap[rean][3]
                error_bars[rean].loc[1,'sr'] = 1-bootstrap[rean][2]
                
                #plot value with errorbars
                x[rean] = 1 - df_avg[thresholds[thr_ind]]['fa'].loc[df_avg[thresholds[thr_ind]]['fa']['dataset'] == rean][season]
                y[rean] = df_avg[thresholds[thr_ind]]['pod'].loc[df_avg[thresholds[thr_ind]]['pod']['dataset'] == rean][season]  
                yerr[rean] = [[float(y[rean] - error_bars[rean].loc[1,'pod'])],
                                  [float(error_bars[rean].loc[0,'pod'] - y[rean])]]
                xerr[rean] = [[float(x[rean] - error_bars[rean].loc[1,'sr'])],
                                  [float(error_bars[rean].loc[0,'sr'] - x[rean])]]
                
                 
                if rean == 'SPHERA':
                    label_thr = int(thresholds[thr_ind])
                    label = f'{label_thr}'
                else:
                    label = ''
                
                plt.errorbar(x[rean], y[rean], yerr = yerr[rean], xerr = xerr[rean],  marker=marker, markersize=12, 
                             color=color, linestyle='', label=label)
           
    cbar = plt.colorbar(csi_contour)
    cbar.ax.tick_params(labelsize=14) 
    cbar.set_label('Threat Score (TS)', fontsize=17)
    plt.xlabel('Success Ratio (1-FAR)', fontsize=17)
    plt.ylabel('Probability of detection (POD)', fontsize=17)
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    #plt.title(f' {seas} average over 2015-2017', fontsize=20)#, fontweight="bold")
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.text(0.67,0.57,"Frequency Bias",fontdict=dict(fontsize=15, rotation=37))
    
    legend = plt.legend(title='Threshold \n [mm/day]', **dict(loc='best', fontsize=15, framealpha=0.75, frameon=True))
    plt.setp(legend.get_title(),fontsize=15)
    ax = plt.gca().add_artist(legend)
    
    #legenda per le due diverse rianalisi
    l1, = plt.plot(1 - df_avg[thresholds[6]]['fa'].loc[df_avg[thresholds[6]]['fa']['dataset'] == rean][season], 
                   df_avg[thresholds[6]]['pod'].loc[df_avg[thresholds[6]]['pod']['dataset'] == rean][season], linestyle='', marker='o', 
                   markersize=12, color='#87489D', label='SPHERA')
    l2, = plt.plot(1 - df_avg[thresholds[6]]['fa'].loc[df_avg[thresholds[6]]['fa']['dataset'] == rean][season], 
                   df_avg[thresholds[6]]['pod'].loc[df_avg[thresholds[6]]['pod']['dataset'] == rean][season], linestyle='', marker='o', 
                   markersize=12, color='#32AAB5', label='ERA5')
    
    leg2 = plt.legend(handles=[l1,l2], loc='best', fontsize=15)
    plt.setp(leg2.get_title(),fontsize=17)
    
    plt.savefig(f'{pathOut}/perfDiag_box60Max_ALL.pdf', bbox_inches='tight')   #{season}

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    