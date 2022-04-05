import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns
import matplotlib.ticker as mticker

"""
Script per plotting di score FAR (SR), POD e TS a frequenza oraria
E plotting istogrammi di frequenza relativa preci a freq oraria
e perfomance diagram a freq oraria
"""


#decide wether max or mean in the box:
aggr='max'

if aggr=='max':
    title_label='MAXIMUM'
elif aggr=='mean':
    title_label='MEAN'

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ver_oraria'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/ver_oraria/box60_{aggr}'


#as Scores_per_Thresh_per_Year but averaging over the trance
def Scores_per_Thresh(trance, aggr):

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
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
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
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
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
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
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
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
       #     scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
       #                        skiprows=4, sep="\s+")
       
    if trance == '2003-2017':
        
        seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06', 'DJF06']
        seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10', 'DJF10']
        seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14', 'DJF14']  
        seasons4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17'] 
        
        winters = ['DJF03', 'DJF04', 'DJF05', 'DJF06', 'DJF07', 'DJF08', 'DJF09', 'DJF10', 'DJF11', 'DJF12', 'DJF13', 'DJF14',
                    'DJF15', 'DJF16']
        summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14',
                   'JJA15', 'JJA16', 'JJA17']
        springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14',
                   'MAM15', 'MAM16', 'MAM17']
        falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14',
                 'SON15', 'SON16', 'SON17']
        
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
        
    #Discard threshold 40 mm/day
    sphera_seasonal_means = sphera_seasonal_means[:9]
    era5_seasonal_means = era5_seasonal_means[:9]         
        
    matplotlib.rcParams['xtick.minor.size'] = 0
    matplotlib.rcParams['xtick.minor.width'] = 0
    
    #DJF and JJA plot
    fig, ax = plt.subplots(figsize=(8.5,4))
    ax.set_xscale('log')
    ax.set_title(r'$\bf{' + 'DEWETRA' + '}$ (2003-2017)', fontsize=19)  # using the {title_label} of the box', fontsize=17)
    ax.set_ylim([-0.05,0.45])
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_JJA'], '-o',  markersize=10, color='#7F000D', label='Summer',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_JJA'], '--o',  markersize=10, mfc='none', color='#7F000D',lw=2)
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_DJF'], '-o',  markersize=10, color='#023FA5', label='Winter',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_DJF'], '--o',  markersize=10, mfc='none', color='#023FA5',lw=2)
    
    ax.set_xticks(sphera_seasonal_means['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    ax.set_xlabel('Precipitation threshold (mm/hour)', fontsize=19)
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

    plt.savefig(f'{pathOut}/Scores_per_Thresh/TS_JJA_DJF_{trance}_Box60_{aggr}_2.pdf', bbox_inches="tight")


    #SON and MAM plot
    fig, ax = plt.subplots(figsize=(8.5,4))
    ax.set_xscale('log')
    ax.set_title(r'$\bf{' + 'DEWETRA' + '}$ (2003-2017)', fontsize=19)  # using the {title_label} of the box', fontsize=17)
    ax.set_ylim([-0.05,0.45])
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_MAM'], '-o',  markersize=10, color='#027C1E', label='Spring',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_MAM'], '--o',  markersize=10, mfc='none', color='#027C1E',lw=2)
    
    ax.plot(sphera_seasonal_means['thr'], sphera_seasonal_means['ts_SON'], '-o',  markersize=10, color='#E8853A', label='Fall',lw=2)
    ax.plot(era5_seasonal_means['thr'], era5_seasonal_means['ts_SON'], '--o',  markersize=10, mfc='none', color='#E8853A',lw=2)
    
    ax.set_xticks(sphera_seasonal_means['thr'])
    
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.tick_params(axis='both', which='major', labelsize=15)
    
    ax.set_xlabel('Precipitation threshold (mm/hour)', fontsize=19)
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

    plt.savefig(f'{pathOut}/Scores_per_Thresh/TS_MAM_SON_{trance}_Box60_{aggr}_2.pdf', bbox_inches="tight")


trance='2015-2017'

Scores_per_Thresh(trance,aggr)



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def Scores_per_Time(trance, score, thresh):

    if trance == '2003-2006':
        
        seasons = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06']
      
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")    

    if trance == '2007-2010':
        
        seasons = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
                   'DJF09', 'MAM10', 'JJA10', 'SON10']
      
        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
       
    if trance == '2011-2014':
        
        seasons = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
                   'DJF13', 'MAM14', 'JJA14', 'SON14']  

        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
        
        
    if trance == '2015-2017':
        
        seasons = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17']   

        scores_sphera = {}
        scores_era5 = {}
        
        for season in seasons:
            scores_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
            scores_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/{trance}/{season}/scores_per_scad.dat",
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
    thresholds = pd.DataFrame(index=np.arange(0,10,1), columns=['thr'])
    thresholds['thr'] = [0.5,1,1.5,2,5,7.5,10,15,20,40]


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
        ylims = [-0.05, 0.45]

    #find the index of threhold based on the thresh parameter
    thr_index = int(thresholds.loc[thresholds['thr'] == thresh].index.values)


    fig, ax = plt.subplots(figsize=(13,4))
    ax.set_title(f'Precipitation larger than {thresh} mm/hour, {trance} \n using the {title_label} of the box', fontsize=20)
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
                


trance = '2015-2017'
score = 'TS'

for thresh in [0.5,1.5,5,10]:

    Scores_per_Time(trance, score, thresh)

    plt.savefig(f'{pathOut}/Scores_per_Time/{score}_{thresh}mm_{trance}_Box60_{aggr}.png', bbox_inches="tight")
    
    
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ISTOGRAMMA FREQUENZA RELATIVA ORARIA
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Leggere gli scatter_plot.dat per ogni stagione e poi aggregare tutto insieme in un file

#QUANDO AVREMO LE ALTRE TRANCE BISOGNERA FARE ANCHE UN CICLO SULLE TRANCE!

seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
                   'DJF05', 'MAM06', 'JJA06', 'SON06', 'DJF06']
seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
           'DJF09', 'MAM10', 'JJA10', 'SON10', 'DJF10']
seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
           'DJF13', 'MAM14', 'JJA14', 'SON14', 'DJF14']  
seasons4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17'] 


#NEGLI scatter_plot.dat LA PRIMA COLONNA SONO OBS E SECONDA PREVISTE (giusto)

#per leggere non usare pd.read_fwf!!!! TAGLIA VIA DATI CON VALORI PIU ALTI!!! usare pd.read_csv

df_sphera = {}
df_era5 = {}

for season in seasons1:
    df_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2003-2006/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
    df_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2003-2006/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
for season in seasons2:
    df_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2007-2010/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
    df_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2007-2010/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
for season in seasons3:
    df_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2011-2014/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
    df_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2011-2014/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
for season in seasons4:
    df_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/2015-2017/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
    df_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/2015-2017/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


#concatenare le diverse stagioni in un unico dataframe con tutte le coppie obs-prev:
df_sphera_2003_2017 = pd.concat(df_sphera.values(), ignore_index=True)
df_era5_2003_2017 = pd.concat(df_era5.values(), ignore_index=True)

def funct_distr(df_sphera_sc, df_era5_sc, thresh=[0.5,1,1.5,2,5,7.5,10,15,20,40]): # thresh=[0.5,1,1.5,2,5,7.5,10,15,20,40]):

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
    
    #loop on the two reanalysis:
    for df in [df_sphera_sc, df_era5_sc]:
        
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
                if float(df['obs'].loc[i]) <= thresh[0]:
                    count_obs[0] = count_obs[0] + 1
                    break
                
                elif float(df['obs'].loc[i]) >= thresh[-1]:
                    count_obs[-1] = count_obs[-1] + 1
                    break
                
                #condizioni tra due soglie chiuse    
                elif (float(df['obs'].loc[i]) > thresh[j]) & (float(df['obs'].loc[i]) <= thresh[j+1]): 
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
                if float(df['prev'].loc[i]) == 0:
                    break
                
                #prima condizioni su soglie aperte: < della piu piccola, > della piu grande
                if float(df['prev'].loc[i]) <= thresh[0]:
                    count_prev[0] = count_prev[0] + 1
                    break
                
                elif float(df['prev'].loc[i]) >= thresh[-1]:
                    count_prev[-1] = count_prev[-1] + 1
                    break
                
                #condizioni tra due soglie chiuse    
                elif (float(df['prev'].loc[i]) > thresh[j]) & (float(df['prev'].loc[i]) <= thresh[j+1]): 
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



thresh_1=[0.5,1,1.5,2,5,7.5,10,15,20,40]
thresh_2=[1,2,3,5,7,10,20]

thresh_intervals_1 = ["<0.5","0.5-1.0","1.0-1.5","1.5-2.0","2.0-5.0","5.0-7.5","7.5-10","10-15","15-20","20-40",">40"]
thresh_intervals_2 = ["<1","(1-2]","(2-3]","(3-5]","(5-7]","(7-10]","(10-20]",">20"]


#CHOOSE Thresholds and thresholds intervals
thresh = thresh_2

funct2015_17 = funct_distr(df_sphera_2003_2017, df_era5_2003_2017, thresh) #df_sphera_2015_2017


count_obs_sphera_2015_17 = funct2015_17[1]
count_prev_sphera_2015_17 = funct2015_17[3]
count_obs_era5_2015_17 = funct2015_17[0]
count_prev_era5_2015_17 = funct2015_17[2]

TOT_count_obs_sphera = count_obs_sphera_2015_17
TOT_count_prev_sphera = count_prev_sphera_2015_17
TOT_count_obs_era5 = count_obs_era5_2015_17
TOT_count_prev_era5 = count_prev_era5_2015_17

#normalize the count arrays with the total count of each array to find the normalized frequency:
norm_TOT_count_obs_sphera = TOT_count_obs_sphera/sum(TOT_count_obs_sphera)
norm_TOT_count_prev_sphera = TOT_count_prev_sphera/sum(TOT_count_prev_sphera)
norm_TOT_count_prev_era5 = TOT_count_prev_era5/sum(TOT_count_prev_era5)
norm_TOT_count_obs_era5 = TOT_count_obs_era5/sum(TOT_count_obs_era5)


#dataframe con obs, sphera ed era5 ai vari livelli di thresholds
df_thresh_1 = pd.DataFrame(index=range(len(thresh_intervals_2)), columns=['Obs','Sphera','Era5','thresh_int'])
df_thresh_1['Obs'] = norm_TOT_count_obs_sphera
df_thresh_1['Sphera'] = norm_TOT_count_prev_sphera
df_thresh_1['Era5'] = norm_TOT_count_prev_era5
df_thresh_1['thresh_int'] = thresh_intervals_2
melt_df_thresh_1 = pd.melt(df_thresh_1, id_vars=['thresh_int'])



#HISTOGRAMS PLOT
sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(figsize=(6.5,4))

ax1.set_title(f'Hourly rainfall frequency distributions (2003-2017)', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
#ax1.set_ylim(0,0.65)
sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_thresh_1, palette=["#023FA5", "#87489D", "#32AAB5"])

ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('Normalized frequency', fontsize = 14)
ax1.set_xlabel('Precipitation threshold [mm/hour]', fontsize=14)
sns.despine(offset=10, trim=True)

handles, labels = plt.gca().get_legend_handles_labels()
labels = ['DEWETRA', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend1 = ax1.legend(by_label.values(), by_label.keys(), title='', fontsize=12)
#plt.setp(legend1.get_title(),fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=13)


    
plt.savefig(f'{pathOut}/rainfall_dist_2003-2017_box60_{aggr}_intervals2_2_3.pdf', bbox_inches="tight", dpi=300)




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

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ver_oraria'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/scores_plots/ver_oraria/box60_max/PerformanceDiagram'


seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
           'DJF05', 'MAM06', 'JJA06', 'SON06', 'DJF06']
seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
           'DJF09', 'MAM10', 'JJA10', 'SON10', 'DJF10']
seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
           'DJF13', 'MAM14', 'JJA14', 'SON14', 'DJF14']  
seasons4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17'] 

seasons=seasons1+seasons2+seasons3+seasons4

winters = ['DJF03', 'DJF04', 'DJF05', 'DJF06', 'DJF07', 'DJF08', 'DJF09', 'DJF10', 'DJF11', 'DJF12', 'DJF13', 'DJF14',
            'DJF15', 'DJF16']
summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14',
           'JJA15', 'JJA16', 'JJA17']
springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14',
           'MAM15', 'MAM16', 'MAM17']
falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14',
         'SON15', 'SON16', 'SON17']

years = ['2003','2004','2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']

MAM_sphera = {}
MAM_era5 = {}
JJA_sphera = {}
JJA_era5 = {}
SON_sphera = {}
SON_era5 = {}
DJF_sphera = {}
DJF_era5 = {}

cont_sphera_mam = {}
cont_era5_mam = {}   
cont_sphera_jja = {}
cont_era5_jja = {}
cont_sphera_son = {}
cont_era5_son = {}     
cont_sphera_djf = {}
cont_era5_djf = {}   


for season in springs:
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    MAM_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    MAM_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera_mam[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    cont_era5_mam[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")

for season in summers:
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    JJA_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    JJA_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera_jja[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    cont_era5_jja[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
for season in falls:
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    SON_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    SON_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera_son[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    cont_era5_son[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
for season in winters:
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    DJF_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    DJF_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera_djf[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    cont_era5_djf[season] = pd.read_csv(f"{pathIn}/ERA5/box60_max/all_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")

"""
#Obtain AVERAGE contingency tables for each threshold
cont_sphera_jja_0cols = pd.DataFrame(columns=summers)
cont_sphera_jja_5cols = pd.DataFrame(columns=summers)
cont_era5_jja_0cols = pd.DataFrame(columns=summers)
cont_era5_jja_5cols = pd.DataFrame(columns=summers)

cont_sphera_djf_0cols = pd.DataFrame(columns=winters)
cont_sphera_djf_5cols = pd.DataFrame(columns=winters)
cont_era5_djf_0cols = pd.DataFrame(columns=winters)
cont_era5_djf_5cols = pd.DataFrame(columns=winters)

for season in summers:
    cont_sphera_jja_0cols[season] = cont_sphera_jja[season]['0']    
    cont_sphera_jja_5cols[season] = cont_sphera_jja[season]['5']    
    cont_era5_jja_0cols[season] = cont_era5_jja[season]['0']    
    cont_era5_jja_5cols[season] = cont_era5_jja[season]['5']  

for season in winters:
    cont_sphera_djf_0cols[season] = cont_sphera_djf[season]['0']    
    cont_sphera_djf_5cols[season] = cont_sphera_djf[season]['5']    
    cont_era5_djf_0cols[season] = cont_era5_djf[season]['0']    
    cont_era5_djf_5cols[season] = cont_era5_djf[season]['5']  


cont_sphera_jja_MEAN = pd.DataFrame(columns=['0','5'])
cont_sphera_jja_MEAN['0'] = cont_sphera_jja_0cols.mean(axis=1)
cont_sphera_jja_MEAN['5'] = cont_sphera_jja_5cols.mean(axis=1)

cont_sphera_djf_MEAN = pd.DataFrame(columns=['0','5'])
cont_sphera_djf_MEAN['0'] = cont_sphera_djf_0cols.mean(axis=1)
cont_sphera_djf_MEAN['5'] = cont_sphera_djf_5cols.mean(axis=1)

cont_era5_jja_MEAN = pd.DataFrame(columns=['0','5'])
cont_era5_jja_MEAN['0'] = cont_era5_jja_0cols.mean(axis=1)
cont_era5_jja_MEAN['5'] = cont_era5_jja_5cols.mean(axis=1)

cont_era5_djf_MEAN = pd.DataFrame(columns=['0','5'])
cont_era5_djf_MEAN['0'] = cont_era5_djf_0cols.mean(axis=1)
cont_era5_djf_MEAN['5'] = cont_era5_djf_5cols.mean(axis=1)
"""

#Summing the cont tables all over the seasons 
cont_sphera_son_TOT =  cont_sphera_son['SON03']
cont_era5_son_TOT =  cont_era5_son['SON03']

for season in falls[1:]:   
    cont_sphera_son_TOT = cont_sphera_son[season] + cont_sphera_son_TOT
    cont_era5_son_TOT = cont_era5_son[season] + cont_era5_son_TOT
    
cont_sphera_mam_TOT =  cont_sphera_mam['MAM03']
cont_era5_mam_TOT =  cont_era5_mam['MAM03']

for season in springs[1:]:   
    cont_sphera_mam_TOT = cont_sphera_mam[season] + cont_sphera_mam_TOT
    cont_era5_mam_TOT = cont_era5_mam[season] + cont_era5_mam_TOT    

cont_sphera_djf_TOT =  cont_sphera_djf['DJF03']
cont_era5_djf_TOT =  cont_era5_djf['DJF03']

for season in winters[1:]:   
    cont_sphera_djf_TOT = cont_sphera_djf[season] + cont_sphera_djf_TOT
    cont_era5_djf_TOT = cont_era5_djf[season] + cont_era5_djf_TOT

cont_sphera_jja_TOT =  cont_sphera_jja['JJA03']
cont_era5_jja_TOT =  cont_era5_jja['JJA03']

for season in summers[1:]:   
    cont_sphera_jja_TOT = cont_sphera_jja[season] + cont_sphera_jja_TOT
    cont_era5_jja_TOT = cont_era5_jja[season] + cont_era5_jja_TOT


df_seasons = {}

for score in ['ts', 'pod', 'fa']:
    
    df_seasons[score] = {}
    
    for thr_ind in np.arange(0,9,1):
        #build dataframe to contain all values of e.g. TS at a certain threshold for all the seasons and the two reanalysis:
        df_seasons[score][thr_ind] = pd.DataFrame(index=np.arange(0,2*len(JJA_sphera),1),columns=['MAM','JJA','SON','DJF', 'year', 'dataset'])
        
        for ind in df_seasons[score][thr_ind].index[1::2]:    
            df_seasons[score][thr_ind]['dataset'][ind] = 'ERA5'
            df_seasons[score][thr_ind]['dataset'][ind-1] = 'SPHERA'
            
        for i,j in zip(df_seasons[score][thr_ind].index[0::2], np.arange(0,len(years),1)):
            df_seasons[score][thr_ind]['year'][i] = years[j]
            df_seasons[score][thr_ind]['year'][i+1] = years[j]
        
        for ind, s_ind in zip(df_seasons[score][thr_ind].index[1::2], np.arange(0,len(summers),1)):
            df_seasons[score][thr_ind]['JJA'][ind] = JJA_era5[summers[s_ind]][score][thr_ind]
            df_seasons[score][thr_ind]['JJA'][ind-1] = JJA_sphera[summers[s_ind]][score][thr_ind]
            
            df_seasons[score][thr_ind]['MAM'][ind] = MAM_era5[springs[s_ind]][score][thr_ind]
            df_seasons[score][thr_ind]['MAM'][ind-1] = MAM_sphera[springs[s_ind]][score][thr_ind]
            
            df_seasons[score][thr_ind]['SON'][ind] = SON_era5[falls[s_ind]][score][thr_ind]
            df_seasons[score][thr_ind]['SON'][ind-1] = SON_sphera[falls[s_ind]][score][thr_ind]
            
            
            if  (ind!=28) & (ind!=29):
                df_seasons[score][thr_ind]['DJF'][ind] = DJF_era5[winters[s_ind]][score][thr_ind]
                df_seasons[score][thr_ind]['DJF'][ind-1] = DJF_sphera[winters[s_ind]][score][thr_ind]
            else:
                df_seasons[score][thr_ind]['DJF'][ind] = np.nan
                df_seasons[score][thr_ind]['DJF'][ind-1] = np.nan


#check for -999.9 values and substitute with np.nan
for score in ['ts', 'pod', 'fa']:
    for thr_ind in np.arange(0,9,1):
        for seas in ['MAM','JJA','SON','DJF']:
            for i in df_seasons[score][thr_ind].index:
                if df_seasons[score][thr_ind][seas][i] == -999.9:
                    df_seasons[score][thr_ind][seas][i] = np.nan

#do the mean for a spec thresh and season on all the seasons for the years considered 
sphera_MAM_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
sphera_JJA_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
sphera_SON_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
sphera_DJF_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])

era5_MAM_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
era5_JJA_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
era5_SON_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])
era5_DJF_means = pd.DataFrame(index=np.arange(0,9,1), columns=['thr','ts','pod','fa'])

sphera_MAM_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
sphera_JJA_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
sphera_SON_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
sphera_DJF_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]

era5_MAM_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
era5_JJA_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
era5_SON_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]
era5_DJF_means['thr'] =  JJA_sphera['JJA03']['thr'][:9]

for score in ['ts','pod','fa']:
    
    for thr_ind in np.arange(0,9,1):
        sphera_MAM_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'SPHERA']['MAM'])       
        sphera_JJA_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'SPHERA']['JJA'])
        sphera_SON_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'SPHERA']['SON'])
        sphera_DJF_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'SPHERA']['DJF'])
        
        if df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['MAM'].isnull().all().all():
            era5_MAM_means[score][thr_ind] = np.nan
        else:
            era5_MAM_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['MAM'])
        
        if df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['JJA'].isnull().all().all():
            era5_JJA_means[score][thr_ind] = np.nan
        else:
            era5_JJA_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['JJA'])
        
        if df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['SON'].isnull().all().all():
            era5_SON_means[score][thr_ind] = np.nan
        else:
            era5_SON_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['SON'])
                
        if df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['DJF'].isnull().all().all():
            era5_DJF_means[score][thr_ind] = np.nan
        else:
            era5_DJF_means[score][thr_ind] = np.nanmean(df_seasons[score][thr_ind].loc[df_seasons[score][thr_ind]['dataset'].values == 'ERA5']['DJF'])
        
   
#SCEGLIERE STAGIONE PER PERF DIAGRAM:    
Seas = 'DJF'

if Seas == 'JJA':
    scores_sphera = sphera_JJA_means
    scores_era5 = era5_JJA_means
    cont_sphera = cont_sphera_jja_TOT
    cont_era5 = cont_era5_jja_TOT
    
elif Seas == 'DJF':
    scores_sphera = sphera_DJF_means
    scores_era5 = era5_DJF_means
    cont_sphera = cont_sphera_djf_TOT
    cont_era5 = cont_era5_djf_TOT
    
elif Seas == 'MAM':
    scores_sphera = sphera_MAM_means
    scores_era5 = era5_MAM_means
    cont_sphera = cont_sphera_mam_TOT
    cont_era5 = cont_era5_mam_TOT

elif Seas == 'SON':
    scores_sphera = sphera_SON_means
    scores_era5 = era5_SON_means
    cont_sphera = cont_sphera_son_TOT
    cont_era5 = cont_era5_son_TOT
    
    
cont_sphera = cont_sphera.where(pd.notnull(cont_sphera), None)
cont_era5 = cont_era5.where(pd.notnull(cont_era5), None)

plt.figure(figsize=(10, 7))
grid_ticks = np.arange(0, 1.01, 0.01)
sr_g, pod_g = np.meshgrid(grid_ticks, grid_ticks)
bias = pod_g / sr_g
csi = 1.0 / (1.0 / sr_g + 1.0 / pod_g - 1.0)
csi_contour = plt.contourf(sr_g, pod_g, csi, np.arange(0.1, 1.1, 0.1), extend="max", cmap='Greys')
b_contour = plt.contour(sr_g, pod_g, bias, [0.3, 0.5, 0.8, 1, 1.3, 1.5, 2, 4], colors="k", linestyles="dashed", linewidths=0.5)
plt.clabel(b_contour, fmt="%1.1f", 
           manual=[(0.23, 0.95), (0.43, 0.95), (0.63, 0.95), (0.72,0.95), (0.8, 0.8), (0.85, 0.67), (0.9, 0.45), (0.75,0.22)])

markers = itertools.cycle(['o','^','s','D','h','8','v','p','P']) 

#colors = itertools.cycle(['black', 'red', 'green', 'blue', 'orange', 'purple', 'brown', 'grey', 'aqua'])
    

for thresh in np.arange(0,9,1):
    
    marker = next(markers)
        
    #colors = itertools.cycle(['#87489D', '#32AAB5',]) 
 
    color = '#87489D' #next(colors)
    
    aaa=1
        
    if thresh == 0:
        ct_sphera = cont_sphera.loc[0:1]
    elif thresh == 1:
        ct_sphera= cont_sphera.loc[3:4]
    elif thresh == 2:
        ct_sphera = cont_sphera.loc[6:7]
    elif thresh == 3:
        ct_sphera = cont_sphera.loc[9:10]
    elif thresh == 4:
        ct_sphera = cont_sphera.loc[12:13]
    elif thresh == 5:
        ct_sphera = cont_sphera.loc[15:16]
    elif thresh == 6:
        ct_sphera = cont_sphera.loc[18:19]
        aaa = cont_sphera.loc[18:19]['0'][18]
    elif thresh == 7:
        ct_sphera = cont_sphera.loc[21:22]
        aaa = cont_sphera.loc[21:22]['0'][21]
    elif thresh == 8:
        ct_sphera = cont_sphera.loc[24:25]
        aaa = cont_sphera.loc[24:25]['0'][24]

    if aaa != None:
    
        #read the contingency table as R matrix
        cont_vec = ro.IntVector([int(ct_sphera.iloc[0,0]),int(ct_sphera.iloc[1,0]),int(ct_sphera.iloc[0,1]),
                         int(ct_sphera.iloc[1,1])])
        m = ro.r.matrix(cont_vec,nrow=2, ncol = 2)
        
        #apply bootstrap resampling to the contingency table to calculate the confidence intervals of POD and FAR 
        boot = ro.r('table.stats.boot')
        bootstrap = boot(m, R=1000)
                
        #extract values from R bootstrap function to save in a pd.DataFrame
        error_bars = pd.DataFrame(columns=['pod','sr'])
        
        error_bars.loc[0,'pod'] = bootstrap[0]
        error_bars.loc[1,'pod'] = bootstrap[1]
        error_bars.loc[0,'sr'] = 1-bootstrap[3]
        error_bars.loc[1,'sr'] = 1-bootstrap[2]
        
        #plot value with errorbars
        x = 1 - scores_sphera.loc[thresh].fa
        y = scores_sphera.loc[thresh].pod
        yerr = [[y - error_bars.loc[1,'pod']],[error_bars.loc[0,'pod'] - y]]
        xerr = [[x - error_bars.loc[1,'sr']],[error_bars.loc[0,'sr'] - x]]
        
        plt.errorbar(x, y, yerr = yerr, xerr = xerr,  marker=marker, markersize=12, color=color, 
                         linestyle='', label=f'{float(scores_sphera.loc[thresh].thr)}')
  
markers = itertools.cycle(['o','^','s','D','h','8','v','p','P']) 

for thresh in np.arange(0,7,1):
    
    marker = next(markers)
     
    color = '#32AAB5' #next(colors)

    aaa=1
    
    if thresh == 0:
        ct_era5 = cont_era5.loc[0:1]
    elif thresh == 1:
        ct_era5= cont_era5.loc[3:4]
    elif thresh == 2:
        ct_era5 = cont_era5.loc[6:7]
    elif thresh == 3:
        ct_era5 = cont_era5.loc[9:10]
    elif thresh == 4:
        ct_era5 = cont_era5.loc[12:13]
    elif thresh == 5:
        ct_era5 = cont_era5.loc[15:16]
    elif thresh == 6:
        ct_era5 = cont_era5.loc[18:19]
        aaa = cont_era5.loc[18:19]['0'][18]
    elif thresh == 7:
        ct_era5 = cont_era5.loc[21:22]
        aaa = cont_era5.loc[21:22]['0'][21]
    elif thresh == 8:
        ct_era5 = cont_era5.loc[24:25]
        aaa = cont_era5.loc[24:25]['0'][24]

    if aaa != None:
            
        #read the contingency table as R matrix
        cont_vec = ro.IntVector([int(ct_era5.iloc[0,0]),int(ct_era5.iloc[1,0]),int(ct_era5.iloc[0,1]),int(ct_era5.iloc[1,1])])
        m = ro.r.matrix(cont_vec,nrow=2, ncol = 2)
        
        #apply bootstrap resampling to the contingency table to calculate the confidence intervals of POD and FAR 
        boot = ro.r('table.stats.boot')
        bootstrap = boot(m, R=1000)
                
        #extract values from R bootstrap function to save in a pd.DataFrame
        error_bars = pd.DataFrame(columns=['pod','sr'])
        
        error_bars.loc[0,'pod'] = bootstrap[0]
        error_bars.loc[1,'pod'] = bootstrap[1]
        error_bars.loc[0,'sr'] = 1-bootstrap[3]
        error_bars.loc[1,'sr'] = 1-bootstrap[2]
        
        #plot value with errorbars
        x = 1 - scores_era5.loc[thresh].fa
        y = scores_era5.loc[thresh].pod
        yerr = [[y - error_bars.loc[1,'pod']],[error_bars.loc[0,'pod'] - y]]
        xerr = [[x - error_bars.loc[1,'sr']],[error_bars.loc[0,'sr'] - x]]
        
        plt.errorbar(x, y, yerr = yerr, xerr = xerr,  marker=marker, markersize=12, color=color, 
                         linestyle='')

cbar = plt.colorbar(csi_contour)
cbar.ax.tick_params(labelsize=14) 
cbar.set_label('Threat Score (TS)', fontsize=17)
plt.xlabel('Success Ratio (1-FAR)', fontsize=17)
plt.ylabel('Probability of detection (POD)', fontsize=17)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
#plt.title(f'{Seas} average over 2003-2017', fontsize=22)#, fontweight="bold")
plt.tick_params(axis='both', which='major', labelsize=14)
    
plt.text(0.67,0.57,"Frequency Bias",fontdict=dict(fontsize=15, rotation=37))

legend = plt.legend(title='Threshold \n[mm/hour]', **dict(loc='upper left', fontsize=15, framealpha=0.85, frameon=True))
plt.setp(legend.get_title(),fontsize=15)
ax = plt.gca().add_artist(legend)

#legenda per le due diverse rianalisi
#l1, = plt.plot(1 - scores_sphera.loc[0].fa, scores_sphera.loc[0].pod, linestyle='', marker='o', markersize=12, color='black', 
#               label='SPHERA')
#l2, = plt.plot(1 - scores_era5.loc[0].fa, scores_era5.loc[0].pod, marker='o', linestyle='',  mfc='none', markersize=12, 
#               markeredgewidth=2, color='black', label='ERA5')
#plt.legend(handles=[l1,l2], loc='upper right', fontsize=15)

plt.savefig(f'{pathOut}/PerfDiag_{Seas}_hourly_box60max_V2.pdf', bbox_inches="tight", dpi=300)


