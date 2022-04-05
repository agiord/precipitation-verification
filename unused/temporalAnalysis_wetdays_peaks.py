import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import itertools


#SCRIPT PER STUDIARE L'ANDAMENTO NEL TEMPO E I CAMBIAMENTI TEMPORALI DEL NUMERO DI GIORNI WET E NUMERO DI GIORNI CON EVENTI DI PICCO
#FONDAMENTALE: DARE DEFINIZIOE CORRETTA DI WET DAY NEL NOSTRO CONTESTO (per ora tengo wet day=giorno in cui cumulata preci >=1mm), E
#DEFINIZIONE CORRETTA DI GIORNO CON EVENTO DI PICCO: SUPERAMENTO DI UNA CERTA SOGLIA ALTA E.G. 100-200 MM/DAY???


dataset='DEWETRA'
aggr = 'max'  #'max'

pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/{dataset}'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/temporalAnalysis'


seasons1 = ['MAM03', 'JJA03', 'SON03', 'DJF03', 'MAM04', 'JJA04', 'SON04', 'DJF04', 'MAM05', 'JJA05', 'SON05', 
           'DJF05', 'MAM06', 'JJA06', 'SON06']
seasons2 = ['MAM07', 'JJA07', 'SON07', 'DJF07', 'MAM08', 'JJA08', 'SON08', 'DJF08', 'MAM09', 'JJA09', 'SON09', 
           'DJF09', 'MAM10', 'JJA10', 'SON10']
seasons3 = ['MAM11', 'JJA11', 'SON11', 'DJF11', 'MAM12', 'JJA12', 'SON12', 'DJF12', 'MAM13', 'JJA13', 'SON13', 
           'DJF13', 'MAM14', 'JJA14', 'SON14']  
seasons4 = ['MAM15', 'JJA15', 'SON15', 'DJF15', 'MAM16', 'JJA16', 'SON16', 'DJF16', 'MAM17', 'JJA17', 'SON17'] 

seasons=seasons1+seasons2+seasons3+seasons4

winters = ['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']
summers = ['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14',
           'JJA15', 'JJA16', 'JJA17']
springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14',
           'MAM15', 'MAM16', 'MAM17']
falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14',
         'SON15', 'SON16', 'SON17']

years = ['2003','2004','2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']


seas_sphera = {}
seas_era5 = {}

cont_sphera = {}
cont_era5 = {}   

for season in seasons:
    #leggi i scores_per_scad.dat di SPHERA ed ERA5
    seas_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    seas_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/scores_per_scad.dat",
                               skiprows=4, sep="\s+")
    
    
    #upload contingency tables and extract them for each threshold   
    cont_sphera[season] = pd.read_csv(f"{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
    cont_era5[season] = pd.read_csv(f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat",
                               skiprows=0, sep="\s+")
    
#CALCOLO PER OGNI STAGIONE DEL NUMERO DI EVENTI FORECASTATI DA SPHERA CON SOGLIA 1mm ECCEDUTA (a+b in cont table) 
#NORMALIZZATO CO IL NUMERO TOTALE DI EVENTI (a+b+c+d in cont table) -> Questo dato rappresenta la frazione di eventi simulati da modello
#che hanno ecceduto la soglia NON  il numero di wet days perchè stiamo considerando gli eventi su TOT box (quante sono??) COME OTTENERE
#NUMERO DI WET DAYS?????? INFORMARSI IN LETTEREATURA

N_event_wet_SPHERA = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_wet_ERA5 = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_wet_obs = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])
    
i=0
for season in seasons:
    
    N_event_wet_SPHERA['season'][i] = season
    N_event_wet_ERA5['season'][i] = season
    N_event_wet_obs['season'][i] = season


    N_event_wet_SPHERA['n'][i] = cont_sphera[season].loc[0].sum()/(cont_sphera[season].loc[0].sum() + cont_sphera[season].loc[1].sum())
    N_event_wet_ERA5['n'][i] = cont_era5[season].loc[0].sum()/(cont_era5[season].loc[0].sum() + cont_era5[season].loc[1].sum())
    N_event_wet_obs['n'][i] = (cont_sphera[season].loc[0][0] + cont_sphera[season].loc[1][0])/(cont_sphera[season].loc[0].sum() + cont_sphera[season].loc[1].sum())
    
    i=i+1
    
  #  N_event_wet_SPHERA = N_event_wet_SPHERA[:15]
  #  N_event_wet_ERA5 = N_event_wet_ERA5[:15]

#USING THE MAX: PEAK: pp>50mm/day    
N_event_peak_SPHERA = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_peak_ERA5 = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_peak_obs = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])
    
i=0
for season in seasons:
    
    N_event_peak_SPHERA['season'][i] = season
    N_event_peak_ERA5['season'][i] = season
    N_event_peak_obs['season'][i] = season


    N_event_peak_SPHERA['n'][i] = cont_sphera[season].loc[15].sum()/(cont_sphera[season].loc[15].sum() + cont_sphera[season].loc[16].sum())
    N_event_peak_ERA5['n'][i] = cont_era5[season].loc[15].sum()/(cont_era5[season].loc[15].sum() + cont_era5[season].loc[16].sum())
    N_event_peak_obs['n'][i] = (cont_sphera[season].loc[15][0] + cont_sphera[season].loc[16][0])/(cont_sphera[season].loc[15].sum() + cont_sphera[season].loc[16].sum())
    
    i=i+1


#USING THE MEAN: PEAK: pp>25mm/day    
N_event_peak_SPHERA = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_peak_ERA5 = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])    
N_event_peak_obs = pd.DataFrame(index=np.arange(0,len(seasons),1), columns=['season','n'])
    
i=0
for season in seasons:
    
    N_event_peak_SPHERA['season'][i] = season
    N_event_peak_ERA5['season'][i] = season
    N_event_peak_obs['season'][i] = season


    N_event_peak_SPHERA['n'][i] = cont_sphera[season].loc[12].sum()/(cont_sphera[season].loc[12].sum() + cont_sphera[season].loc[13].sum())
    N_event_peak_ERA5['n'][i] = cont_era5[season].loc[12].sum()/(cont_era5[season].loc[12].sum() + cont_era5[season].loc[13].sum())
    N_event_peak_obs['n'][i] = (cont_sphera[season].loc[12][0] + cont_sphera[season].loc[13][0])/(cont_sphera[season].loc[12].sum() + cont_sphera[season].loc[13].sum())
    
    i=i+1


















    
#WET DAYS pp>1mm/day    
fig, ax1 = plt.subplots(figsize=(15,6))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
#ax1.set_ylim(0,0.65)
ax1.plot(N_event_wet_SPHERA['season'], N_event_wet_SPHERA['n'], '-o',  markersize=4, color='red', label='SPHERA')
plt.axhline(y=N_event_wet_SPHERA['n'].mean(), linestyle='--', color='red', label='SPHERA clim')

ax1.plot(N_event_wet_ERA5['season'], N_event_wet_ERA5['n'], '-o',  markersize=4, color='blue', label='ERA5')
plt.axhline(y=N_event_wet_ERA5['n'].mean(), linestyle='--', color='blue', label='ERA5 clim')

ax1.plot(N_event_wet_obs['season'], N_event_wet_obs['n'], '-o',  markersize=4, color='orange', label='OBS')
plt.axhline(y=N_event_wet_obs['n'].mean(), linestyle='--', color='orange', label='OBS clim')


ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 14)
ax1.set_xlabel('Season', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Fcst yes/Tot events > 1 mm/day')
plt.title(f'Temporal frequency of number of wet events (pp>1 mm/day), using the MAX, 2003-2017 ({dataset})', fontsize=17)


plt.savefig(f'{pathOut}/fcstYes_freq1mm_{dataset}_2003-2017_box60{aggr}.png', bbox_inches="tight")

    


#PEAK DAYS pp>50mm/day
fig, ax1 = plt.subplots(figsize=(15,6))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
#ax1.set_ylim(0,0.65)
ax1.plot(N_event_peak_SPHERA['season'], N_event_peak_SPHERA['n'], '-o',  markersize=4, color='red', label='SPHERA')
plt.axhline(y=N_event_peak_SPHERA['n'].mean(), linestyle='--', color='red', label='SPHERA clim')

ax1.plot(N_event_peak_ERA5['season'], N_event_peak_ERA5['n'], '-o',  markersize=4, color='blue', label='ERA5')
plt.axhline(y=N_event_peak_ERA5['n'].mean(), linestyle='--', color='blue', label='ERA5 clim')

ax1.plot(N_event_peak_obs['season'], N_event_peak_obs['n'], '-o',  markersize=4, color='orange', label='OBS')
plt.axhline(y=N_event_peak_obs['n'].mean(), linestyle='--', color='orange', label='OBS clim')


ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 14)
ax1.set_xlabel('Season', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Fcst yes/Tot events > 50 mm/day')
plt.title(f'Temporal frequency of number of peak events (pp>50 mm/day), using the MAX, 2003-2017 ({dataset})', fontsize=17)


plt.savefig(f'{pathOut}/fcstYes_freq50mm_{dataset}_2003-2017_box60{aggr}.png', bbox_inches="tight")
    
    
    

#USING THE MEAN VALUES OF THE BOX: PEAK DAYS pp>25mm/day
fig, ax1 = plt.subplots(figsize=(15,6))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
#ax1.set_ylim(0,0.65)
ax1.plot(N_event_peak_SPHERA['season'], N_event_peak_SPHERA['n'], '-o',  markersize=4, color='red', label='SPHERA')
plt.axhline(y=N_event_peak_SPHERA['n'].mean(), linestyle='--', color='red', label='SPHERA clim')

ax1.plot(N_event_peak_ERA5['season'], N_event_peak_ERA5['n'], '-o',  markersize=4, color='blue', label='ERA5')
plt.axhline(y=N_event_peak_ERA5['n'].mean(), linestyle='--', color='blue', label='ERA5 clim')

ax1.plot(N_event_peak_obs['season'], N_event_peak_obs['n'], '-o',  markersize=4, color='orange', label='OBS')
plt.axhline(y=N_event_peak_obs['n'].mean(), linestyle='--', color='orange', label='OBS clim')


ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 14)
ax1.set_xlabel('Season', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Fcst yes/Tot events > 25 mm/day')
plt.title(f'Temporal frequency of number of peak events (pp>25 mm/day), using the MEAN, 2003-2017 ({dataset})', fontsize=17)


plt.savefig(f'{pathOut}/fcstYes_freq50mm_{dataset}_2003-2017_box60{aggr}.png', bbox_inches="tight")
        
    