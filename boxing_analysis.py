import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns
import matplotlib.ticker as mticker

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/boxing_analysis'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_DEWETRA/Boxing_analysis'

#as Scores_per_Thresh_per_Year but averaging over the trance
def Scores_per_Time_box(score, thresh):

    trance = '2015-2017'
        
    seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

    scores_sphera_box15 = {}
    scores_sphera_box25 = {}
    scores_sphera_box35 = {}
    scores_sphera_box45 = {}
    scores_sphera_box60 = {}
    scores_sphera_box100 = {}
    scores_sphera_box200 = {}
    
    scores_era5_box25 = {}
    scores_era5_box35 = {}
    scores_era5_box45 = {}
    scores_era5_box60 = {}
    scores_era5_box100 = {}
    scores_era5_box200 = {}
    
    for season in seasons:
        
        scores_sphera_box15[season] = pd.read_csv(f"{pathIn}/SPHERA/box15/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        
        
        scores_sphera_box25[season] = pd.read_csv(f"{pathIn}/SPHERA/box25/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box25[season] = pd.read_csv(f"{pathIn}/ERA5/box25/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")

        scores_sphera_box35[season] = pd.read_csv(f"{pathIn}/SPHERA/box35/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box35[season] = pd.read_csv(f"{pathIn}/ERA5/box35/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")

        scores_sphera_box45[season] = pd.read_csv(f"{pathIn}/SPHERA/box45/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box45[season] = pd.read_csv(f"{pathIn}/ERA5/box45/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        
        scores_sphera_box60[season] = pd.read_csv(f"{pathIn}/SPHERA/box60/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box60[season] = pd.read_csv(f"{pathIn}/ERA5/box60/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")

        scores_sphera_box100[season] = pd.read_csv(f"{pathIn}/SPHERA/box100/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box100[season] = pd.read_csv(f"{pathIn}/ERA5/box100/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        
        scores_sphera_box200[season] = pd.read_csv(f"{pathIn}/SPHERA/box200/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")
        scores_era5_box200[season] = pd.read_csv(f"{pathIn}/ERA5/box200/{season}/scores_per_scad.dat",
                           skiprows=4, sep="\s+")

    #extract for every threshold the scores for all the seasons using a nested dictionary of dataframes
    
    nested_dict = lambda: defaultdict(nested_dict)

    scores_per_thresh_sphera_box15 = nested_dict()

    
    scores_per_thresh_sphera_box25 = nested_dict()
    scores_per_thresh_era5_box25 = nested_dict()
    
    scores_per_thresh_sphera_box35 = nested_dict()
    scores_per_thresh_era5_box35 = nested_dict()
    
    scores_per_thresh_sphera_box45 = nested_dict()
    scores_per_thresh_era5_box45 = nested_dict()
    
    scores_per_thresh_sphera_box60 = nested_dict()
    scores_per_thresh_era5_box60 = nested_dict()
    
    scores_per_thresh_sphera_box100 = nested_dict()
    scores_per_thresh_era5_box100 = nested_dict()
    
    scores_per_thresh_sphera_box200 = nested_dict()
    scores_per_thresh_era5_box200 = nested_dict()
    
    for i_thresh in np.arange(0,8,1):
        
        scores_per_thresh_sphera_box15[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box15[season].columns)
        
        
        scores_per_thresh_sphera_box25[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box25[season].columns)
        scores_per_thresh_era5_box25[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box25[season].columns)
        
        scores_per_thresh_sphera_box35[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box35[season].columns)
        scores_per_thresh_era5_box35[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box35[season].columns)
        
        scores_per_thresh_sphera_box45[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box45[season].columns)
        scores_per_thresh_era5_box45[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box45[season].columns)
        
        scores_per_thresh_sphera_box60[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box60[season].columns)
        scores_per_thresh_era5_box60[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box60[season].columns)
        
        scores_per_thresh_sphera_box100[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box100[season].columns)
        scores_per_thresh_era5_box100[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box100[season].columns)
        
        scores_per_thresh_sphera_box200[i_thresh] = pd.DataFrame(index=seasons, columns=scores_sphera_box200[season].columns)
        scores_per_thresh_era5_box200[i_thresh] = pd.DataFrame(index=seasons, columns=scores_era5_box200[season].columns)
        
        for season in seasons:
           
           scores_per_thresh_sphera_box15[i_thresh].iloc[scores_per_thresh_sphera_box15[i_thresh]
                                                         .index == season] = scores_sphera_box15[season].iloc[[i_thresh]].values
            
           
           scores_per_thresh_sphera_box25[i_thresh].iloc[scores_per_thresh_sphera_box25[i_thresh]
                                                         .index == season] = scores_sphera_box25[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box25[i_thresh].iloc[scores_per_thresh_era5_box25[i_thresh]
                                                       .index == season] = scores_era5_box25[season].iloc[[i_thresh]].values

           scores_per_thresh_sphera_box35[i_thresh].iloc[scores_per_thresh_sphera_box35[i_thresh]
                                                         .index == season] = scores_sphera_box35[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box35[i_thresh].iloc[scores_per_thresh_era5_box35[i_thresh]
                                                       .index == season] = scores_era5_box35[season].iloc[[i_thresh]].values

           scores_per_thresh_sphera_box45[i_thresh].iloc[scores_per_thresh_sphera_box45[i_thresh]
                                                         .index == season] = scores_sphera_box45[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box45[i_thresh].iloc[scores_per_thresh_era5_box45[i_thresh]
                                                       .index == season] = scores_era5_box45[season].iloc[[i_thresh]].values

           scores_per_thresh_sphera_box60[i_thresh].iloc[scores_per_thresh_sphera_box60[i_thresh]
                                                         .index == season] = scores_sphera_box60[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box60[i_thresh].iloc[scores_per_thresh_era5_box60[i_thresh]
                                                       .index == season] = scores_era5_box60[season].iloc[[i_thresh]].values
           
           scores_per_thresh_sphera_box100[i_thresh].iloc[scores_per_thresh_sphera_box100[i_thresh]
                                                         .index == season] = scores_sphera_box100[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box100[i_thresh].iloc[scores_per_thresh_era5_box100[i_thresh]
                                                       .index == season] = scores_era5_box100[season].iloc[[i_thresh]].values

           scores_per_thresh_sphera_box200[i_thresh].iloc[scores_per_thresh_sphera_box200[i_thresh]
                                                         .index == season] = scores_sphera_box200[season].iloc[[i_thresh]].values
           scores_per_thresh_era5_box200[i_thresh].iloc[scores_per_thresh_era5_box200[i_thresh]
                                                       .index == season] = scores_era5_box200[season].iloc[[i_thresh]].values


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
        ylims = [-0.05, 0.6]

    #find the index of threhold based on the thresh parameter
    thr_index = int(thresholds.loc[thresholds['thr'] == thresh].index.values)


    fig, ax = plt.subplots(figsize=(13,5))
    ax.set_title(f'Precipitation larger than {thresh} mm, {trance}', fontsize=25)
    ax.set_ylim(ylims)
    
    ax.plot(scores_per_thresh_sphera_box15[thr_index].index, scores_per_thresh_sphera_box15[thr_index][sco], '-o',  markersize=8, 
            color='purple', label='15km')
    
    
    
    ax.plot(scores_per_thresh_sphera_box25[thr_index].index, scores_per_thresh_sphera_box25[thr_index][sco], '-o',  markersize=8, 
            color='#70FF7E', label='25km')
    ax.plot(scores_per_thresh_era5_box25[thr_index].index, scores_per_thresh_era5_box25[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='#70FF7E')

    ax.plot(scores_per_thresh_sphera_box35[thr_index].index, scores_per_thresh_sphera_box35[thr_index][sco], '-o',  markersize=8, 
            color='#AAD922', label='35km')
    ax.plot(scores_per_thresh_era5_box35[thr_index].index, scores_per_thresh_era5_box35[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='#AAD922')

    ax.plot(scores_per_thresh_sphera_box45[thr_index].index, scores_per_thresh_sphera_box45[thr_index][sco], '-o',  markersize=8, 
            color='#6F7C12', label='45km')
    ax.plot(scores_per_thresh_era5_box45[thr_index].index, scores_per_thresh_era5_box45[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='#6F7C12')
    
    ax.plot(scores_per_thresh_sphera_box60[thr_index].index, scores_per_thresh_sphera_box60[thr_index][sco], '-o',  markersize=8, 
            color='#483519', label='60km')
    ax.plot(scores_per_thresh_era5_box60[thr_index].index, scores_per_thresh_era5_box60[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='#483519')
    
    ax.plot(scores_per_thresh_sphera_box100[thr_index].index, scores_per_thresh_sphera_box100[thr_index][sco], '-o',  markersize=8, 
            color='red', label='100km')
    ax.plot(scores_per_thresh_era5_box100[thr_index].index, scores_per_thresh_era5_box100[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='red')
    
    ax.plot(scores_per_thresh_sphera_box200[thr_index].index, scores_per_thresh_sphera_box200[thr_index][sco], '-o',  markersize=8, 
            color='orange', label='200km')
    ax.plot(scores_per_thresh_era5_box200[thr_index].index, scores_per_thresh_era5_box200[thr_index][sco], '--o',  markersize=8,
            mfc='none', color='orange')
    
    ax.tick_params(axis='both', which='major', labelsize=18)
        
    ax.set_xlabel('Season', fontsize=22)
    ax.set_ylabel(f'{ylabel}', fontsize=22)
    legend = plt.legend(title='Box dimension', ncol=2, fontsize=18, loc='upper center')
    plt.setp(legend.get_title(),fontsize=18)
    ax.grid(lw=0.5, linestyle='--')
    
    ax1 = ax.twinx()
    ax1.set_yticks([])
        
    l1, = ax1.plot([1,1], [1.5,2], linestyle='-', marker='o', markersize=8, color='black', 
                       label='SPHERA',scaley=False)
    l2, = ax1.plot(1, 1.5, linestyle='--', marker='o', markersize=8, mfc='none', color='black', 
                       label='ERA5', scaley=False)
    ax1.legend(handles=[l1,l2], loc='upper left', fontsize=18)

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
                


score = 'TS'
thresh = 50

Scores_per_Time_box(score, thresh)
plt.savefig(f'/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/Boxing_analysis/Scores_per_time_per_box_100-200/{score}_{thresh}mm_2015-2017_poster.png', bbox_inches="tight")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
asd
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#as Scores_per_Thresh_per_Year but averaging over the trance
def Scores_per_Thresh_box(score_fig):

    seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

    winters = ['DJF15', 'DJF16']
    summers = ['JJA15', 'JJA16', 'JJA17']
    springs = ['MAM15', 'MAM16', 'MAM17']
    falls = ['SON15', 'SON16', 'SON17']
    
    scores_per_box = {}
    
    for box_size in [15, 25, 35, 45, 60, 100, 200]:
    
        scores_sphera = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box{box_size}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            
        sphera_seasonal_means = pd.DataFrame(index=scores_sphera[season].index, 
                                             columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF', 'pod_MAM', 'pod_JJA', 'pod_SON',
                                                      'pod_DJF', 'fa_MAM', 'fa_JJA', 'fa_SON', 'fa_DJF', 'bs_MAM', 'bs_JJA', 'bs_SON', 
                                                      'bs_DJF','fa.1_MAM', 'fa.1_JJA', 'fa.1_SON', 'fa.1_DJF'])
        
        sphera_seasonal_means['thr'] = scores_sphera[season].thr
        
        for score in ['ts','pod','fa','bs','fa.1']:
            
            for list_of_seasons in [springs, summers, falls, winters]:
            
                temp_df_sphera = pd.DataFrame(index=scores_sphera[season].index, columns=list_of_seasons)
                
                for season in list_of_seasons:
                    temp_df_sphera[season] = pd.Series(scores_sphera[season][f'{score}'].loc[scores_sphera[season][f'{score}'] != -999.900], 
                                                       name=season)
                    
                if list_of_seasons == springs:
                    sphera_seasonal_means[f'{score}_MAM'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == summers:
                    sphera_seasonal_means[f'{score}_JJA'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == falls:
                    sphera_seasonal_means[f'{score}_SON'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == winters:
                    sphera_seasonal_means[f'{score}_DJF'] = temp_df_sphera.mean(axis=1)
                
        scores_per_box[box_size] = sphera_seasonal_means
        
    #ATTENZIONE: per RMSE la colonna relativa è rinominata 'fa.1' a causa di un errore nella trascrizione dei nomi delle colonne!!
    score_fig='fa.1'
        
    #PLOT 4 plot, one for each season, of score as function of threshold for different box sizes          
    for season in ['MAM', 'JJA', 'SON', 'DJF']:
        
        matplotlib.rcParams['xtick.minor.size'] = 0
        matplotlib.rcParams['xtick.minor.width'] = 0
        
        #DJF and JJA plot
        fig, ax = plt.subplots(figsize=(9,4))
        ax.set_xscale('log')
        ax.set_title(f'{season}', fontsize=17)  #Average over 2015-2017
        
        
        ax.plot(scores_per_box[15]['thr'], scores_per_box[15][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='brown', label='15 km')
        ax.plot(scores_per_box[25]['thr'], scores_per_box[25][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='red', label='25 km')        
        ax.plot(scores_per_box[35]['thr'], scores_per_box[35][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='orange', label='35 km')        
        ax.plot(scores_per_box[45]['thr'], scores_per_box[45][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='green', label='45 km')        
        ax.plot(scores_per_box[60]['thr'], scores_per_box[60][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='blue', label='60 km')        
        ax.plot(scores_per_box[100]['thr'], scores_per_box[100][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='purple', label='100 km')        
        ax.plot(scores_per_box[200]['thr'], scores_per_box[200][f'{score_fig}_{season}'], '-o',  markersize=8, 
                color='black', label='200 km')        
    
        ax.set_xticks(scores_per_box[15]['thr'])
        
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax.tick_params(axis='both', which='major', labelsize=12)
        
        ax.set_xlabel('Precipitation (mm/day)', fontsize=14)
        
        if score_fig == 'ts':
            ylabel='TS'
            ax.set_ylim([-0.05,1.05])
        elif score_fig == 'pod':
            ylabel='POD'
            ax.set_ylim([-0.05,1.05])
        elif score_fig == 'fa':
            ylabel='FAR'
            ax.set_ylim([-0.05,1.05])
        elif score_fig == 'bs':
            ylabel='Frequency bias'
        elif score_fig == 'fa.1':
            ylabel='RMSE'
        
        ax.set_ylabel(f'{ylabel}', fontsize=14)
        legend = plt.legend(fontsize=15, loc='upper right', title='Box size')
        ax.grid(lw=0.5, linestyle='--')
        
        leg = plt.legend(loc='best', title='Box size', fontsize=14)
        plt.setp(leg.get_title(),fontsize=16)

        plt.savefig(f'{pathOut}/{score_fig}_{season}_avg2015-2017.pdf', bbox_inches="tight")

Scores_per_Thresh(trance)





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
asd
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""















def funct(df_sphera_sc, df_era5_sc):

    #OBIETTIVO: contare per ogni colonna del file quante volte il valore è all'interno di due soglie, per contare le occorrenze
    #di valori tra tutti gli intervalli di soglie considerati e plottarne la distribuzione
    
    #pulizia dataset: rimuovere righe con caratteri non numerici e converti in numeric
    df_sphera_sc = df_sphera_sc[pd.to_numeric(df_sphera_sc['obs'], errors='coerce').notnull()].reset_index(drop=True)
    df_sphera_sc['obs'] = pd.to_numeric(df_sphera_sc['obs'])
    df_sphera_sc = df_sphera_sc[pd.to_numeric(df_sphera_sc['prev'], errors='coerce').notnull()].reset_index(drop=True)
    df_sphera_sc['prev'] = pd.to_numeric(df_sphera_sc['prev'])
    
    df_era5_sc = df_era5_sc[pd.to_numeric(df_era5_sc['obs'], errors='coerce').notnull()].reset_index(drop=True)
    df_era5_sc['obs'] = pd.to_numeric(df_era5_sc['obs'])
    df_era5_sc = df_era5_sc[pd.to_numeric(df_era5_sc['prev'], errors='coerce').notnull()].reset_index(drop=True)
    df_era5_sc['prev'] = pd.to_numeric(df_era5_sc['prev'])
    
    
    #CHECK: osservate di sphera e era5 se sono uguali:
    #all(df_sphera_sc['obs'] == df_era5_sc['obs'])
    
    #TANTE VOLTE OBS DEI DUE RIANALISI NON COINCIDNO!! PERCHE?
    #numero diverso di previste per i due e quindi vengono tagliate le obs in più per quello che ne ha meno??
    #specialmente e.g. per JJA11: Sphera ha 5804 dati, mentre ERA5 48713!!
    #Quando le lunghezze delle due serie di obs coincidono -> in grafico solo 1 unica osservazione è presente!
        
    #set thresholds every 5mm
    thresh = np.arange(5.0,155.0,5.0)
    
    #thresh = np.concatenate((np.arange(5.0,105.0,5.0), np.arange(110.0,155.0,10.0)),axis=0)
    
    #loop on the two reanalysis:
    for df in [df_sphera_sc, df_era5_sc]:#, df_era5_sc]:
        
        #array of counters, initialized with zeros
        count_obs = np.zeros(len(thresh)+1, dtype=int)
        count_prev = np.zeros(len(thresh)+1, dtype=int)
    
        #Loops for observations:
        #for thr in thresh:
        for i in range(0, len(df)):
            #print(f'i={i}')  
           
            for j in range(0,len(thresh)):
                #print(f'j={j}') 
                
                #non contare niente se prec=0.0 mm
                if float(df['obs'].loc[i]) == 0.0:
                    break
                
                #prima condizioni su soglie aperte: < della piu piccola, > della piu grande
                if float(df['obs'].loc[i]) < thresh[0]:
                    count_obs[0] = count_obs[0] + 1
                    break
                
                elif float(df['obs'].loc[i]) >= thresh[-1]:
                    count_obs[-1] = count_obs[-1] + 1
                    break
                
                #condizioni tra due soglie chiuse    
                elif (float(df['obs'].loc[i]) >= thresh[j]) & (float(df['obs'].loc[i]) < thresh[j+1]): 
                     count_obs[j+1] = count_obs[j+1] + 1
                     break
                else:
                    continue
                
        #Loops for predicted:
        #for thr in thresh:
        for i in range(0, len(df)):
            #print(f'i={i}')  
           
            for j in range(0,len(thresh)):
                #print(f'j={j}')
                
                #non contare niente se prec=0.0 mm
                if float(df['prev'].loc[i]) == 0.0:
                    break
                
                #prima condizioni su soglie aperte: < della piu piccola, > della piu grande
                if float(df['prev'].loc[i]) < thresh[0]:
                    count_prev[0] = count_prev[0] + 1
                    break
                
                elif float(df['prev'].loc[i]) >= thresh[-1]:
                    count_prev[-1] = count_prev[-1] + 1
                    break
                
                #condizioni tra due soglie chiuse    
                elif (float(df['prev'].loc[i]) >= thresh[j]) & (float(df['prev'].loc[i]) < thresh[j+1]): 
                     count_prev[j+1] = count_prev[j+1] + 1
                     break
                else:
                    continue
         
        print('finito 1 df')
                
        #assign the counters to the right reanalysis:
        if df['prev'].equals(df_sphera_sc['prev']):
            count_obs_sphera = count_obs
            count_prev_sphera = count_prev
            
        elif df['prev'].equals(df_era5_sc['prev']):
            count_obs_era5 = count_obs
            count_prev_era5 = count_prev
            
    
    return count_obs_era5, count_obs_sphera, count_prev_era5, count_prev_sphera  


pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati'

df_sphera_box15 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box15/2015-2017_complete/scatter_plot.dat",
                       skiprows=1, sep="\s+", names=['obs','prev'])

df_sphera_box25 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box25/2015-2017_complete/scatter_plot.dat",
                       skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_box25 = pd.read_csv(f"{pathIn}/boxing_analysis/ERA5/box25/2015-2017_complete/scatter_plot.dat",
                      skiprows=1, sep="\s+", names=['obs','prev'])

df_sphera_box35 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box35/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])
df_era5_box35 = pd.read_csv(f"{pathIn}/boxing_analysis/ERA5/box35/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])

df_sphera_box45 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box45/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])
df_era5_box45 = pd.read_csv(f"{pathIn}/boxing_analysis/ERA5/box45/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])

df_sphera_box60 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box60/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])
df_era5_box60 = pd.read_csv(f"{pathIn}/boxing_analysis/ERA5/box60/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])

df_sphera_box100 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box100/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])
#df_era5_box100 = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/boxing_analysis/ERA5/box100/2015-2017_complete/scatter_plot.dat",
#                       skiprows=4, sep="\s+", names=['obs','prev'])

df_sphera_box200 = pd.read_csv(f"{pathIn}/boxing_analysis/SPHERA/box200/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])
df_era5_box200 = pd.read_csv(f"{pathIn}/boxing_analysis/ERA5/box200/2015-2017_complete/scatter_plot.dat",
                       skiprows=4, sep="\s+", names=['obs','prev'])

funct15 = funct(df_sphera_box15, df_era5_box25)
funct25 = funct(df_sphera_box25, df_era5_box25)
funct35 = funct(df_sphera_box35, df_era5_box35)
funct45 = funct(df_sphera_box45, df_era5_box45)
funct60 = funct(df_sphera_box60, df_era5_box60)
funct100 = funct(df_sphera_box100, df_era5_box60)
funct200 = funct(df_sphera_box200, df_era5_box200)


def graf_dist(funct, size):
           
    count_obs_era5 = funct[0]
    count_obs_sphera = funct[1]
    count_prev_era5 = funct[2]
    count_prev_sphera = funct[3]
    
    fig, ax = plt.subplots(1, 1, figsize=(8,4))
    
    plt.rcParams.update({'font.size': 14})
    
    plt.xlabel('Daily-cumulated precipitation threshold [mm]')
    plt.ylabel('Cases with exceeded threshold')
    
    #log y scale
    plt.yscale('log')
    
    #set only lower limit on y scale
    ax.set_ylim([0.5,400000])
    ax.set_xlim([-0.1,30.1])
    plt.xticks(np.arange(0, len(count_obs_era5), 2))
    plt.title(f'Rainfall distributions 2015-2017, box size: {size} km', fontsize=20)   #10 years: 2007-2017
    
    #ax.plot(np.arange(0,len(count_obs_era5)), count_obs_era5, label='OBS ERA5', color='blue', lw=1.5)
    ax.plot(np.arange(0,len(count_obs_sphera)), count_obs_sphera, label='OBS', color='black', lw=1.5)
    ax.plot(np.arange(0,len(count_prev_era5)), count_prev_era5, label='ERA5', color='#32AAB5', lw=1.8)
    ax.plot(np.arange(0,len(count_prev_sphera)), count_prev_sphera, label='SPHERA', color='#87489D', lw=1.8)
    
    
    #thresh_intervals_labels = ['<5', '5-10', '10-15', '15-20', '20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65',
    #                   '65-70','70-75','75-80','80-85','85-90','90-95','95-100','100-105','105-110','110-115','115-120','120-125',
    #                   '125-130','130-135','135-140','140-145','145-150','>150']
    
    thresh_intervals_labels2 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-105',
                           '110-115','120-125','130-135','140-145','>150']
    
    #thresh_intervals_labels3 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-110', '',
    #                            '120-130','','140-150','>150']
    
    ax.set_xticklabels(thresh_intervals_labels2)
    #ax.tick_params(axis='x', which='major', rotation=30)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right" )
    
    ax.grid(True, linestyle='--', lw=0.75)
    
    plt.legend(loc='best')



size='25'
funct = funct25

graf_dist(funct, size)

plt.savefig(f'/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/Boxing_analysis/rainfall_distributions/rainfall_dist_2015-2017_{size}km.png', bbox_inches='tight')


#Plot with difference between obs frequency and SPHERA frequency for different sizes of the box:
    
    


count_obs_sphera_15 = funct15[1]
count_prev_sphera_15 = funct15[3]
count_obs_sphera_25 = funct25[1]
count_prev_sphera_25 = funct25[3]
count_obs_sphera_35 = funct35[1]
count_prev_sphera_35 = funct35[3]
count_obs_sphera_45 = funct45[1]
count_prev_sphera_45 = funct45[3]
count_obs_sphera_60 = funct60[1]
count_prev_sphera_60 = funct60[3]
count_obs_sphera_100 = funct100[1]
count_prev_sphera_100 = funct100[3]
count_obs_sphera_200 = funct200[1]
count_prev_sphera_200 = funct200[3]


count_obs_era5_25 = funct25[0]
count_prev_era5_25 = funct25[2]
count_obs_era5_35 = funct35[0]
count_prev_era5_35 = funct35[2]
count_obs_era5_45 = funct45[0]
count_prev_era5_45 = funct45[2]
count_obs_era5_60 = funct60[0]
count_prev_era5_60 = funct60[2]
#count_obs_era5_100 = funct100[0]
#count_prev_era5_100 = funct100[2]
count_obs_era5_200 = funct200[0]
count_prev_era5_200 = funct200[2]




fig, ax = plt.subplots(1, 1, figsize=(10,6))

plt.rcParams.update({'font.size': 14})

plt.xlabel('Daily-cumulated precipitation threshold [mm]')
plt.ylabel('|SPHERA - OBS| (cases with exceeded threshold)')

#log y scale
plt.yscale('log')

#set only lower limit on y scale
ax.set_ylim([0.5,400000])
ax.set_xlim([-0.1,30.1])
plt.xticks(np.arange(0, len(count_obs_sphera_25), 2))
plt.title(f'Absolute difference in rainfall distributions, 2015-2017', fontsize=20)   #10 years: 2007-2017

ax.plot(np.arange(0,len(count_obs_sphera_25)), abs(count_prev_sphera_25 - count_obs_sphera_25), label='25 km', color='red', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_35)), abs(count_prev_sphera_35 - count_obs_sphera_35), label='35 km', color='blue', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_45)), abs(count_prev_sphera_45 - count_obs_sphera_45), label='45 km', color='green', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_60)), abs(count_prev_sphera_60 - count_obs_sphera_60), label='60 km', color='orange', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_100)), abs(count_prev_sphera_100 - count_obs_sphera_100), label='100 km', color='purple', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_200)), abs(count_prev_sphera_200 - count_obs_sphera_200), label='200 km', color='black', lw=1.5)

#ax.plot(np.arange(0,len(count_obs_sphera_25)), abs(count_prev_era5_25 - count_obs_era5_25), label='25 km', color='red', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_35)), abs(count_prev_era5_35 - count_obs_era5_35), label='35 km', color='blue', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_45)), abs(count_prev_era5_45 - count_obs_era5_45), label='45 km', color='green', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_60)), abs(count_prev_era5_60 - count_obs_era5_60), label='60 km', color='orange', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_100)), abs(count_prev_sphera_100 - count_obs_sphera_100), label='100 km', color='purple', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_200)), abs(count_prev_era5_200 - count_obs_era5_200), label='200 km', color='black', lw=1.5, linestyle='--')


#thresh_intervals_labels = ['<5', '5-10', '10-15', '15-20', '20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65',
#                   '65-70','70-75','75-80','80-85','85-90','90-95','95-100','100-105','105-110','110-115','115-120','120-125',
#                   '125-130','130-135','135-140','140-145','145-150','>150']

thresh_intervals_labels2 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-105',
                       '110-115','120-125','130-135','140-145','>150']

#thresh_intervals_labels3 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-110', '',
#                            '120-130','','140-150','>150']

ax.set_xticklabels(thresh_intervals_labels2)
#ax.tick_params(axis='x', which='major', rotation=30)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right" )

ax.grid(True, linestyle='--', lw=0.75)

plt.legend(loc='best')

plt.savefig(f'/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/Boxing_analysis/rainfall_distributions/Difference_rainfall_dist_2015-2017.png', bbox_inches='tight')



#NORMALIZED PLOT:
    
fig, ax = plt.subplots(1, 1, figsize=(9,6))

plt.rcParams.update({'font.size': 14})

plt.xlabel('Daily-cumulated precipitation threshold [mm/day]', fontsize=16)
plt.ylabel('Normalized distance |SPHERA - OBS|', fontsize=16)

#log y scale
#plt.yscale('log')

#set only lower limit on y scale
ax.set_ylim([0.5,10])
ax.set_xlim([-0.1,30.1])
plt.xticks(np.arange(0, len(count_obs_sphera_25), 2))
plt.title(f'Normalized abs. difference (SPHERA - DEWETRA) \n rainfall distributions, 2015-2017', fontsize=18)   #10 years: 2007-2017

ax.plot(np.arange(0,len(count_obs_sphera_15)), abs(count_prev_sphera_15 - count_obs_sphera_15)/count_obs_sphera_15, 
        label='15 km', color='brown', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_25)), abs(count_prev_sphera_25 - count_obs_sphera_25)/count_obs_sphera_25,
        label='25 km', color='red', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_35)), abs(count_prev_sphera_35 - count_obs_sphera_35)/count_obs_sphera_35, 
        label='35 km', color='orange', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_45)), abs(count_prev_sphera_45 - count_obs_sphera_45)/count_obs_sphera_45, 
        label='45 km', color='green', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_60)), abs(count_prev_sphera_60 - count_obs_sphera_60)/count_obs_sphera_60, 
        label='60 km', color='blue', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_100)), abs(count_prev_sphera_100 - count_obs_sphera_100)/count_obs_sphera_100, 
        label='100 km', color='purple', lw=1.5)
ax.plot(np.arange(0,len(count_obs_sphera_200)), abs(count_prev_sphera_200 - count_obs_sphera_200)/count_obs_sphera_200,
        label='200 km', color='black', lw=1.5)

#ax.plot(np.arange(0,len(count_obs_sphera_25)), abs(count_prev_era5_25 - count_obs_era5_25)/count_obs_era5_25, color='red', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_35)), abs(count_prev_era5_35 - count_obs_era5_35)/count_obs_era5_35, color='blue', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_45)), abs(count_prev_era5_45 - count_obs_era5_45)/count_obs_era5_45, color='green', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_60)), abs(count_prev_era5_60 - count_obs_era5_60)/count_obs_era5_60, color='orange', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_100)), abs(count_prev_era5_100 - count_obs_era5_100)/count_obs_era5_100, color='purple', lw=1.5, linestyle='--')
#ax.plot(np.arange(0,len(count_obs_sphera_200)), abs(count_prev_era5_200 - count_obs_era5_200)/count_obs_era5_200, color='black', lw=1.5, linestyle='--')

#thresh_intervals_labels = ['<5', '5-10', '10-15', '15-20', '20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65',
#                   '65-70','70-75','75-80','80-85','85-90','90-95','95-100','100-105','105-110','110-115','115-120','120-125',
#                   '125-130','130-135','135-140','140-145','145-150','>150']

thresh_intervals_labels2 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-105',
                       '110-115','120-125','130-135','140-145','>150']

#thresh_intervals_labels3 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-110', '',
#                            '120-130','','140-150','>150']

ax.set_xticklabels(thresh_intervals_labels2)
#ax.tick_params(axis='x', which='major', rotation=30)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right" )

ax.grid(True, linestyle='--', lw=0.75)

leg = plt.legend(loc='best', title='Box size', fontsize=13)
plt.setp(leg.get_title(),fontsize=15)


#ax1 = ax.twinx()
#ax1.set_yticks([])
    
#l1, = ax1.plot([1,1], [1.5,2], linestyle='-', color='black', label='SPHERA',scaley=False)
#l2, = ax1.plot(1, 1.5, linestyle='--', color='black', label='ERA5', scaley=False)
#ax1.legend(handles=[l1,l2], loc='upper center', fontsize=15)


plt.savefig(f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_DEWETRA/Boxing_analysis/rainfall_distributions/Normalized_Difference_rainfall_dist_2015-2017_SPHERA_correct2_AGGIORNATO.png', bbox_inches='tight')



    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PERFORMANCE DIAGRAM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import itertools

import rpy2.robjects as ro
import rpy2.robjects.packages as r

import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()

#import verification library from R
ver = ro.packages.importr("verification")

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/boxing_analysis/SPHERA'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/vs_DEWETRA/Boxing_analysis/Performance_diagram'

season='2015-2017_complete'

def PerformanceDiagram(season):
    
    scores_sphera = {}
    cont_sphera = {}
    
    #PER PERIODO 2015-2017 INTERO AVERAGED:
    
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    scores_sphera['25'] = pd.read_csv(f"{pathIn}/box25/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    scores_sphera['35'] = pd.read_csv(f"{pathIn}/box35/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    scores_sphera['45'] = pd.read_csv(f"{pathIn}/box45/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    scores_sphera['60'] = pd.read_csv(f"{pathIn}/box60/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    scores_sphera['100'] = pd.read_csv(f"{pathIn}/box100/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    scores_sphera['200'] = pd.read_csv(f"{pathIn}/box200/{season}/scores_per_scad.dat",skiprows=4, sep="\s+")
    
    #scores_era5 = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ERA5/2003-2006/{season}/scores_per_scad.dat",
    #                           skiprows=4, sep="\s+")
 
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera['15'] = pd.read_csv(f"{pathIn}/box15/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['25'] = pd.read_csv(f"{pathIn}/box25/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['35'] = pd.read_csv(f"{pathIn}/box35/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['45'] = pd.read_csv(f"{pathIn}/box45/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['60'] = pd.read_csv(f"{pathIn}/box60/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['100'] = pd.read_csv(f"{pathIn}/box100/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    cont_sphera['200'] = pd.read_csv(f"{pathIn}/box200/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
    
    #cont_era5 = pd.read_csv(f"/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ERA5/2003-2006/{season}/cont_table_mod.dat",
    #                           skiprows=0, sep="\s+")
    
    
    #PER STAGIONI SPECIFICHE: JJA AVERAGED O DJF AVERAGED
    seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

    winters = ['DJF15', 'DJF16']
    summers = ['JJA15', 'JJA16', 'JJA17']
    springs = ['MAM15', 'MAM16', 'MAM17']
    falls = ['SON15', 'SON16', 'SON17']
    
    scores_per_box = {}
    cont_seasonal_sums = {}
    
    for box_size in [15, 25, 35, 45, 60, 100, 200]:
        
        cont_seasonal_sums[f'{box_size}'] = {}
        
        scores_sphera = {}
        cont_sphera = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/box{box_size}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            cont_sphera[season] =  pd.read_csv(f"{pathIn}/box{box_size}/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
            

        cont_seasonal_sums[f'{box_size}']['DJF'] = cont_sphera['DJF15']
        cont_seasonal_sums[f'{box_size}']['DJF'][0:2] = cont_seasonal_sums[f'{box_size}']['DJF'][0:2] + cont_sphera['DJF16'][0:2]
        cont_seasonal_sums[f'{box_size}']['DJF'][3:5] = cont_seasonal_sums[f'{box_size}']['DJF'][3:5] + cont_sphera['DJF16'][3:5]
        cont_seasonal_sums[f'{box_size}']['DJF'][6:8] = cont_seasonal_sums[f'{box_size}']['DJF'][6:8] + cont_sphera['DJF16'][6:8]
        cont_seasonal_sums[f'{box_size}']['DJF'][9:11] = cont_seasonal_sums[f'{box_size}']['DJF'][9:11] + cont_sphera['DJF16'][9:11]
        cont_seasonal_sums[f'{box_size}']['DJF'][12:14] = cont_seasonal_sums[f'{box_size}']['DJF'][12:14] + cont_sphera['DJF16'][12:14]
        cont_seasonal_sums[f'{box_size}']['DJF'][15:17] = cont_seasonal_sums[f'{box_size}']['DJF'][15:17] + cont_sphera['DJF16'][15:17]
        cont_seasonal_sums[f'{box_size}']['DJF'][18:20] = cont_seasonal_sums[f'{box_size}']['DJF'][18:20] + cont_sphera['DJF16'][18:20]
        cont_seasonal_sums[f'{box_size}']['DJF'][21:23] = cont_seasonal_sums[f'{box_size}']['DJF'][21:23] + cont_sphera['DJF16'][21:23]
        
        cont_seasonal_sums[f'{box_size}']['JJA'] = cont_sphera['JJA15']
        cont_seasonal_sums[f'{box_size}']['JJA'][0:2] = cont_seasonal_sums[f'{box_size}']['JJA'][0:2] + cont_sphera['JJA16'][0:2] + cont_sphera['JJA17'][0:2]
        cont_seasonal_sums[f'{box_size}']['JJA'][3:5] = cont_seasonal_sums[f'{box_size}']['JJA'][3:5] + cont_sphera['JJA16'][3:5] + cont_sphera['JJA17'][3:5]
        cont_seasonal_sums[f'{box_size}']['JJA'][6:8] = cont_seasonal_sums[f'{box_size}']['JJA'][6:8] + cont_sphera['JJA16'][6:8] + cont_sphera['JJA17'][6:8]
        cont_seasonal_sums[f'{box_size}']['JJA'][9:11] = cont_seasonal_sums[f'{box_size}']['JJA'][9:11] + cont_sphera['JJA16'][9:11] + cont_sphera['JJA17'][9:11]
        cont_seasonal_sums[f'{box_size}']['JJA'][12:14] = cont_seasonal_sums[f'{box_size}']['JJA'][12:14] + cont_sphera['JJA16'][12:14] + cont_sphera['JJA17'][12:14]
        cont_seasonal_sums[f'{box_size}']['JJA'][15:17] = cont_seasonal_sums[f'{box_size}']['JJA'][15:17] + cont_sphera['JJA16'][15:17] + cont_sphera['JJA17'][15:17]
        cont_seasonal_sums[f'{box_size}']['JJA'][18:20] = cont_seasonal_sums[f'{box_size}']['JJA'][18:20] + cont_sphera['JJA16'][18:20] + cont_sphera['JJA17'][18:20]
        cont_seasonal_sums[f'{box_size}']['JJA'][21:23] = cont_seasonal_sums[f'{box_size}']['JJA'][21:23] + cont_sphera['JJA16'][21:23] + cont_sphera['JJA17'][21:23]
        
        
       
        sphera_seasonal_means = pd.DataFrame(index=scores_sphera[season].index, 
                                            columns=['thr', 'ts_MAM', 'ts_JJA', 'ts_SON', 'ts_DJF', 'pod_MAM', 'pod_JJA', 'pod_SON',
                                                     'pod_DJF', 'fa_MAM', 'fa_JJA', 'fa_SON', 'fa_DJF', 'bs_MAM', 'bs_JJA', 'bs_SON', 
                                                     'bs_DJF','fa.1_MAM', 'fa.1_JJA', 'fa.1_SON', 'fa.1_DJF'])
        sphera_seasonal_means['thr'] = scores_sphera[season].thr
        
        for score in ['ts','pod','fa','bs','fa.1']:
            
            for list_of_seasons in [springs, summers, falls, winters]:
            
                temp_df_sphera = pd.DataFrame(index=scores_sphera[season].index, columns=list_of_seasons)
                
                for season in list_of_seasons:
                    temp_df_sphera[season] = pd.Series(scores_sphera[season][f'{score}'].loc[scores_sphera[season][f'{score}'] != -999.900], 
                                                       name=season)
                    
                if list_of_seasons == springs:
                    sphera_seasonal_means[f'{score}_MAM'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == summers:
                    sphera_seasonal_means[f'{score}_JJA'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == falls:
                    sphera_seasonal_means[f'{score}_SON'] = temp_df_sphera.mean(axis=1)
                elif list_of_seasons == winters:
                    sphera_seasonal_means[f'{score}_DJF'] = temp_df_sphera.mean(axis=1)
                
        scores_per_box[f'{box_size}'] = sphera_seasonal_means
    
    scores_sphera = scores_per_box
    
    
    #DECIDERE STAGIONE:
    seas = 'DJF'
    
    plt.figure(figsize=(13, 9))
    grid_ticks = np.arange(0, 1.01, 0.01)
    sr_g, pod_g = np.meshgrid(grid_ticks, grid_ticks)
    bias = pod_g / sr_g
    csi = 1.0 / (1.0 / sr_g + 1.0 / pod_g - 1.0)
    csi_contour = plt.contourf(sr_g, pod_g, csi, np.arange(0.1, 1.1, 0.1), extend="max", cmap='Greens')
    b_contour = plt.contour(sr_g, pod_g, bias, [0.3, 0.5, 0.8, 1, 1.3, 1.5, 2, 4], colors="k", linestyles="dashed", linewidths=0.5)
    plt.clabel(b_contour, fmt="%1.1f", manual=[(0.23, 0.95), (0.43, 0.95), (0.63, 0.95), (0.72,0.95), (0.8, 0.8), (0.85, 0.67), (0.9, 0.45), (0.75,0.22)])
    
    markers = itertools.cycle(['o','^','s','D','h','8','v','p']) 
       
    for thresh in np.arange(0,8,1):
        
        marker = next(markers)
        
        colors = itertools.cycle(['brown', 'blue', 'black'])  #['brown', 'red', 'orange', 'green', 'blue', 'purple', 'black']) 
        
        ct_sphera = {}
        cont_vec = {}
        m = {}
        bootstrap = {}
        error_bars = {}
        x = {}
        y = {}
        yerr = {}
        xerr = {}
        
        for box in [15,60,200]:   #[15,25,35,45,60,100,200]:
            
            color = next(colors)
            
            #cont_sphera[f'{box}'] = cont_sphera[f'{box}'].fillna(0)
        
            if scores_sphera[f'{box}'].loc[thresh].pod_JJA != -999.9: #scores_sphera[f'{box}'].loc[thresh].pod != -999.9:
                
                if thresh == 0:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[0:1] #cont_sphera[f'{box}'].loc[0:1]
                elif thresh == 1:
                    ct_sphera[f'{box}']= cont_seasonal_sums[f'{box}'][f'{seas}'].loc[3:4] #cont_sphera[f'{box}'].loc[3:4]
                elif thresh == 2:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[6:7]  #cont_sphera[f'{box}'].loc[6:7]
                elif thresh == 3:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[9:10]  #cont_sphera[f'{box}'].loc[9:10]
                elif thresh == 4:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[12:13]  #cont_sphera[f'{box}'].loc[12:13]
                elif thresh == 5:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[15:16]  #cont_sphera[f'{box}'].loc[15:16]
                elif thresh == 6:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[18:19]  #cont_sphera[f'{box}'].loc[18:19]
                elif thresh == 7:
                    ct_sphera[f'{box}'] = cont_seasonal_sums[f'{box}'][f'{seas}'].loc[21:22]  #cont_sphera[f'{box}'].loc[21:22]
                    
                #read the contingency table as R matrix
                cont_vec[f'{box}'] = ro.IntVector([int(ct_sphera[f'{box}'].iloc[0,0]),int(ct_sphera[f'{box}'].iloc[1,0]),
                                         int(ct_sphera[f'{box}'].iloc[0,1]),int(ct_sphera[f'{box}'].iloc[1,1])])
                m[f'{box}'] = ro.r.matrix(cont_vec[f'{box}'],nrow=2, ncol = 2)
                
                #apply bootstrap resampling to the contingency table to calculate the confidence intervals of POD and FAR 
                boot = ro.r('table.stats.boot')
                bootstrap[f'{box}'] = boot(m[f'{box}'], R=1000)
                        
                #extract values from R bootstrap function to save in a pd.DataFrame
                error_bars[f'{box}'] = pd.DataFrame(columns=['pod','sr'])
                
                error_bars[f'{box}'].loc[0,'pod'] = bootstrap[f'{box}'][0]
                error_bars[f'{box}'].loc[1,'pod'] = bootstrap[f'{box}'][1]
                error_bars[f'{box}'].loc[0,'sr'] = 1-bootstrap[f'{box}'][3]
                error_bars[f'{box}'].loc[1,'sr'] = 1-bootstrap[f'{box}'][2]
                
                #plot value with errorbars
                x[f'{box}'] = 1 - scores_sphera[f'{box}'].loc[thresh][f'fa_{seas}']
                y[f'{box}'] = scores_sphera[f'{box}'].loc[thresh][f'pod_{seas}']
                yerr[f'{box}'] = [[y[f'{box}'] - error_bars[f'{box}'].loc[1,'pod']],
                                  [error_bars[f'{box}'].loc[0,'pod'] - y[f'{box}']]]
                xerr[f'{box}'] = [[x[f'{box}'] - error_bars[f'{box}'].loc[1,'sr']],
                                  [error_bars[f'{box}'].loc[0,'sr'] - x[f'{box}']]]
                
                if box==200:
                    label_thr = int(scores_sphera[f'{box}'].loc[thresh].thr)
                    label = f'{label_thr}'
                else:
                    label = ''
                    
                plt.errorbar(x[f'{box}'], y[f'{box}'], yerr = yerr[f'{box}'], xerr = xerr[f'{box}'],  marker=marker, markersize=12, 
                             color=color, linestyle='', label=label)
       
    cbar = plt.colorbar(csi_contour)
    cbar.ax.tick_params(labelsize=14) 
    cbar.set_label('Threat Score (TS)', fontsize=17)
    plt.xlabel('Success Ratio (1-FAR)', fontsize=17)
    plt.ylabel('Probability of detection (POD)', fontsize=17)
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.title(f' {seas} average over 2015-2017', fontsize=20)#, fontweight="bold")
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.text(0.67,0.57,"Frequency Bias",fontdict=dict(fontsize=15, rotation=37))
    
    legend = plt.legend(title='Threshold \n [mm/day]', **dict(loc='lower right', fontsize=15, framealpha=0.75, frameon=True))
    plt.setp(legend.get_title(),fontsize=15)
    ax = plt.gca().add_artist(legend)
    
    #legenda per le due diverse rianalisi
    l1, = plt.plot(1 - scores_sphera['15'].loc[0][f'fa_{seas}'], scores_sphera['15'].loc[0][f'pod_{seas}'], linestyle='', marker='o', markersize=12, 
                   color='brown', label='15 km')
    #l2, = plt.plot(1 - scores_sphera['25'].loc[0].fa, scores_sphera['25'].loc[0].pod, linestyle='', marker='o', markersize=12, 
    #               color='red', label='25 km')
    #l3, = plt.plot(1 - scores_sphera['35'].loc[0].fa, scores_sphera['35'].loc[0].pod, linestyle='', marker='o', markersize=12, 
    #               color='orange', label='35 km')
    #l4, = plt.plot(1 - scores_sphera['45'].loc[0].fa, scores_sphera['45'].loc[0].pod, linestyle='', marker='o', markersize=12, 
    #               color='green', label='45 km')
    l5, = plt.plot(1 - scores_sphera['60'].loc[0][f'fa_{seas}'], scores_sphera['60'].loc[0][f'pod_{seas}'], linestyle='', marker='o', markersize=12, 
                   color='blue', label='60 km')
    #l6, = plt.plot(1 - scores_sphera['100'].loc[0].fa, scores_sphera['100'].loc[0].pod, linestyle='', marker='o', markersize=12, 
    #               color='purple', label='100 km')
    l7, = plt.plot(1 - scores_sphera['200'].loc[0][f'fa_{seas}'], scores_sphera['200'].loc[0][f'pod_{seas}'], linestyle='', marker='o', markersize=12, 
                   color='black', label='200 km')
    
    leg2 = plt.legend(handles=[l1,l5,l7], loc='upper right', title='Box size', fontsize=15)
    plt.setp(leg2.get_title(),fontsize=17)

    plt.savefig(f'{pathOut}/perfDiag_boxing_15-60-200_avg2015-2017_{seas}.pdf', bbox_inches='tight')





















