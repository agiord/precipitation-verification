import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns
import matplotlib.ticker as mticker

"""
Script per il plotting degli score FAR (o SR), TS, POD:
    - in funzione della soglia di preci per il singolo anno
    - in funzione della soglia di preci aggregando su piu anni
    - in funzione della stagione (con e senza osservate)
e per il calcolo dell'ETS e paragone di ETS con TS    
"""

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ARCIS'

pathOut='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_ARCIS/box_60_max'


#plot for each year the score for the two reanalysis and for two separate seasons
def Scores_per_Thresh_per_Year(trance, year, season1, season2, s1_label, s2_label, score):

    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    scores_sphera_1 = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season1}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    scores_era5_1 = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season1}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    scores_sphera_2 = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season2}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    scores_era5_2 = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season2}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    S_1 = pd.DataFrame(index=scores_sphera_1.index, columns=['thr', 'ERA5_ts', 'SPHERA_ts', 'ERA5_pod', 'SPHERA_pod', 'ERA5_far', 'SPHERA_far'])
    S_2 = pd.DataFrame(index=scores_sphera_2.index, columns=['thr', 'ERA5_ts', 'SPHERA_ts', 'ERA5_pod', 'SPHERA_pod', 'ERA5_far', 'SPHERA_far'])
    
    S_1['thr'] = scores_sphera_1.thr
    S_1['ERA5_ts'] = scores_era5_1.ts.loc[scores_era5_1.ts != -999.900]
    S_1['SPHERA_ts'] = scores_sphera_1.ts.loc[scores_sphera_1.ts != -999.900]
    S_1['ERA5_pod'] = scores_era5_1.pod.loc[scores_era5_1.pod != -999.900]
    S_1['SPHERA_pod'] = scores_sphera_1.pod.loc[scores_sphera_1.pod != -999.900]
    S_1['ERA5_far'] = scores_era5_1.fa.loc[scores_era5_1.fa != -999.900]
    S_1['SPHERA_far'] = scores_sphera_1.fa.loc[scores_sphera_1.fa != -999.900]
    
    
    S_2['thr'] = scores_sphera_2.thr
    S_2['ERA5_ts'] = scores_era5_2.ts.loc[scores_era5_2.ts != -999.900]
    S_2['SPHERA_ts'] = scores_sphera_2.ts.loc[scores_sphera_2.ts != -999.900]
    S_2['ERA5_pod'] = scores_era5_2.pod.loc[scores_era5_2.pod != -999.900]
    S_2['SPHERA_pod'] = scores_sphera_2.pod.loc[scores_sphera_2.pod != -999.900]
    S_2['ERA5_far'] = scores_era5_2.fa.loc[scores_era5_2.fa != -999.900]
    S_2['SPHERA_far'] = scores_sphera_2.fa.loc[scores_sphera_2.fa != -999.900]    
    
    
    if score == 'TS':
        S1_sphera_score = S_1['SPHERA_ts']
        S1_era5_score = S_1['ERA5_ts']
        S2_sphera_score = S_2['SPHERA_ts']
        S2_era5_score = S_2['ERA5_ts']
        ylabel = 'Threat score'
        
    elif score == 'POD':
        S1_sphera_score = S_1['SPHERA_pod']
        S1_era5_score = S_1['ERA5_pod']
        S2_sphera_score = S_2['SPHERA_pod']
        S2_era5_score = S_2['ERA5_pod']
        ylabel = 'POD'
   
    elif score == 'FAR':
        S1_sphera_score = S_1['SPHERA_far']
        S2_era5_score = S_2['ERA5_far']
        ylabel = 'FAR'
        
    matplotlib.rcParams['xtick.minor.size'] = 0
    matplotlib.rcParams['xtick.minor.width'] = 0
    
    
    fig, ax = plt.subplots(figsize=(11,5))
    ax.set_xscale('log')
    ax.set_title(f'{year}', fontsize=17)
    ax.set_ylim([-0.05,1.05])
    
    ax.plot(S_1['thr'], S1_sphera_score, '-o',  markersize=8, color='red', label=f'{s1_label}')
    ax.plot(S_1['thr'], S1_era5_score, '--o',  markersize=8, mfc='none', color='red')
    
    ax.plot(S_2['thr'], S2_sphera_score, '-o',  markersize=8, color='blue', label=f'{s2_label}')
    ax.plot(S_2['thr'], S2_era5_score, '--o',  markersize=8, mfc='none', color='blue')
    
    ax.set_xticks(S_1['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    ax.set_xlabel('Precipitation (mm/day)', fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    legend = plt.legend(fontsize=15, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='best', fontsize=15)




trance='2003-2006'

year = '2005'

season1 = 'JJA05'
season2 = 'DJF05'

s1_label = 'Summer'
s2_label = 'Winter'

#decide the score to plot
#score = 'FAR'

for score in ['TS','FAR','POD']:
    
    Scores_per_Thresh_per_Year(trance, year, season1, season2, s1_label, s2_label, score)
    
    plt.savefig(f'{pathOut}/Scores_per_Thresh_perYear/{score}_{season1}_{season2}_{trance}.png', bbox_inches="tight")





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#as Scores_per_Thresh_per_Year but averaging over the trance
def Scores_per_Thresh(trance):

    if trance == '2003-2006':
        
        seasons = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
        
        winters = ['DJF03', 'DJF04', 'DJF05']
        summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06']
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06']
        falls = ['SON03', 'SON04', 'SON05', 'SON06']
        
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
           
    if trance == '2007-2010':
        
        seasons = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
        
        winters = ['DJF07', 'DJF08', 'DJF09']
        summers = ['JJA07', 'JJA08', 'JJA09', 'JJA10']
        springs = ['MAM07', 'MAM08', 'MAM09', 'MAM10']
        falls = ['SON07', 'SON08', 'SON09', 'SON10']
        
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
       
    if trance == '2011-2014':
        
        seasons = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  

        winters = ['DJF11', 'DJF12', 'DJF13']
        summers = ['JJA11', 'JJA12', 'JJA13', 'JJA14']
        springs = ['MAM11', 'MAM12', 'MAM13', 'MAM14']
        falls = ['SON11', 'SON12', 'SON13', 'SON14']
        
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
        
        
    if trance == '2015-2017':
        
        seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   


        winters = ['DJF15', 'DJF16']
        summers = ['JJA15', 'JJA16', 'JJA17']
        springs = ['MAM15', 'MAM16', 'MAM17']
        falls = ['SON15', 'SON16', 'SON17']
        
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
        
        
    sphera_seasonal_means = pd.DataFrame(index=scores_sphera[season].index, columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])
    era5_seasonal_means = pd.DataFrame(index=scores_era5[season].index, columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])    
    
    sphera_seasonal_means['thr'] = scores_sphera[season].thr
    era5_seasonal_means['thr'] = scores_era5[season].thr
    
    for list_of_seasons in [springs, summers, falls, winters]:
    
        temp_df_sphera = pd.DataFrame(index=scores_sphera[season].index, columns=list_of_seasons)
        temp_df_era5 = pd.DataFrame(index=scores_era5[season].index, columns=list_of_seasons)
        
        for season in list_of_seasons:
            temp_df_sphera[season] = pd.Series(scores_sphera[season].ts.loc[scores_sphera[season].ts != -999.900], name=season)
            temp_df_era5[season] = pd.Series(scores_era5[season].ts.loc[scores_era5[season].ts != -999.900], name=season)
            
        if list_of_seasons == springs:
            sphera_seasonal_means['ts_MAM'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_MAM'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == summers:
            sphera_seasonal_means['ts_JJA'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_JJA'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == falls:
            sphera_seasonal_means['ts_SON'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_SON'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == winters:
            sphera_seasonal_means['ts_DJF'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_DJF'] = temp_df_era5.mean(axis=1)            
        
                
    
        
    matplotlib.rcParams['xtick.minor.size'] = 0
    matplotlib.rcParams['xtick.minor.width'] = 0
    
    #DJF and JJA plot
    fig, ax = plt.subplots(figsize=(11,5))
    ax.set_xscale('log')
    ax.set_title(f'Average over {trance}', fontsize=17)
    ax.set_ylim([-0.05,1.05])
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_JJA'], '-o',  markersize=8, color='red', label='Summer')
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_JJA'], '--o',  markersize=8, mfc='none', color='red')
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_DJF'], '-o',  markersize=8, color='blue', label='Winter')
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_DJF'], '--o',  markersize=8, mfc='none', color='blue')
    
    ax.set_xticks(sphera_seasonal_means['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    ax.set_xlabel('Precipitation (mm/day)', fontsize=14)
    ax.set_ylabel('Threat Score', fontsize=14)
    legend = plt.legend(fontsize=15, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='best', fontsize=15)

    plt.savefig(f'{pathOut}/Scores_per_Thresh/TS_JJA_DJF_{trance}.png', bbox_inches="tight")


    #SON and MAM plot
    fig, ax = plt.subplots(figsize=(11,5))
    ax.set_xscale('log')
    ax.set_title(f'Average over {trance}', fontsize=17)
    ax.set_ylim([-0.05,1.05])
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_MAM'], '-o',  markersize=8, color='red', label='Spring')
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_MAM'], '--o',  markersize=8, mfc='none', color='red')
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_SON'], '-o',  markersize=8, color='blue', label='Fall')
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_SON'], '--o',  markersize=8, mfc='none', color='blue')
    
    ax.set_xticks(sphera_seasonal_means['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    ax.set_xlabel('Precipitation (mm/day)', fontsize=14)
    ax.set_ylabel('Threat Score', fontsize=14)
    legend = plt.legend(fontsize=15, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=8, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='best', fontsize=15)

    plt.savefig(f'{pathOut}/Scores_per_Thresh/TS_MAM_SON_{trance}.png', bbox_inches="tight")


trance='2011-2014'

Scores_per_Thresh(trance)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Scores_per_Thresh when considering all seasons and DEWETRA and ARCIS together:
"""

#decide wether max or mean in the box:
aggr='mean'

if aggr=='max':
    title_label='MAXIMUM'
elif aggr=='mean':
    title_label='MEAN'
    
obs_data='ARCIS'

if obs_data == 'DEWETRA':
    trance='2003-2017'
elif obs_data == 'ARCIS':
    trance='2003-2014'

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{obs_data}'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_{obs_data}/box60_{aggr}'

#as Scores_per_Thresh_per_Year but averaging over the trance
def Scores_per_Thresh(trance, aggr):

    if obs_data == 'DEWETRA':
        
        seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
        seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
        seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  
        seasons4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17'] 
        
        winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']
        summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14',
                   'JJA15', 'JJA16', 'JJA17']
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14',
                   'MAM15', 'MAM16', 'MAM17']
        falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14',
                 'SON15', 'SON16', 'SON17']
    
    elif obs_data == 'ARCIS':
        
        seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
        seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
        seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  
        
        winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13']
        summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14']
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14']
        falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14']
    
        
    scores_sphera = {}
    scores_era5 = {}
    
    for season in seasons1:
        scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    for season in seasons2:
        scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    for season in seasons3:
        scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
    if obs_data == 'DEWETRA':
        for season in seasons4:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2015-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2015-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            
    sphera_seasonal_means = pd.DataFrame(index=scores_sphera[season].index, columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])
    era5_seasonal_means = pd.DataFrame(index=scores_era5[season].index, columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF'])    
    
    sphera_seasonal_means['thr'] = scores_sphera[season].thr
    era5_seasonal_means['thr'] = scores_era5[season].thr
    
    for list_of_seasons in [springs, summers, falls, winters]:
    
        temp_df_sphera = pd.DataFrame(index=scores_sphera[season].index, columns=list_of_seasons)
        temp_df_era5 = pd.DataFrame(index=scores_era5[season].index, columns=list_of_seasons)
        
        for season in list_of_seasons:
            temp_df_sphera[season] = pd.Series(scores_sphera[season].ts.loc[scores_sphera[season].ts != -999.900], name=season)
            temp_df_era5[season] = pd.Series(scores_era5[season].ts.loc[scores_era5[season].ts != -999.900], name=season)
            
        if list_of_seasons == springs:
            sphera_seasonal_means['ts_MAM'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_MAM'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == summers:
            sphera_seasonal_means['ts_JJA'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_JJA'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == falls:
            sphera_seasonal_means['ts_SON'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_SON'] = temp_df_era5.mean(axis=1)
        elif list_of_seasons == winters:
            sphera_seasonal_means['ts_DJF'] = temp_df_sphera.mean(axis=1)
            era5_seasonal_means['ts_DJF'] = temp_df_era5.mean(axis=1)    
            
    #PLOT AGGREGATING ALL SEASONS TOGETHER:
    sphera_annual_means = pd.DataFrame(index=scores_sphera[season].index, columns=['thr', 'ts'])
    sphera_annual_means['thr'] = sphera_seasonal_means['thr']
    sphera_annual_means['ts'] = sphera_seasonal_means[['ts_MAM','ts_JJA','ts_SON','ts_DJF']].mean(axis=1)
            
    era5_annual_means = pd.DataFrame(index=scores_sphera[season].index, columns=['thr', 'ts'])
    era5_annual_means['thr'] = era5_seasonal_means['thr']
    era5_annual_means['ts'] = era5_seasonal_means[['ts_MAM','ts_JJA','ts_SON','ts_DJF']].mean(axis=1)
    
    
    matplotlib.rcParams['xtick.minor.size'] = 0
    matplotlib.rcParams['xtick.minor.width'] = 0
    
    #annual means plot
    fig, ax = plt.subplots(figsize=(8.5,4))
    ax.set_xscale('log')
    ax.set_title(r'$\bf{' + obs_data + '}$ (' + trance + ')', fontsize=19)  # using the {title_label} of the box', fontsize=17)
    ax.set_ylim([-0.05,0.7])
    
    ax.plot(sphera_annual_means['thr'][:7], sphera_annual_means['ts'][:7], '-o',  markersize=10, color='#7F000D', label='SPHERA',lw=2)
    ax.plot(era5_annual_means['thr'][:7], era5_annual_means['ts'][:7], '--o',  markersize=10, mfc='none', color='#023FA5',label='ERA5',lw=2)
    
    ax.set_xticks(sphera_annual_means['thr'][:7])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=19)
    ax.set_ylabel('Threat Score', fontsize=19)
    legend = plt.legend(fontsize=18, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    plt.savefig(f'{pathOut}/Scores_per_Thresh_MultiYear/TS_annual_{obs_data}_{trance}_Box60_{aggr}.pdf', bbox_inches="tight")
    
    #SEASONAL PLOTS:    
    #DJF and JJA plot
    fig, ax = plt.subplots(figsize=(8.5,4))
    ax.set_xscale('log')
    ax.set_title(r'$\bf{' + obs_data + '}$ (' + trance + ')', fontsize=19)  # using the {title_label} of the box', fontsize=17)
    ax.set_ylim([-0.05,0.7])
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_JJA'], '-o',  markersize=10, color='#7F000D', label='Summer',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_JJA'], '--o',  markersize=10, mfc='none', color='#7F000D',lw=2)
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_DJF'], '-o',  markersize=10, color='#023FA5', label='Winter',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_DJF'], '--o',  markersize=10, mfc='none', color='#023FA5',lw=2)
    
    ax.set_xticks(sphera_seasonal_means['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=19)
    ax.set_ylabel('Threat Score', fontsize=19)
    legend = plt.legend(fontsize=18, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='best', fontsize=18)

    plt.savefig(f'{pathOut}/Scores_per_Thresh_MultiYear/TS_JJA_DJF_{obs_data}_{trance}_Box60_{aggr}.pdf', bbox_inches="tight")


    #SON and MAM plot
    fig, ax = plt.subplots(figsize=(8.5,4))
    ax.set_xscale('log')
    ax.set_title(r'$\bf{' + obs_data + '}$ (' + trance + ')', fontsize=19)  # using the {title_label} of the box', fontsize=17)
    ax.set_ylim([-0.05,0.7])
    
    ax.plot(sphera_seasonal_means['thr'][:7], sphera_seasonal_means['ts_MAM'][:7], '-o',  markersize=10, color='#027C1E', label='Spring',lw=2)
    ax.plot(era5_seasonal_means['thr'][:7], era5_seasonal_means['ts_MAM'][:7], '--o',  markersize=10, mfc='none', color='#027C1E',lw=2)
    
    ax.plot(sphera_seasonal_means['thr'][:7], sphera_seasonal_means['ts_SON'][:7], '-o',  markersize=10, color='#E8853A', label='Fall',lw=2)
    ax.plot(era5_seasonal_means['thr'][:7], era5_seasonal_means['ts_SON'][:7], '--o',  markersize=10, mfc='none', color='#E8853A',lw=2)
    
    ax.set_xticks(sphera_seasonal_means['thr'][:7])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=19)
    ax.set_ylabel('Threat Score', fontsize=19)
    legend = plt.legend(fontsize=18, loc='lower left')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='best', fontsize=18)

    plt.savefig(f'{pathOut}/Scores_per_Thresh_MultiYear/TS_MAM_SON_{obs_data}_{trance}_Box60_{aggr}.pdf', bbox_inches="tight")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Scores_per_Thresh for multiple years together:
"""

dataset='DEWETRA'  #'DEWETRA'

aggr='mean'   #'max'

if dataset == 'ARCIS':
    all_seas_fold = 'all_seasons_2003-2014'
else:
    all_seas_fold = 'all_seasons_2003-2017'

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{dataset}'



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


pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_{dataset}/box60_{aggr}/Scores_per_Thresh_MultiYear'


df_1mm_max = df_seasons_thr(0,aggr)[1]
df_5mm_max = df_seasons_thr(1,aggr)[1]
df_10mm_max = df_seasons_thr(2,aggr)[1]
df_15mm_max = df_seasons_thr(3,aggr)[1]
df_25mm_max = df_seasons_thr(4,aggr)[1]
df_50mm_max = df_seasons_thr(5,aggr)[1]
df_80mm_max = df_seasons_thr(6,aggr)[1]
df_150mm_max = df_seasons_thr(7,aggr)[1]


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



matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['xtick.minor.width'] = 0

#DJF and JJA plot
fig, ax = plt.subplots(figsize=(7,4))
ax.set_xscale('log')
ax.set_title('Average TS vs daily rainfall thresholds, ' + r'$\bf{' + dataset + '}$ (2003-2014)' , fontsize=19)
ax.set_ylim([-0.05,0.75])
plt.locator_params(axis='y', nbins=7)

ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_JJA'], '-o',  markersize=10, color='#7F000D', label='Summer', lw=2)
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_JJA'], '--o',  markersize=10, mfc='none', color='#7F000D', lw=2)

ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_DJF'], '-o',  markersize=10, color='#023FA5', label='Winter', lw=2)
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_DJF'], '--o',  markersize=10, mfc='none', color='#023FA5', lw=2)

ax.set_xticks(sphera_seasonal_means_MAX['thr'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=19)
ax.set_ylabel('Threat Score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])

l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
           label='SPHERA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none', color='black', 
           label='ERA5', scaley=False)
leg = ax1.legend(handles=[l1,l2], loc='best', fontsize=18)

plt.savefig(f'{pathOut}/TS_JJA-DJF_2003-2014_{dataset}_{aggr}_2.pdf', bbox_inches="tight", dpi=300)




matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['xtick.minor.width'] = 0

#SON and MAM plot
fig, ax = plt.subplots(figsize=(7,4))
ax.set_xscale('log')
ax.set_title('Average TS vs daily rainfall thresholds, ' + r'$\bf{' + dataset + '}$ (2003-2014)' , fontsize=19)
ax.set_ylim([-0.05,0.7])

ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_MAM'], '-o',  markersize=10, color='#027C1E', label='Spring',lw=2)
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_MAM'], '--o',  markersize=10, mfc='none', color='#027C1E',lw=2)

ax.plot(sphera_seasonal_means_MAX['thr'], sphera_seasonal_means_MAX['ts_SON'], '-o',  markersize=10, color='#E8853A', label='Fall',lw=2)
ax.plot(era5_seasonal_means_MAX['thr'], era5_seasonal_means_MAX['ts_SON'], '--o',  markersize=10, mfc='none', color='#E8853A',lw=2)

ax.set_xticks(sphera_seasonal_means_MAX['thr'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=16)

ax.set_xlabel('Precipitation threshold (mm/day)', fontsize=19)
ax.set_ylabel('Threat Score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])

l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
           label='SPHERA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none', color='black', 
           label='ERA5', scaley=False)
leg = ax1.legend(handles=[l1,l2], loc='best', fontsize=18)

plt.savefig(f'{pathOut}/TS_MAM-SON_2003-2017_{dataset}_{aggr}_2.pdf', bbox_inches="tight", dpi=300)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def Scores_per_Time(trance, score, thresh):

    if trance == '2003-2006':
        
        seasons = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
      
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")    

    if trance == '2007-2010':
        
        seasons = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
      
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
       
    if trance == '2011-2014':
        
        seasons = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  

        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
        
        
    if trance == '2015-2017':
        
        seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")


    #extract for every threshold the scores for all the seasons using a nested dictionary of dataframes
    
    nested_dict = lambda: defaultdict(nested_dict)
    scores_per_thresh_sphera = nested_dict()
    scores_per_thresh_era5 = nested_dict()
    
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_sphera[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera[season].columns)
        scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5[season].columns)
        
        for season in seasons:
           scores_per_thresh_sphera[i_thresh].iloc[scores_per_thresh_sphera[i_thresh].index == season] = scores_sphera[season].iloc[[i_thresh]].values
           scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = scores_era5[season].iloc[[i_thresh]].values


    #dataframe of thresholds
    thresholds = pd.DataFrame(index=np.arange(0,8,1), columns=['thr'])
    thresholds['thr'] = [1,5,10,15,25,50,80,150]


    if score == 'FAR':
        sco = 'fa'
        ylabel = 'FAR'
        ylims = [-0.05, 1.05]
    elif score == 'POD':
        sco = 'pod'
        ylabel = 'POD'
        ylims = [-0.05, 1.05]
    elif score == 'TS':
        sco = 'ts'
        ylabel = 'Threat score'
        ylims = [-0.05, 0.65]

    #find the index of threhold based on the thresh parameter
    thr_index = int(thresholds.loc[thresholds['thr'] == thresh].index.values)


    fig, ax = plt.subplots(figsize=(13,4))
    ax.set_title(f'Precipitation larger than {thresh} mm/day, {trance}', fontsize=24)
    ax.set_ylim(ylims)
    
    ax.plot(scores_per_thresh_sphera[thr_index].index, scores_per_thresh_sphera[thr_index][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax.plot(scores_per_thresh_era5[thr_index].index, scores_per_thresh_era5[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax.tick_params(axis='both', which='major', labelsize=14)
        
    ax.set_xlabel('Season', fontsize=20)
    ax.set_ylabel(f'{ylabel}', fontsize=20)
    ax.legend(fontsize=18, loc='best')
    ax.grid(lw=0.5, linestyle='--')

    #set colors to individual grid lines and xticks labels depending on season
    grid_lines = ax.get_xgridlines()
    
    if trance != '2015-2017':
        for tick in [1,5,9,13]:
            ax.get_xticklabels()[tick].set_color("red")
            grid_lines[tick].set_color('red')
            grid_lines[tick].set_linewidth(1)
        for tick in [3,7,11]:
            ax.get_xticklabels()[tick].set_color("blue")
            grid_lines[tick].set_color('blue')
            grid_lines[tick].set_linewidth(1)
    else:
        for tick in [1,5,9]:
            ax.get_xticklabels()[tick].set_color("red")
            grid_lines[tick].set_color('red')
            grid_lines[tick].set_linewidth(1)
        for tick in [3,7]:
            ax.get_xticklabels()[tick].set_color("blue")
            grid_lines[tick].set_color('blue')
            grid_lines[tick].set_linewidth(1)
                


trance = '2011-2014'
score = 'TS'
#thresh = 50

for thresh in [15,25,50,80]:

    Scores_per_Time(trance, score, thresh)

    plt.savefig(f'{pathOut}/Scores_per_Time/{score}_{thresh}mm_{trance}.png', bbox_inches="tight")


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#as Scores_per_Time with boxplot of observed precipitation distributions x season
def Scores_per_Time_wOBS_distr(trance, score, thresh):
    
    if trance == '2003-2006':
        
        seasons = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
      
        scores_sphera = {}
        scores_era5 = {}
        obs_prec = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            obs_prec[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scatter_plot.dat",
                                       sep="\s+", usecols=['scad'])
            obs_prec[season] = obs_prec[season].rename(columns={"scad": "obs"})
    
    if trance == '2007-2010':
        
        seasons = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
      
        scores_sphera = {}
        scores_era5 = {}
        obs_prec = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            obs_prec[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scatter_plot.dat",
                                       sep="\s+", usecols=['scad'])
            obs_prec[season] = obs_prec[season].rename(columns={"scad": "obs"})
       
    if trance == '2011-2014':
        
        seasons = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  
    
        scores_sphera = {}
        scores_era5 = {}
        obs_prec = {}
         
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            obs_prec[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scatter_plot.dat",
                                       sep="\s+", usecols=['scad'])
            obs_prec[season] = obs_prec[season].rename(columns={"scad": "obs"})
        
        
    if trance == '2015-2017':
        
        seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   
    
        scores_sphera = {}
        scores_era5 = {}
        obs_prec = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5_box60/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            obs_prec[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/{trance}/{season}/scatter_plot.dat",
                                       sep="\s+", usecols=['scad'])
            obs_prec[season] = obs_prec[season].rename(columns={"scad": "obs"})
            
    #extract for every threshold the scores for the seasons selected for each trance using a nested dictionary of dataframes
    nested_dict = lambda: defaultdict(nested_dict)
    scores_per_thresh_sphera = nested_dict()
    scores_per_thresh_era5 = nested_dict()
    
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_sphera[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera[season].columns)
        scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5[season].columns)
        
        for season in seasons:
           scores_per_thresh_sphera[i_thresh].iloc[scores_per_thresh_sphera[i_thresh].index == season] = scores_sphera[season].iloc[[i_thresh]].values
           scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = scores_era5[season].iloc[[i_thresh]].values
    
    
    #dataframe of thresholds
    thresholds = pd.DataFrame(index=np.arange(0,8,1), columns=['thr'])
    thresholds['thr'] = [1,5,10,15,25,50,80,150]
    
    if score == 'FAR':
        sco = 'fa'
        ylabel = 'FAR'
        ylims = [-0.05, 1.05]
    elif score == 'POD':
        sco = 'pod'
        ylabel = 'POD'
        ylims = [-0.05, 1.05]
    elif score == 'TS':
        sco = 'ts'
        ylabel = 'Threat score'
        ylims = [-0.05, 0.65]
    
    #find the index of threhold based on the thresh parameter
    thr_index = int(thresholds.loc[thresholds['thr'] == thresh].index.values)
    
    
    
    #find longest set of observations within the seasons and take its length:
    def GetMaxFlow(flows):        
        maks=max(flows, key=lambda k: len(flows[k]))
        return len(flows[maks]), maks
    
    max_len = GetMaxFlow(obs_prec)[0]
    #create dataframe of observations with columns corresponding to seasons:
        
    df_obs_per_season = pd.DataFrame(index=np.arange(0,max_len,1), columns=seasons)
    for season in seasons:
        df_obs_per_season[season] = obs_prec[season]['obs']
        
        #clean out numeric non values from dataframes and convert every value to numeric:
        df_obs_per_season[season] = df_obs_per_season[season][pd.to_numeric(df_obs_per_season[season], errors='coerce').notnull()]
        df_obs_per_season[season] = pd.to_numeric(df_obs_per_season[season])
    
    #APPLY A FILTER TO AVOID THE LARGEST VALUES: WHICH CRITERIA SHOULD WE USE?????? for now keep values >0 and everything higher
    #BUT THERE ARE SOME VALUES VERY LARGE (ALMOST 1000 mm)
    
    df_obs_per_season_filt = pd.DataFrame(index=np.arange(0,max_len,1), columns=seasons)
    for season in seasons:
        df_obs_per_season_filt[season] = df_obs_per_season[season].loc[df_obs_per_season[season] > 0]#.loc[df_obs_per_season[season] < 1000]
    
    #melt data to use in seaborn boxplot:
    melted_df_obs_per_season_filt = pd.DataFrame(columns=['val','season'])
    for season in seasons:
        
        temp_df = pd.DataFrame(columns=['val','season'])
        temp_df['val'] = df_obs_per_season_filt[season]
        temp_df['season'] = pd.Series([season]*len(df_obs_per_season_filt[season]))
        
        melted_df_obs_per_season_filt = pd.concat([melted_df_obs_per_season_filt, temp_df], ignore_index=True)
    
    #PLOT
    fig, (ax1, ax2) = plt.subplots(2, 2, figsize=(13,8), dpi=100)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=3, colspan=1)
    ax1.set_title(f'Precipitation larger than {thresh} mm, {trance}', fontsize=17)
    ax1.set_ylim(ylims)
    
    ax1.plot(scores_per_thresh_sphera[thr_index].index, scores_per_thresh_sphera[thr_index][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax1.plot(scores_per_thresh_era5[thr_index].index, scores_per_thresh_era5[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax1.tick_params(axis='y', which='major', labelsize=12)
    ax1.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax1.set_ylabel(f'{ylabel}', fontsize=16)
    ax1.grid(lw=0.5, linestyle='--')
    ax1.legend(fontsize=15, loc='best')    
    
    
    ax2 = plt.subplot2grid((6,1), (3,0), rowspan=3, colspan=1, sharex=ax1)
    
    ax2.grid(lw=0.5, linestyle='--')
    ax2.tick_params(axis='both', which='major', labelsize=12)
    
    sns.set(style="ticks", palette="pastel")
    
    flierprops = dict(markerfacecolor='0.75', markersize=1,linestyle='none')
    sns.boxplot(x='season', y='val', data=melted_df_obs_per_season_filt, ax=ax2, width=0.65, whis=2, color='#D0EAF3',
                showfliers=True, showmeans=True, flierprops=flierprops)
    
    ax2.xaxis.grid(True)
    ax2.set_xlabel('Season', fontsize=16)
    ax2.set_ylabel('Observed prec. distribution', fontsize=16)
    
    
    plt.yscale('log')
    
    
    plt.subplots_adjust(hspace=0.0)
    
    
    #set colors to individual grid lines and xticks labels depending on season
    grid_lines1 = ax1.get_xgridlines()
    grid_lines2 = ax2.get_xgridlines()
    
    if trance != '2015-2017':
        for tick in [1,5,9,13]:
            ax1.get_xticklabels()[tick].set_color("red")
            ax2.get_xticklabels()[tick].set_color("red")
            grid_lines1[tick].set_color('red')
            grid_lines1[tick].set_linewidth(1)
            grid_lines2[tick].set_color('red')
            grid_lines2[tick].set_linewidth(1)
        for tick in [3,7,11]:
            ax1.get_xticklabels()[tick].set_color("blue")
            ax2.get_xticklabels()[tick].set_color("blue")
            grid_lines1[tick].set_color('blue')
            grid_lines1[tick].set_linewidth(1)
            grid_lines2[tick].set_color('blue')
            grid_lines2[tick].set_linewidth(1)
    else:
        for tick in [1,5,9]:
            ax1.get_xticklabels()[tick].set_color("red")
            ax2.get_xticklabels()[tick].set_color("red")
            grid_lines1[tick].set_color('red')
            grid_lines1[tick].set_linewidth(1)
            grid_lines2[tick].set_color('red')
            grid_lines2[tick].set_linewidth(1)
        for tick in [3,7]:
            ax1.get_xticklabels()[tick].set_color("blue")
            ax2.get_xticklabels()[tick].set_color("blue")
            grid_lines1[tick].set_color('blue')
            grid_lines1[tick].set_linewidth(1)
            grid_lines2[tick].set_color('blue')
            grid_lines2[tick].set_linewidth(1)
            
    

trance = '2015-2017'
score = 'TS'
thresh = 80

Scores_per_Time_wOBS_distr(trance, score, thresh)

plt.savefig(f'{pathOut}/Scores_per_Time_+OBS_distr/{score}_{thresh}mm_{trance}.png', bbox_inches="tight")



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



def Scores_per_Time_Season(seas, score, thresh):
    
       
    seasons_1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
               'DJF05', 'MAM06', 'JJA06', 'SON06']
  
    scores_sphera_1 = {}
    scores_era5_1 = {}
    obs_prec_1 = {}
    
    for season in seasons_1:
        scores_sphera_1[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_1[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_1[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2003-2006/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_1[season] = obs_prec_1[season].rename(columns={"scad": "obs"})



    seasons_2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
               'DJF09', 'MAM10', 'JJA10', 'SON10']
  
    scores_sphera_2 = {}
    scores_era5_2 = {}
    obs_prec_2 = {}
    
    for season in seasons_2:
        scores_sphera_2[season] = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/SPHERA/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_2[season] = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ERA5/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_2[season] = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/SPHERA/2007-2010/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_2[season] = obs_prec_2[season].rename(columns={"scad": "obs"})
       
   
    
    seasons_3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
               'DJF13', 'MAM14', 'JJA14', 'SON14']  

    scores_sphera_3 = {}
    scores_era5_3 = {}
    obs_prec_3 = {}
     
    for season in seasons_3:
        scores_sphera_3[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_3[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_3[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2011-2014/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_3[season] = obs_prec_3[season].rename(columns={"scad": "obs"})

    seasons_4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

    scores_sphera_4 = {}
    scores_era5_4 = {}
    obs_prec_4 = {}
    
    for season in seasons_4:
        scores_sphera_4[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2015-2017/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_4[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2015-2017/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_4[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2015-2017/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_4[season] = obs_prec_4[season].rename(columns={"scad": "obs"})
        
        
    
    if seas == 'Summers':
        
        seas_1 = ['JJA03', 'JJA04', 'JJA05', 'JJA06']
        seas_2 = ['JJA07', 'JJA08', 'JJA09', 'JJA10']
        seas_3 = ['JJA11', 'JJA12', 'JJA13', 'JJA14']
        seas_4 = ['JJA15', 'JJA16', 'JJA17']
        
    elif seas == 'Springs':
        
        seas_1 = ['MAM03', 'MAM04', 'MAM05', 'MAM06']
        seas_2 = ['MAM07', 'MAM08', 'MAM09', 'MAM10']
        seas_3 = ['MAM11', 'MAM12', 'MAM13', 'MAM14']
        seas_4 = ['MAM15', 'MAM16', 'MAM17']
        
    elif seas == 'Falls':
        
        seas_1 = ['SON03', 'SON04', 'SON05', 'SON06']
        seas_2 = ['SON07', 'SON08', 'SON09', 'SON10']
        seas_3 = ['SON11', 'SON12', 'SON13', 'SON14']
        seas_4 = ['SON15', 'SON16', 'SON17']
        
    elif seas == 'Winters':
        
        seas_1 = ['DJF03', 'DJF04', 'DJF05']
        seas_2 = ['DJF07', 'DJF08', 'DJF09']
        seas_3 = ['DJF11', 'DJF12', 'DJF13']
        seas_4 = ['DJF15', 'DJF16']
        
    
    all_scores_sphera = [scores_sphera_1,scores_sphera_2,scores_sphera_3,scores_sphera_4]
    all_scores_era5 = [scores_era5_1,scores_era5_2,scores_era5_3,scores_era5_4]

    all_seas = [seas_1,seas_2,seas_3,seas_4]
    all_seasons = np.concatenate([seas_1,seas_2,seas_3,seas_4])
        
    #extract for every threshold the scores for all the seasons using a nested dictionary of dataframes
    nested_dict = lambda: defaultdict(nested_dict)
    scores_per_thresh_sphera = nested_dict()
    scores_per_thresh_era5 = nested_dict()
    
    #loop for sphera
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_sphera[i_thresh] = pd.DataFrame(index=all_seasons, columns=scores_sphera_4[season].columns)
        
        for dataset, seasons in zip(all_scores_sphera, all_seas):
            #scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5[season].columns)
            
            for season in seasons:
                scores_per_thresh_sphera[i_thresh].iloc[scores_per_thresh_sphera[i_thresh].index == season] = dataset[season].iloc[[i_thresh]].values
            #scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = scores_era5[season].iloc[[i_thresh]].values
    
    
    #loop for era5
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=all_seasons, columns=scores_era5_4[season].columns)
        
        for dataset, seasons in zip(all_scores_era5, all_seas):
            
            for season in seasons:
                scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = dataset[season].iloc[[i_thresh]].values
    
    
    #dataframe of thresholds
    thresholds = pd.DataFrame(index=np.arange(0,8,1), columns=['thr'])
    thresholds['thr'] = [1,5,10,15,25,50,80,150]
    
    if score == 'FAR':
        sco = 'fa'
        ylabel = 'FAR'
        ylims = [-0.05, 1.05]
    elif score == 'POD':
        sco = 'pod'
        ylabel = 'POD'
        ylims = [-0.05, 1.05]
    elif score == 'TS':
        sco = 'ts'
        ylabel = 'Threat score'
        ylims = [-0.05, 0.65]
    
    #find the index of threhold based on the thresh parameter
    thr_index = int(thresholds.loc[thresholds['thr'] == thresh].index.values)
    
    
    #calculate seasonal prec cumulation:
    all_obs_prec = [obs_prec_1, obs_prec_2, obs_prec_3, obs_prec_4]
    
    df_cum_obs_per_season = pd.DataFrame(index = all_seasons, columns=['seas_cum', 'n_obs_data'])
    
    for dataset, seasons in zip(all_obs_prec, all_seas):
            
        for season in seasons:
                
            dataset[season]['obs'] = pd.to_numeric(dataset[season]['obs'], errors='coerce')
            df_cum_obs_per_season.loc[df_cum_obs_per_season.index == season,'seas_cum'] = np.sum(dataset[season]['obs'])
            df_cum_obs_per_season.loc[df_cum_obs_per_season.index == season,'n_obs_data'] = len(dataset[season]['obs'])
            
    #normalize observed prec with Nstations x Ndays = n available data:
    df_cum_obs_per_season['norm_seas_cum'] = df_cum_obs_per_season['seas_cum']/df_cum_obs_per_season['n_obs_data']    
        
            
    #PLOT
    fig, (ax1, ax2) = plt.subplots(2, 2, figsize=(14,7), dpi=100)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=3, colspan=1)
    ax1.set_title(f'Precipitation larger than {thresh} mm, {seas}', fontsize=17)
    ax1.set_ylim(ylims)
    
    ax1.plot(scores_per_thresh_sphera[thr_index].index, scores_per_thresh_sphera[thr_index][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax1.plot(scores_per_thresh_era5[thr_index].index, scores_per_thresh_era5[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax1.tick_params(axis='y', which='major', labelsize=12)
    ax1.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax1.set_ylabel(f'{ylabel}', fontsize=16)
    ax1.grid(lw=0.5, linestyle='--')
    ax1.legend(fontsize=15, loc='best')    
    
    
    ax2 = plt.subplot2grid((6,1), (3,0), rowspan=3, colspan=1, sharex=ax1)
    
    ax2.grid(lw=0.5, linestyle='--')
    ax2.tick_params(axis='both', which='major', labelsize=12)
    
    sns.set(style="ticks", palette="pastel")
    
    plt.bar(df_cum_obs_per_season.index, df_cum_obs_per_season['norm_seas_cum'], color ='lightseagreen', width = 0.4) 
    
    #f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
    #g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
    #plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

    
    #ax2.ticklabel_format(style='sci', axis='y', scilimits=(4,4), useMathText=True)
    ax2.xaxis.grid(True)
    ax2.set_xlabel('Season', fontsize=16)
    ax2.set_ylabel('Seasonal cum. prec. per \n N avail. obs. (mm/N obs)', fontsize=16)
    
    plt.subplots_adjust(hspace=0.0)
    
    #plt.yscale('log')
    
    
    
    
    
    
    
seas = 'Summers'
score = 'TS'
thresh = 50


Scores_per_Time_Season(seas, score, thresh)

plt.savefig(f'{pathOut}/Scores_per_Season/{score}_{thresh}mm_{seas}.png', bbox_inches="tight")










# same function but PLOT with many thresholds

def Scores_per_Time_Season_manyThresh(seas, score):
    
       
    seasons_1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
               'DJF05', 'MAM06', 'JJA06', 'SON06']
  
    scores_sphera_1 = {}
    scores_era5_1 = {}
    obs_prec_1 = {}
    
    for season in seasons_1:
        scores_sphera_1[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_1[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2003-2006/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_1[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2003-2006/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_1[season] = obs_prec_1[season].rename(columns={"scad": "obs"})



    seasons_2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
               'DJF09', 'MAM10', 'JJA10', 'SON10']
  
    scores_sphera_2 = {}
    scores_era5_2 = {}
    obs_prec_2 = {}
    
    for season in seasons_2:
        scores_sphera_2[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_2[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2007-2010/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_2[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2007-2010/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_2[season] = obs_prec_2[season].rename(columns={"scad": "obs"})
       
   
    
    seasons_3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
               'DJF13', 'MAM14', 'JJA14', 'SON14']  

    scores_sphera_3 = {}
    scores_era5_3 = {}
    obs_prec_3 = {}
     
    for season in seasons_3:
        scores_sphera_3[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_3[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2011-2014/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_3[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2011-2014/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_3[season] = obs_prec_3[season].rename(columns={"scad": "obs"})

    seasons_4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

    scores_sphera_4 = {}
    scores_era5_4 = {}
    obs_prec_4 = {}
    
    for season in seasons_4:
        scores_sphera_4[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2015-2017/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_4[season] = pd.read_csv(f"{pathIn}/ERA5_box60/2015-2017/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        obs_prec_4[season] = pd.read_csv(f"{pathIn}/SPHERA_box60/2015-2017/{season}/scatter_plot.dat",
                                   sep="\s+", usecols=['scad'])
        obs_prec_4[season] = obs_prec_4[season].rename(columns={"scad": "obs"})
        
        
    
    if seas == 'Summers':
        
        seas_1 = ['JJA03', 'JJA04', 'JJA05', 'JJA06']
        seas_2 = ['JJA07', 'JJA08', 'JJA09', 'JJA10']
        seas_3 = ['JJA11', 'JJA12', 'JJA13', 'JJA14']
        seas_4 = ['JJA15', 'JJA16', 'JJA17']
        
    elif seas == 'Springs':
        
        seas_1 = ['MAM03', 'MAM04', 'MAM05', 'MAM06']
        seas_2 = ['MAM07', 'MAM08', 'MAM09', 'MAM10']
        seas_3 = ['MAM11', 'MAM12', 'MAM13', 'MAM14']
        seas_4 = ['MAM15', 'MAM16', 'MAM17']
        
    elif seas == 'Falls':
        
        seas_1 = ['SON03', 'SON04', 'SON05', 'SON06']
        seas_2 = ['SON07', 'SON08', 'SON09', 'SON10']
        seas_3 = ['SON11', 'SON12', 'SON13', 'SON14']
        seas_4 = ['SON15', 'SON16', 'SON17']
        
    elif seas == 'Winters':
        
        seas_1 = ['DJF03', 'DJF04', 'DJF05']
        seas_2 = ['DJF07', 'DJF08', 'DJF09']
        seas_3 = ['DJF11', 'DJF12', 'DJF13']
        seas_4 = ['DJF15', 'DJF16']
        
    
    all_scores_sphera = [scores_sphera_1,scores_sphera_2,scores_sphera_3,scores_sphera_4]
    all_scores_era5 = [scores_era5_1,scores_era5_2,scores_era5_3,scores_era5_4]

    all_seas = [seas_1,seas_2,seas_3,seas_4]
    all_seasons = np.concatenate([seas_1,seas_2,seas_3,seas_4])
        
    #extract for every threshold the scores for all the seasons using a nested dictionary of dataframes
    nested_dict = lambda: defaultdict(nested_dict)
    scores_per_thresh_sphera = nested_dict()
    scores_per_thresh_era5 = nested_dict()
    
    #loop for sphera
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_sphera[i_thresh] = pd.DataFrame(index=all_seasons, columns=scores_sphera_4[season].columns)
        
        for dataset, seasons in zip(all_scores_sphera, all_seas):
            #scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5[season].columns)
            
            for season in seasons:
                scores_per_thresh_sphera[i_thresh].iloc[scores_per_thresh_sphera[i_thresh].index == season] = dataset[season].iloc[[i_thresh]].values
            #scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = scores_era5[season].iloc[[i_thresh]].values
    
    
    #loop for era5
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_era5[i_thresh] = pd.DataFrame(index=all_seasons, columns=scores_era5_4[season].columns)
        
        for dataset, seasons in zip(all_scores_era5, all_seas):
            
            for season in seasons:
                scores_per_thresh_era5[i_thresh].iloc[scores_per_thresh_era5[i_thresh].index == season] = dataset[season].iloc[[i_thresh]].values
    
    
    #dataframe of thresholds
    thresholds = pd.DataFrame(index=np.arange(0,8,1), columns=['thr'])
    thresholds['thr'] = [1,5,10,15,25,50,80,150]
    
    if score == 'FAR':
        sco = 'fa'
        tit_label = 'FAR'
        ylims = [-0.05, 1.05]
    elif score == 'POD':
        sco = 'pod'
        tit_label = 'POD'
        ylims = [-0.05, 1.05]
    elif score == 'TS':
        sco = 'ts'
        tit_label = 'threat'
        ylims = [-0.05, 0.65]
    
    #calculate seasonal prec cumulation:
    all_obs_prec = [obs_prec_1, obs_prec_2, obs_prec_3, obs_prec_4]
    
    df_cum_obs_per_season = pd.DataFrame(index = all_seasons, columns=['seas_cum', 'n_obs_data'])
    
    for dataset, seasons in zip(all_obs_prec, all_seas):
            
        for season in seasons:
                
            dataset[season]['obs'] = pd.to_numeric(dataset[season]['obs'], errors='coerce')
            df_cum_obs_per_season.loc[df_cum_obs_per_season.index == season,'seas_cum'] = np.sum(dataset[season]['obs'])
            df_cum_obs_per_season.loc[df_cum_obs_per_season.index == season,'n_obs_data'] = len(dataset[season]['obs'])
            
    #normalize observed prec with Nstations x Ndays = n available data:
    df_cum_obs_per_season['norm_seas_cum'] = df_cum_obs_per_season['seas_cum']/df_cum_obs_per_season['n_obs_data']    
        
    
            
    #PLOT
    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(13,15))  #, ax6
    
    fig.subplots_adjust(hspace=0.0)
    fig.suptitle(f'Seasonal {tit_label} score for different \n daily rainfall thresholds, {seas}', fontsize=26, y=0.93)
    
    
    ax1 = plt.subplot2grid((7,1), (0,0), rowspan=1, colspan=1)
    ax1.set_ylim(ylims)
    ax1.plot(scores_per_thresh_sphera[1].index, scores_per_thresh_sphera[1][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax1.plot(scores_per_thresh_era5[1].index, scores_per_thresh_era5[1][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax1.tick_params(axis='y', which='major', labelsize=12)
    ax1.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax1.set_ylabel(f'5 mm', fontsize=17)
    ax1.grid(lw=0.5, linestyle='--')
    ax1.legend(fontsize=20, loc='lower left')    
    
    
    ax2 = plt.subplot2grid((7,1), (1,0), rowspan=1, colspan=1)
    ax2.set_ylim(ylims)
    ax2.plot(scores_per_thresh_sphera[1].index, scores_per_thresh_sphera[3][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax2.plot(scores_per_thresh_era5[1].index, scores_per_thresh_era5[3][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax2.tick_params(axis='y', which='major', labelsize=12)
    ax2.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax2.set_ylabel(f'15 mm', fontsize=20)
    ax2.grid(lw=0.5, linestyle='--')
    #ax2.legend(fontsize=15, loc='best')    
    
    
    ax3 = plt.subplot2grid((7,1), (2,0), rowspan=1, colspan=1)
    ax3.set_ylim(ylims)
    ax3.plot(scores_per_thresh_sphera[1].index, scores_per_thresh_sphera[4][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax3.plot(scores_per_thresh_era5[1].index, scores_per_thresh_era5[4][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax3.tick_params(axis='y', which='major', labelsize=12)
    ax3.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax3.set_ylabel(f'25 mm', fontsize=20)
    ax3.grid(lw=0.5, linestyle='--')
    #ax2.legend(fontsize=15, loc='best')    
    
    
    ax4 = plt.subplot2grid((7,1), (3,0), rowspan=1, colspan=1)
    ax4.set_ylim(ylims)
    ax4.plot(scores_per_thresh_sphera[1].index, scores_per_thresh_sphera[5][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax4.plot(scores_per_thresh_era5[1].index, scores_per_thresh_era5[5][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax4.tick_params(axis='y', which='major', labelsize=12)
    ax4.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax4.set_ylabel(f'50 mm', fontsize=20)
    ax4.grid(lw=0.5, linestyle='--')
    #ax2.legend(fontsize=15, loc='best')   
    
    
    
    ax5 = plt.subplot2grid((7,1), (4,0), rowspan=1, colspan=1)
    ax5.set_ylim(ylims)
    ax5.plot(scores_per_thresh_sphera[1].index, scores_per_thresh_sphera[6][sco], '-o',  markersize=8, 
            color='black', label='SPHERA')
    ax5.plot(scores_per_thresh_era5[1].index, scores_per_thresh_era5[6][sco], '--o',  markersize=8,
            mfc='none', color='black', label='ERA5')
    
    ax5.tick_params(axis='y', which='major', labelsize=12)
    ax5.tick_params(axis='x', which='major', labelsize=0, length=0)
    ax5.set_ylabel(f'80 mm', fontsize=20)
    ax5.grid(lw=0.5, linestyle='--')
    #ax2.legend(fontsize=15, loc='best')  
    
    
    ax6 = plt.subplot2grid((7,1), (5,0), rowspan=2, colspan=1, sharex=ax1)
    
    ax6.grid(lw=0.5, linestyle='--')
    ax6.tick_params(axis='x', which='major', labelsize=16)
    ax6.tick_params(axis='y', which='major', labelsize=12)
    
    sns.set(style="ticks", palette="pastel")
    
    plt.bar(df_cum_obs_per_season.index, df_cum_obs_per_season['norm_seas_cum'], color ='lightseagreen', width = 0.4) 
    
    #f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
    #g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
    #plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

    
    #ax2.ticklabel_format(style='sci', axis='y', scilimits=(4,4), useMathText=True)
    ax6.xaxis.grid(True)
    ax6.set_xlabel('Season', fontsize=22)
    ax6.set_ylabel('Seasonal cum. prec. per \n N avail. obs. (mm/Nobs)', fontsize=18)
    
    



seas = 'Summers'
#score = 'POD'

for score in ['POD','FAR','TS']:
    
    Scores_per_Time_Season_manyThresh(seas, score)
    
    plt.savefig(f'{pathOut}/Scores_per_Season_manyThresh/{score}_{seas}.png', bbox_inches="tight")









""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#calculate ETS and gives as output a pd dataframe per reanalysis with ts and ets 
def ETS(trance, season):

    scores_sphera = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/SPHERA/{trance}/{season}/scores_per_scad.dat",
                                   skiprows=4, sep="\s+")
    
    scores_era5 = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ERA5/{trance}/{season}/scores_per_scad.dat",
                                   skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/SPHERA/{trance}/{season}/cont_table_mod.dat",
                               skiprows=-1, sep="\s+")
    
    cont_era5 = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ERA5/{trance}/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    
    ts_vs_ets_sphera = pd.DataFrame(index = scores_sphera.index, columns=['thr', 'ts', 'ets'])
    ts_vs_ets_sphera['thr'] = scores_sphera['thr']
    ts_vs_ets_sphera['ts'] = scores_sphera['ts']
    
    ts_vs_ets_era5 = pd.DataFrame(index = scores_era5.index, columns=['thr', 'ts', 'ets'])
    ts_vs_ets_era5['thr'] = scores_era5['thr']
    ts_vs_ets_era5['ts'] = scores_era5['ts']
    
    #SIAMO SICURI CHE QUESTO SIA n=tot number of forecast???
    #tot_fcst_sphera = sum(scores_sphera['nos'])
    #tot_fcst_era5 = sum(scores_era5['nos'])
    
    #n dovrebbe essere nella cont table: n=a+b+c+d quindi lo calcoliamo nel ciclo ogni volta:
        
    
    #Calculate ETS for each threshold
    i = 0
    for thresh in list(ts_vs_ets_sphera['thr']):
            
            tot_fcst_sphera = cont_sphera['1'][i] + cont_sphera['0'][i] + cont_sphera['1'][i+1] + cont_sphera['0'][i+1]
            hits_random_sphera = ((cont_sphera['1'][i] + cont_sphera['0'][i]) * (cont_sphera['1'][i] + cont_sphera['1'][i+1])) / tot_fcst_sphera
            ets_sphera = (cont_sphera['1'][i] - hits_random_sphera) / (cont_sphera['1'][i] + cont_sphera['0'][i] + cont_sphera['1'][i+1] - hits_random_sphera)
            ts_vs_ets_sphera['ets'].loc[ts_vs_ets_sphera['thr'] == thresh] = ets_sphera
            
            if i < len(cont_era5):
               
                tot_fcst_era5 = cont_era5['1'][i] + cont_era5['0'][i] + cont_era5['1'][i+1] + cont_era5['0'][i+1]
                hits_random_era5 = ((cont_era5['1'][i] + cont_era5['0'][i]) * (cont_era5['1'][i] + cont_era5['1'][i+1])) / tot_fcst_era5
                ets_era5 = (cont_era5['1'][i] - hits_random_era5) / (cont_era5['1'][i] + cont_era5['0'][i] + cont_era5['1'][i+1] - hits_random_era5)
                ts_vs_ets_era5['ets'].loc[ts_vs_ets_era5['thr'] == thresh] = ets_era5
            
            else:
                
                ts_vs_ets_era5['ets'].loc[ts_vs_ets_era5['thr'] == thresh] = np.NaN
            
            #substitute values of TS -999.90 with Nan:
            if  ts_vs_ets_era5['ts'].loc[ts_vs_ets_era5['thr'] == thresh].values ==  -999.900:
                ts_vs_ets_era5['ts'].loc[ts_vs_ets_era5['thr'] == thresh] = np.NaN
            
            i = i + 3
            
    return ts_vs_ets_sphera, ts_vs_ets_era5


def ETS_vs_TS_plot(trance, season):

    ets_ts_sphera = ETS(trance, season)[0]
    ets_ts_era5 = ETS(trance, season)[1]    


    fig, ax = plt.subplots(figsize=(11,5))
    ax.set_xscale('log')
    ax.set_title(f'{season}, {trance}', fontsize=17)
    ax.set_ylim([-0.05,1.05])
    
    ax.plot(ets_ts_sphera['thr'], ets_ts_sphera['ets'], '-o',  markersize=8, color='#0095AF', label='SPHERA')
    ax.plot(ets_ts_era5['thr'], ets_ts_era5['ets'], '-o',  markersize=8, color='#B5456F', label='ERA5')
    
    ax.plot(ets_ts_sphera['thr'], ets_ts_sphera['ts'], '--o',  markersize=8, mfc='none', color='#0095AF')
    ax.plot(ets_ts_era5['thr'], ets_ts_era5['ts'], '--o',  markersize=8, mfc='none', color='#B5456F')
    
    ax.set_xticks(ets_ts_sphera['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    ax.set_xlabel('Precipitation (mm/day)', fontsize=14)
    ax.set_ylabel('Equitable threat score / Threat score', fontsize=14)
    legend = plt.legend(fontsize=15, loc='best')
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot([1,1], [1.5,2], '-o',  markersize=8, color='black', 
                       label='ETS',scaley=False)
    l2, = ax1.plot([1,1], [1.5,2], '--o', markersize=8, mfc='none', color='black', 
                       label='TS', scaley=False)
    ax1.legend(handles=[l1,l2], loc='upper left', fontsize=15)



trance = '2003-2006'
season = '2003-2006_complete'

for season in ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']:  
    
    ETS_vs_TS_plot(trance, season)
    
    plt.savefig(f'/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/ETS_vs_TS/ETSvTS_{season}_{trance}.png', bbox_inches="tight")



