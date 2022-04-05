import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

"""
Script per plottare:
- cumulata preci per soglia
- istogramma di frequenze relative come funzione di intervalli di soglie di preci nei bin
"""

#Importa file .dat con i dati di osservate e previste
#PROVA PER DJF11, SCORES_PER_SCAD E SCATTER_PLOT
#df_sphera = pd.read_fwf("/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/scores_2011-2014/oper2015/DJF11/scores_per_scad.dat",
#                          skiprows=5, names=['thr','npo','nos','bs','hr','ts','pod','fa','rnd_ts', 'rnd_fa','hss', 'rmserr','bias'])

#df_era5 = pd.read_fwf("/media/ciccuz/Volume/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/scores_2011-2014/era5/DJF11/scores_per_scad.dat",
#                          skiprows=5, names=['thr','npo','nos','bs','hr','ts','pod','fa','rnd_ts', 'rnd_fa','hss', 'rmserr','bias'])

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati/ARCIS'
pathOut='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/cumulata_prec_per_soglia/vs_ARCIS/box60'

#set season:
season='2007-2010_complete'


#NEGLI scatter_plot.dat LA PRIMA COLONNA SONO OBS E SECONDA PREVISTE (giusto)

#per leggere non usare pd.read_fwf!!!! TAGLIA VIA DATI CON VALORI PIU ALTI!!! usare pd.read_csv
df_sphera_sc = pd.read_csv(f"{pathIn}/SPHERA_box60/2007-2010/{season}/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_era5_sc = pd.read_csv(f"{pathIn}/ERA5_box60/2007-2010/{season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])





df_sphera_sc_2003_2006 = pd.read_csv(f"{pathIn}/SPHERA_box60/2003-2006/2003-2006_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_era5_sc_2003_2006 = pd.read_csv(f"{pathIn}/ERA5_box60/2003-2006/2003-2006_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2007_2010 = pd.read_csv(f"{pathIn}/SPHERA_box60/2007-2010/2007-2010_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_era5_sc_2007_2010 = pd.read_csv(f"{pathIn}/ERA5_box60/2007-2010/2007-2010_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2011_2014 = pd.read_csv(f"{pathIn}/SPHERA_box60/2011-2014/2011-2014_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_era5_sc_2011_2014 = pd.read_csv(f"{pathIn}/ERA5_box60/2011-2014/2011-2014_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2015_2017 = pd.read_csv(f"{pathIn}/SPHERA_box60/2015-2017/2015-2017_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_era5_sc_2015_2017 = pd.read_csv(f"{pathIn}/ERA5_box60/2015-2017/2015-2017_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])








def funct_distr(df_sphera_sc, df_era5_sc, thresh=[1.0,5.0,10.0,20.0,40.0,60.0,100.0]):

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
    #thresh = np.arange(5.0,155.0,5.0)
    #thresh = [1.0,5.0,10.0,20.0,40.0,60.0,80.0,100.0,150.0]
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
                if float(df['obs'].loc[i]) <= thresh[0]:
                    count_obs[0] = count_obs[0] + 1
                    break
                
                elif float(df['obs'].loc[i]) > thresh[-1]:
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
                
                elif float(df['prev'].loc[i]) > thresh[-1]:
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
    

funct = funct_distr(df_sphera_sc_2011_2014, df_era5_sc_2011_2014)

count_obs_era5 = funct[0]
count_obs_sphera = funct[1]
count_prev_era5 = funct[2]
count_prev_sphera = funct[3]

#per fare check: fare la somma di tutti i valori dentro count_obs/count_prev e la lunghezza delle colonne del df,
#escludendo i valori = 0.0:
#sum(count_obs_sphera) == len(df_sphera_sc['obs'].loc[df_sphera_sc['obs'] != 0.0])
#sum(count_prev_sphera) == len(df_sphera_sc['prev'].loc[df_sphera_sc['prev'] != 0.0])

#sum(count_obs_era5) == len(df_era5_sc['obs'].loc[df_era5_sc['obs'] != 0.0])
#sum(count_prev_era5) == len(df_era5_sc['prev'].loc[df_era5_sc['prev'] != 0.0])


#PLOT
fig, ax = plt.subplots(1, 1, figsize=(8,4))

plt.rcParams.update({'font.size': 14})

plt.xlabel('Daily-cumulated precipitation threshold [mm]', fontsize=15)
plt.ylabel('Cases with exceeded threshold', fontsize=15)

#log y scale
plt.yscale('log')

#set only lower limit on y scale
ax.set_ylim([0.5,400000])
ax.set_xlim([-0.1,30.1])
plt.xticks(np.arange(0, len(count_obs_era5), 2))
plt.title(f'Rainfall distributions 2003-2014', fontsize=20)   #10 years: 2007-2017

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
ax.tick_params(axis='both', which='major', labelsize=13)
#ax.tick_params(axis='x', which='major', rotation=30)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right" )

ax.grid(True, linestyle='--', lw=0.75)

plt.legend(loc='best')

plt.savefig(f'{pathOut}/rainfall_dist_2003-2014.png', bbox_inches='tight')






funct2003_06 = funct(df_sphera_sc_2003_2006, df_era5_sc_2003_2006)
funct2007_10 = funct(df_sphera_sc_2007_2010, df_era5_sc_2007_2010)
funct2011_14 = funct(df_sphera_sc_2011_2014, df_era5_sc_2011_2014)
funct2015_17 = funct(df_sphera_sc_2015_2017, df_era5_sc_2015_2017)


count_obs_era5_2003_2006 = funct2003_06[0]
count_obs_sphera_2003_2006 = funct2003_06[1]
count_prev_era5_2003_2006 = funct2003_06[2]
count_prev_sphera_2003_2006 = funct2003_06[3]

count_obs_era5_2007_2010 = funct2007_10[0]
count_obs_sphera_2007_2010 = funct2007_10[1]
count_prev_era5_2007_2010 = funct2007_10[2]
count_prev_sphera_2007_2010 = funct2007_10[3]

count_obs_era5_2011_2014 = funct2011_14[0]
count_obs_sphera_2011_2014 = funct2011_14[1]
count_prev_era5_2011_2014 = funct2011_14[2]
count_prev_sphera_2011_2014 = funct2011_14[3]

count_obs_era5_2015_2017 = funct2015_17[0]
count_obs_sphera_2015_2017 = funct2015_17[1]
count_prev_era5_2015_2017 = funct2015_17[2]
count_prev_sphera_2015_2017 = funct2015_17[3]


count_obs_era5 = count_obs_era5_2003_2006 + count_obs_era5_2007_2010 + count_obs_era5_2011_2014# + count_obs_era5_2015_2017
count_obs_sphera = count_obs_sphera_2003_2006 + count_obs_sphera_2007_2010 + count_obs_sphera_2011_2014# + count_obs_sphera_2015_2017
count_prev_era5 = count_prev_era5_2003_2006 + count_prev_era5_2007_2010 + count_prev_era5_2011_2014# + count_prev_era5_2015_2017
count_prev_sphera = count_prev_sphera_2003_2006 + count_prev_sphera_2007_2010 + count_prev_sphera_2011_2014# + count_prev_sphera_2015_2017









"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
GRAFICO PARAGONE DEWETRA VS ARCIS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#SCEGLIERE MEDIE O MASSIMI DELLE BOX (avg O max)
aggr='mean'   # o max


pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/dati'
pathOut=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/cumulata_prec_per_soglia/box_{aggr}'



df_sphera_sc_2003_2006_arcis = pd.read_csv(f"{pathIn}/ARCIS/SPHERA/box60_{aggr}/2003-2006/2003-2006_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2003_2006_arcis = pd.read_csv(f"{pathIn}/ARCIS/ERA5/box60_{aggr}/2003-2006/2003-2006_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2007_2010_arcis = pd.read_csv(f"{pathIn}/ARCIS/SPHERA/box60_{aggr}/2007-2010/2007-2010_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2007_2010_arcis = pd.read_csv(f"{pathIn}/ARCIS/ERA5/box60_{aggr}/2007-2010/2007-2010_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2011_2014_arcis = pd.read_csv(f"{pathIn}/ARCIS/SPHERA/box60_{aggr}/2011-2014/2011-2014_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2011_2014_arcis = pd.read_csv(f"{pathIn}/ARCIS/ERA5/box60_{aggr}/2011-2014/2011-2014_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])





df_sphera_sc_2003_2006_dew = pd.read_csv(f"{pathIn}/DEWETRA/SPHERA/box60_{aggr}/2003-2006/2003-2006_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2003_2006_dew = pd.read_csv(f"{pathIn}/DEWETRA/ERA5/box60_{aggr}/2003-2006/2003-2006_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2007_2010_dew = pd.read_csv(f"{pathIn}/DEWETRA/SPHERA/box60_{aggr}/2007-2010/2007-2010_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2007_2010_dew = pd.read_csv(f"{pathIn}/DEWETRA/ERA5/box60_{aggr}/2007-2010/2007-2010_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


df_sphera_sc_2011_2014_dew = pd.read_csv(f"{pathIn}/DEWETRA/SPHERA/box60_{aggr}/2011-2014/2011-2014_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2011_2014_dew = pd.read_csv(f"{pathIn}/DEWETRA/ERA5/box60_{aggr}/2011-2014/2011-2014_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])

df_sphera_sc_2015_2017_dew = pd.read_csv(f"{pathIn}/DEWETRA/SPHERA/box60_{aggr}/2015-2017/2015-2017_complete/scatter_plot.dat",# {season}/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])
df_era5_sc_2015_2017_dew = pd.read_csv(f"{pathIn}/DEWETRA/ERA5/box60_{aggr}/2015-2017/2015-2017_complete/scatter_plot.dat",
                           skiprows=1, sep="\s+", names=['obs','prev'])


funct2003_06_arcis = funct_distr(df_sphera_sc_2003_2006_arcis, df_era5_sc_2003_2006_arcis)
funct2007_10_arcis = funct_distr(df_sphera_sc_2007_2010_arcis, df_era5_sc_2007_2010_arcis)
funct2011_14_arcis = funct_distr(df_sphera_sc_2011_2014_arcis, df_era5_sc_2011_2014_arcis)

funct2003_06_dew = funct_distr(df_sphera_sc_2003_2006_dew, df_era5_sc_2003_2006_dew)
funct2007_10_dew = funct_distr(df_sphera_sc_2007_2010_dew, df_era5_sc_2007_2010_dew)
funct2011_14_dew = funct_distr(df_sphera_sc_2011_2014_dew, df_era5_sc_2011_2014_dew)
funct2015_17_dew = funct_distr(df_sphera_sc_2015_2017_dew, df_era5_sc_2015_2017_dew)



count_obs_era5_2003_2006_arcis = funct2003_06_arcis[0]
count_obs_sphera_2003_2006_arcis = funct2003_06_arcis[1]
count_prev_era5_2003_2006_arcis = funct2003_06_arcis[2]
count_prev_sphera_2003_2006_arcis = funct2003_06_arcis[3]

count_obs_era5_2007_2010_arcis = funct2007_10_arcis[0]
count_obs_sphera_2007_2010_arcis = funct2007_10_arcis[1]
count_prev_era5_2007_2010_arcis = funct2007_10_arcis[2]
count_prev_sphera_2007_2010_arcis = funct2007_10_arcis[3]

count_obs_era5_2011_2014_arcis = funct2011_14_arcis[0]
count_obs_sphera_2011_2014_arcis = funct2011_14_arcis[1]
count_prev_era5_2011_2014_arcis = funct2011_14_arcis[2]
count_prev_sphera_2011_2014_arcis = funct2011_14_arcis[3]



count_obs_era5_2003_2006_dew = funct2003_06_dew[0]
count_obs_sphera_2003_2006_dew = funct2003_06_dew[1]
count_prev_era5_2003_2006_dew = funct2003_06_dew[2]
count_prev_sphera_2003_2006_dew = funct2003_06_dew[3]

count_obs_era5_2007_2010_dew = funct2007_10_dew[0]
count_obs_sphera_2007_2010_dew = funct2007_10_dew[1]
count_prev_era5_2007_2010_dew = funct2007_10_dew[2]
count_prev_sphera_2007_2010_dew = funct2007_10_dew[3]

count_obs_era5_2011_2014_dew = funct2011_14_dew[0]
count_obs_sphera_2011_2014_dew = funct2011_14_dew[1]
count_prev_era5_2011_2014_dew = funct2011_14_dew[2]
count_prev_sphera_2011_2014_dew = funct2011_14_dew[3]

count_obs_era5_2015_2017_dew = funct2015_17_dew[0]
count_obs_sphera_2015_2017_dew = funct2015_17_dew[1]
count_prev_era5_2015_2017_dew = funct2015_17_dew[2]
count_prev_sphera_2015_2017_dew = funct2015_17_dew[3]



TOT_count_obs_era5_arcis = count_obs_era5_2003_2006_arcis + count_obs_era5_2007_2010_arcis + count_obs_era5_2011_2014_arcis# + count_obs_era5_2015_2017
TOT_count_obs_sphera_arcis = count_obs_sphera_2003_2006_arcis + count_obs_sphera_2007_2010_arcis + count_obs_sphera_2011_2014_arcis# + count_obs_sphera_2015_2017
TOT_count_prev_era5_arcis = count_prev_era5_2003_2006_arcis + count_prev_era5_2007_2010_arcis + count_prev_era5_2011_2014_arcis# + count_prev_era5_2015_2017
TOT_count_prev_sphera_arcis = count_prev_sphera_2003_2006_arcis + count_prev_sphera_2007_2010_arcis + count_prev_sphera_2011_2014_arcis# + count_prev_sphera_2015_2017


TOT_count_obs_era5_dew = count_obs_era5_2003_2006_dew + count_obs_era5_2007_2010_dew + count_obs_era5_2011_2014_dew + count_obs_era5_2015_2017_dew
TOT_count_obs_sphera_dew = count_obs_sphera_2003_2006_dew + count_obs_sphera_2007_2010_dew + count_obs_sphera_2011_2014_dew + count_obs_sphera_2015_2017_dew
TOT_count_prev_era5_dew = count_prev_era5_2003_2006_dew + count_prev_era5_2007_2010_dew + count_prev_era5_2011_2014_dew + count_prev_era5_2015_2017_dew
TOT_count_prev_sphera_dew = count_prev_sphera_2003_2006_dew + count_prev_sphera_2007_2010_dew + count_prev_sphera_2011_2014_dew + count_prev_sphera_2015_2017_dew





#PLOT
fig, ax = plt.subplots(1, 1, figsize=(10,6))

plt.rcParams.update({'font.size': 14})

plt.xlabel('Daily-cumulated precipitation threshold [mm]', fontsize=15)
plt.ylabel('Cases with exceeded threshold', fontsize=15)

#log y scale
plt.yscale('log')

#set only lower limit on y scale
ax.set_ylim([0.5,400000])
#ax.set_xlim([-0.1,30.1])
plt.xticks(np.arange(0, len(TOT_count_obs_era5_dew), 2))
plt.title(f'Rainfall distributions 2003-2014', fontsize=20)   #10 years: 2007-2017

#ax.plot(np.arange(0,len(count_obs_era5)), count_obs_era5, label='OBS ERA5', color='blue', lw=1.5)
ax.plot(np.arange(0,len(TOT_count_obs_sphera_dew)), TOT_count_obs_sphera_dew, label='OBS', color='black', lw=1.5)
ax.plot(np.arange(0,len(TOT_count_prev_era5_dew)), TOT_count_prev_era5_dew, label='ERA5', color='#87489D', lw=1.8)
ax.plot(np.arange(0,len(TOT_count_prev_sphera_dew)), TOT_count_prev_sphera_dew, label='SPHERA', color='#32AAB5', lw=1.8)

#ax.plot(np.arange(0,len(count_obs_era5)), count_obs_era5, label='OBS ERA5', color='blue', lw=1.5)
ax.plot(np.arange(0,len(TOT_count_obs_sphera_arcis)), TOT_count_obs_sphera_arcis, color='black', lw=1.5, linestyle='--')
ax.plot(np.arange(0,len(TOT_count_prev_era5_arcis)), TOT_count_prev_era5_arcis, color='#87489D', lw=1.8, linestyle='--')
ax.plot(np.arange(0,len(TOT_count_prev_sphera_arcis)), TOT_count_prev_sphera_arcis, color='#32AAB5', lw=1.8, linestyle='--')


#thresh_intervals_labels = ['<5', '5-10', '10-15', '15-20', '20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65',
#                   '65-70','70-75','75-80','80-85','85-90','90-95','95-100','100-105','105-110','110-115','115-120','120-125',
#                   '125-130','130-135','135-140','140-145','145-150','>150']

thresh_intervals_labels2 = thresh_intervals #['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-105',
                           #'110-115','120-125','130-135','140-145','>150']

#thresh_intervals_labels3 = ['<5', '10-15','20-25', '30-35','40-45','50-55','60-65','70-75','80-85','90-95','100-110', '',
#                            '120-130','','140-150','>150']

ax.set_xticklabels(thresh_intervals_labels2)
ax.tick_params(axis='both', which='major', labelsize=13)
#ax.tick_params(axis='x', which='major', rotation=30)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha="right" )

ax.grid(True, linestyle='--', lw=0.75)

plt.legend(loc='best')


ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot([1,1], [1.5,2], linestyle='-', color='black', label='DEWETRA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='--', color='black', label='ARCIS', scaley=False)
ax1.legend(title='OBS DATASET', handles=[l1,l2], loc='lower left', fontsize=15)

plt.savefig(f'{pathOut}/rainfall_dist_2003-2014_DEW_v_ARC.png', bbox_inches='tight')








#NORMALIZED PLOT OF ABSOLUTE DIFFERENCE IN PRECIPITATION DISTRIBUTION:
    
fig, ax = plt.subplots(1, 1, figsize=(10,6))

plt.rcParams.update({'font.size': 14})

plt.xlabel('Daily-cumulated precipitation threshold [mm]')
plt.ylabel('|REANALYSIS - OBS| (cases with exceeded threshold)')

#log y scale
#plt.yscale('log')

#set only lower limit on y scale
#ax.set_ylim([0.5,400000])
ax.set_xlim([-0.1,30.1])
plt.xticks(np.arange(0, len(TOT_count_obs_sphera_dew), 2))
plt.title(f'Normalized abs. difference in rainfall distributions, 2003-2014', fontsize=18)   #10 years: 2007-2017


ax.plot(np.arange(0,len(TOT_count_obs_sphera_dew)), abs(TOT_count_prev_sphera_dew - TOT_count_obs_sphera_dew)/TOT_count_obs_sphera_dew, 
        label='SPHERA', color='#32AAB5', lw=1.5)
ax.plot(np.arange(0,len(TOT_count_obs_sphera_arcis)), abs(TOT_count_prev_sphera_arcis - TOT_count_obs_sphera_arcis)/TOT_count_obs_sphera_arcis, 
         color='#32AAB5', lw=1.5, linestyle='--')

ax.plot(np.arange(0,len(TOT_count_obs_era5_dew)), abs(TOT_count_prev_era5_dew - TOT_count_obs_era5_dew)/TOT_count_obs_era5_dew, 
        label='ERA5', color='#87489D', lw=1.5)
ax.plot(np.arange(0,len(TOT_count_obs_era5_arcis)), abs(TOT_count_prev_era5_arcis - TOT_count_obs_era5_arcis)/TOT_count_obs_era5_arcis, 
        color='#87489D', lw=1.5, linestyle='--')


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

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot([1,1], [1.5,2], linestyle='-', color='black', label='DEWETRA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='--', color='black', label='ARCIS', scaley=False)
ax1.legend(title='OBS DATASET', handles=[l1,l2], loc='lower right', fontsize=15)

plt.savefig(f'{pathOut}/Normalized_Difference_rainfall_dist_2003-2014_DEWETRAvsARCIS.png', bbox_inches='tight')






"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ISTOGRAMMA FREQUENZA RELATIVA CON BIN PIU LASCHI
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
thresh_1=[1.0,5.0,10.0,20.0,40.0,60.0,80.0,100.0,150.0]
thresh_2=[5.0,10.0,20.0,30.0,50.0,80.0,100.0]
thresh_3=[0.5,1.0,5.0,10.0]
thresh_4=[0.2,0.4,0.6,0.8,1.0,1.5,2.0]
thresh_avg=[1.0,5.0,10.0,20.0,40.0,60.0,100.0]


thresh_intervals_avg = ["<1","1-5","5-10","10-20","20-40","40-60","60-100",">100"]

thresh_intervals_11 = ["<1","1-5","5-10","10-20","20-40","40-60","60-80","80-100","100-150",">150"]
thresh_intervals_12 = ["40-60","60-80","80-100","100-150",">150"]

thresh_intervals_21 = ["<5","(5-10]","(10-20]","(20-30]","(30-50]","(50-80]","(80-100]",">100"]
thresh_intervals_22 = ["20-30","30-50","50-80","80-100","100-200",">200"]

thresh_intervals_31 = ["<0.5","0.5-1","1-5","5-10",">10"]

thresh_intervals_41 = ["<=0.2","0.2-0.4","0.4-0.6","0.6-0.8","0.8-1.0","1.0-1.5", "1.5-2.0", ">2.0"]


#CHOOSE Thresholds and thresholds intervals
thresh = thresh_avg

funct2003_06_arcis = funct_distr(df_sphera_sc_2003_2006_arcis, df_era5_sc_2003_2006_arcis,thresh)
funct2007_10_arcis = funct_distr(df_sphera_sc_2007_2010_arcis, df_era5_sc_2007_2010_arcis,thresh)
funct2011_14_arcis = funct_distr(df_sphera_sc_2011_2014_arcis, df_era5_sc_2011_2014_arcis,thresh)

funct2003_06_dew = funct_distr(df_sphera_sc_2003_2006_dew, df_era5_sc_2003_2006_dew,thresh)
funct2007_10_dew = funct_distr(df_sphera_sc_2007_2010_dew, df_era5_sc_2007_2010_dew,thresh)
funct2011_14_dew = funct_distr(df_sphera_sc_2011_2014_dew, df_era5_sc_2011_2014_dew,thresh)
funct2015_17_dew = funct_distr(df_sphera_sc_2015_2017_dew, df_era5_sc_2015_2017_dew,thresh)



count_obs_era5_2003_2006_arcis = funct2003_06_arcis[0]
count_obs_sphera_2003_2006_arcis = funct2003_06_arcis[1]
count_prev_era5_2003_2006_arcis = funct2003_06_arcis[2]
count_prev_sphera_2003_2006_arcis = funct2003_06_arcis[3]

count_obs_era5_2007_2010_arcis = funct2007_10_arcis[0]
count_obs_sphera_2007_2010_arcis = funct2007_10_arcis[1]
count_prev_era5_2007_2010_arcis = funct2007_10_arcis[2]
count_prev_sphera_2007_2010_arcis = funct2007_10_arcis[3]

count_obs_era5_2011_2014_arcis = funct2011_14_arcis[0]
count_obs_sphera_2011_2014_arcis = funct2011_14_arcis[1]
count_prev_era5_2011_2014_arcis = funct2011_14_arcis[2]
count_prev_sphera_2011_2014_arcis = funct2011_14_arcis[3]


count_obs_era5_2003_2006_dew = funct2003_06_dew[0]
count_obs_sphera_2003_2006_dew = funct2003_06_dew[1]
count_prev_era5_2003_2006_dew = funct2003_06_dew[2]
count_prev_sphera_2003_2006_dew = funct2003_06_dew[3]

count_obs_era5_2007_2010_dew = funct2007_10_dew[0]
count_obs_sphera_2007_2010_dew = funct2007_10_dew[1]
count_prev_era5_2007_2010_dew = funct2007_10_dew[2]
count_prev_sphera_2007_2010_dew = funct2007_10_dew[3]

count_obs_era5_2011_2014_dew = funct2011_14_dew[0]
count_obs_sphera_2011_2014_dew = funct2011_14_dew[1]
count_prev_era5_2011_2014_dew = funct2011_14_dew[2]
count_prev_sphera_2011_2014_dew = funct2011_14_dew[3]

count_obs_era5_2015_2017_dew = funct2015_17_dew[0]
count_obs_sphera_2015_2017_dew = funct2015_17_dew[1]
count_prev_era5_2015_2017_dew = funct2015_17_dew[2]
count_prev_sphera_2015_2017_dew = funct2015_17_dew[3]


TOT_count_obs_era5_arcis = count_obs_era5_2003_2006_arcis + count_obs_era5_2007_2010_arcis + count_obs_era5_2011_2014_arcis# + count_obs_era5_2015_2017
TOT_count_obs_sphera_arcis = count_obs_sphera_2003_2006_arcis + count_obs_sphera_2007_2010_arcis + count_obs_sphera_2011_2014_arcis# + count_obs_sphera_2015_2017
TOT_count_prev_era5_arcis = count_prev_era5_2003_2006_arcis + count_prev_era5_2007_2010_arcis + count_prev_era5_2011_2014_arcis# + count_prev_era5_2015_2017
TOT_count_prev_sphera_arcis = count_prev_sphera_2003_2006_arcis + count_prev_sphera_2007_2010_arcis + count_prev_sphera_2011_2014_arcis# + count_prev_sphera_2015_2017

TOT_count_obs_era5_dew = count_obs_era5_2003_2006_dew + count_obs_era5_2007_2010_dew + count_obs_era5_2011_2014_dew + count_obs_era5_2015_2017_dew
TOT_count_obs_sphera_dew = count_obs_sphera_2003_2006_dew + count_obs_sphera_2007_2010_dew + count_obs_sphera_2011_2014_dew + count_obs_sphera_2015_2017_dew
TOT_count_prev_era5_dew = count_prev_era5_2003_2006_dew + count_prev_era5_2007_2010_dew + count_prev_era5_2011_2014_dew + count_prev_era5_2015_2017_dew
TOT_count_prev_sphera_dew = count_prev_sphera_2003_2006_dew + count_prev_sphera_2007_2010_dew + count_prev_sphera_2011_2014_dew + count_prev_sphera_2015_2017_dew




#normalize the count arrays with the total count of each array to find the normalized frequency:
norm_TOT_count_obs_era5_arcis = TOT_count_obs_era5_arcis/sum(TOT_count_obs_era5_arcis)
norm_TOT_count_obs_sphera_arcis = TOT_count_obs_sphera_arcis/sum(TOT_count_obs_sphera_arcis)
norm_TOT_count_prev_era5_arcis = TOT_count_prev_era5_arcis/sum(TOT_count_prev_era5_arcis)
norm_TOT_count_prev_sphera_arcis = TOT_count_prev_sphera_arcis/sum(TOT_count_prev_sphera_arcis)

norm_TOT_count_obs_era5_dew = TOT_count_obs_era5_dew/sum(TOT_count_obs_era5_dew)
norm_TOT_count_obs_sphera_dew = TOT_count_obs_sphera_dew/sum(TOT_count_obs_sphera_dew)
norm_TOT_count_prev_era5_dew = TOT_count_prev_era5_dew/sum(TOT_count_prev_era5_dew)
norm_TOT_count_prev_sphera_dew = TOT_count_prev_sphera_dew/sum(TOT_count_prev_sphera_dew)


#dataframe con obs, sphera ed era5 ai vari livelli di thresholds
df_arcis_11 = pd.DataFrame(index=range(len(thresh_intervals_11)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_11['Obs'] = norm_TOT_count_obs_sphera_arcis
df_arcis_11['Sphera'] = norm_TOT_count_prev_sphera_arcis
df_arcis_11['Era5'] = norm_TOT_count_prev_era5_arcis
df_arcis_11['thresh_int'] = thresh_intervals_11
melt_df_arcis_11 = pd.melt(df_arcis_11, id_vars=['thresh_int'])

df_arcis_12 = pd.DataFrame(index=range(len(thresh_intervals_12)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_12['Obs'] = norm_TOT_count_obs_sphera_arcis[5:]
df_arcis_12['Sphera'] = norm_TOT_count_prev_sphera_arcis[5:]
df_arcis_12['Era5'] = norm_TOT_count_prev_era5_arcis[5:]
df_arcis_12['thresh_int'] = thresh_intervals_12
melt_df_arcis_12 = pd.melt(df_arcis_12, id_vars=['thresh_int'])

df_arcis_21 = pd.DataFrame(index=range(len(thresh_intervals_21)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_21['Obs'] = norm_TOT_count_obs_sphera_arcis
df_arcis_21['Sphera'] = norm_TOT_count_prev_sphera_arcis
df_arcis_21['Era5'] = norm_TOT_count_prev_era5_arcis
df_arcis_21['thresh_int'] = thresh_intervals_21
melt_df_arcis_21 = pd.melt(df_arcis_21, id_vars=['thresh_int'])

df_arcis_22 = pd.DataFrame(index=range(len(thresh_intervals_22)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_22['Obs'] = norm_TOT_count_obs_sphera_arcis[3:]
df_arcis_22['Sphera'] = norm_TOT_count_prev_sphera_arcis[3:]
df_arcis_22['Era5'] = norm_TOT_count_prev_era5_arcis[3:]
df_arcis_22['thresh_int'] = thresh_intervals_22
melt_df_arcis_22 = pd.melt(df_arcis_22, id_vars=['thresh_int'])

df_arcis_31 = pd.DataFrame(index=range(len(thresh_intervals_31)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_31['Obs'] = norm_TOT_count_obs_sphera_arcis
df_arcis_31['Sphera'] = norm_TOT_count_prev_sphera_arcis
df_arcis_31['Era5'] = norm_TOT_count_prev_era5_arcis
df_arcis_31['thresh_int'] = thresh_intervals_31
melt_df_arcis_31 = pd.melt(df_arcis_31, id_vars=['thresh_int'])

df_arcis_41 = pd.DataFrame(index=range(len(thresh_intervals_41)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_41['Obs'] = norm_TOT_count_obs_sphera_arcis
df_arcis_41['Sphera'] = norm_TOT_count_prev_sphera_arcis
df_arcis_41['Era5'] = norm_TOT_count_prev_era5_arcis
df_arcis_41['thresh_int'] = thresh_intervals_41
melt_df_arcis_41 = pd.melt(df_arcis_41, id_vars=['thresh_int'])

df_arcis_avg = pd.DataFrame(index=range(len(thresh_intervals_avg)), columns=['Obs','Sphera','Era5','thresh_int'])
df_arcis_avg['Obs'] = norm_TOT_count_obs_sphera_arcis
df_arcis_avg['Sphera'] = norm_TOT_count_prev_sphera_arcis
df_arcis_avg['Era5'] = norm_TOT_count_prev_era5_arcis
df_arcis_avg['thresh_int'] = thresh_intervals_avg
melt_df_arcis_avg = pd.melt(df_arcis_avg, id_vars=['thresh_int'])







df_dew_11 = pd.DataFrame(index=range(len(thresh_intervals_11)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_11['Obs'] = norm_TOT_count_obs_sphera_dew
df_dew_11['Sphera'] = norm_TOT_count_prev_sphera_dew
df_dew_11['Era5'] = norm_TOT_count_prev_era5_dew
df_dew_11['thresh_int'] = thresh_intervals_11
melt_df_dew_11 = pd.melt(df_dew_11, id_vars=['thresh_int'])

df_dew_12 = pd.DataFrame(index=range(len(thresh_intervals_12)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_12['Obs'] = norm_TOT_count_obs_sphera_dew[5:]
df_dew_12['Sphera'] = norm_TOT_count_prev_sphera_dew[5:]
df_dew_12['Era5'] = norm_TOT_count_prev_era5_dew[5:]
df_dew_12['thresh_int'] = thresh_intervals_12
melt_df_dew_12 = pd.melt(df_dew_12, id_vars=['thresh_int'])

df_dew_21 = pd.DataFrame(index=range(len(thresh_intervals_21)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_21['Obs'] = norm_TOT_count_obs_sphera_dew
df_dew_21['Sphera'] = norm_TOT_count_prev_sphera_dew
df_dew_21['Era5'] = norm_TOT_count_prev_era5_dew
df_dew_21['thresh_int'] = thresh_intervals_21
melt_df_dew_21 = pd.melt(df_dew_21, id_vars=['thresh_int'])

df_dew_22 = pd.DataFrame(index=range(len(thresh_intervals_22)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_22['Obs'] = norm_TOT_count_obs_sphera_dew[3:]
df_dew_22['Sphera'] = norm_TOT_count_prev_sphera_dew[3:]
df_dew_22['Era5'] = norm_TOT_count_prev_era5_dew[3:]
df_dew_22['thresh_int'] = thresh_intervals_22
melt_df_dew_22 = pd.melt(df_dew_22, id_vars=['thresh_int'])

df_dew_31 = pd.DataFrame(index=range(len(thresh_intervals_31)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_31['Obs'] = norm_TOT_count_obs_sphera_dew
df_dew_31['Sphera'] = norm_TOT_count_prev_sphera_dew
df_dew_31['Era5'] = norm_TOT_count_prev_era5_dew
df_dew_31['thresh_int'] = thresh_intervals_31
melt_df_dew_31 = pd.melt(df_dew_31, id_vars=['thresh_int'])

df_dew_41 = pd.DataFrame(index=range(len(thresh_intervals_41)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_41['Obs'] = norm_TOT_count_obs_sphera_dew
df_dew_41['Sphera'] = norm_TOT_count_prev_sphera_dew
df_dew_41['Era5'] = norm_TOT_count_prev_era5_dew
df_dew_41['thresh_int'] = thresh_intervals_41
melt_df_dew_41 = pd.melt(df_dew_41, id_vars=['thresh_int'])

df_dew_avg = pd.DataFrame(index=range(len(thresh_intervals_avg)), columns=['Obs','Sphera','Era5','thresh_int'])
df_dew_avg['Obs'] = norm_TOT_count_obs_sphera_dew
df_dew_avg['Sphera'] = norm_TOT_count_prev_sphera_dew
df_dew_avg['Era5'] = norm_TOT_count_prev_era5_dew
df_dew_avg['thresh_int'] = thresh_intervals_avg
melt_df_dew_avg = pd.melt(df_dew_avg, id_vars=['thresh_int'])




#SET THE DATASETS USED BASED ON THRESH:
melt_df_dew = melt_df_dew_avg
melt_df_arcis = melt_df_arcis_avg



#HISTOGRAMS PLOT FOR THE TWO OBSERVATIVE DATASETS
sns.set(style="ticks", palette="pastel")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9,4))  #, ax6
    
fig.subplots_adjust(hspace=0.0)
fig.suptitle(f'Daily rainfall frequency distributions', fontsize=20, y=0.92)


ax1 = plt.subplot2grid((2,1), (0,0), rowspan=1, colspan=1)
ax1.tick_params(axis='y', which='major', labelsize=15)
#ax1.set_title('ARCIS')

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_arcis, palette=["orange", "#87489D", "#32AAB5"])

ax1.legend(title='', fontsize=16)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('Normalized frequency', fontsize = 18)
#sns.despine(offset=10, trim=True)

handles, labels = plt.gca().get_legend_handles_labels()
labels = ['ARCIS', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend1 = ax1.legend(by_label.values(), by_label.keys(), title='2003-2014', fontsize=18)
#ax1.set_ylim([0.0,0.02])

plt.setp(legend1.get_title(),fontsize=18)

ax2 = plt.subplot2grid((2,1), (1,0), rowspan=1, colspan=1)
ax2.tick_params(axis='y', which='major', labelsize=15)
#ax2.set_title('DEWETRA')

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_dew, palette=["#023FA5", "#87489D", "#32AAB5"])

ax2.legend(title='', fontsize=16)                                                                   
ax2.grid(True, linestyle='--')
ax2.set_ylabel('Normalized frequency', fontsize = 18)
ax2.set_xlabel('Precipitation threshold [mm/day]', fontsize=18)
sns.despine(offset=10, trim=True)
ax2.tick_params(axis='x', which='major', labelsize=16)
#ax2.set_ylim([0.0,0.02])


handles, labels = plt.gca().get_legend_handles_labels()
labels = ['DEWETRA', 'SPHERA', 'ERA5']
by_label = dict(zip(labels, [handles[0],handles[1],handles[2]]))
legend2 = ax2.legend(by_label.values(), by_label.keys(), title='2003-2017', fontsize=18)

plt.setp(legend2.get_title(),fontsize=18)

plt.savefig(f'{pathOut}/rainfall_dist_2003-2014_DEW_v_ARC_{aggr}Box_4NEW.pdf', bbox_inches="tight", dpi=300)




#ZOOM PLOT ON HIGHER THRESHOLDS


df_dew_avg_ZOOM = df_dew_avg[5:]
df_arcis_avg_ZOOM = df_arcis_avg[5:]

melt_df_dew_avg_ZOOM = pd.melt(df_dew_avg_ZOOM, id_vars=['thresh_int'])
melt_df_arcis_avg_ZOOM = pd.melt(df_arcis_avg_ZOOM, id_vars=['thresh_int'])



sns.set(style="ticks", palette="pastel")

fig, ax1 = plt.subplots(1, 1, figsize=(5,3))  #, ax6
    
ax1.tick_params(axis='both', which='major', labelsize=15)

sns.barplot(x="thresh_int", y="value", hue="variable", data=melt_df_dew_avg_ZOOM, palette=["#023FA5", "#87489D", "#32AAB5"])

ax1.grid(True, linestyle='--')
ax1.set_ylabel('Normalized frequency', fontsize = 18)
#ax1.set_ylim([0.0,0.015])
sns.despine(offset=1, trim=True)

plt.savefig(f'{pathOut}/rainfall_dist_2003-2014_{aggr}Box_4NEW_Dew_ZOOM2.pdf', bbox_inches="tight", dpi=300)


















