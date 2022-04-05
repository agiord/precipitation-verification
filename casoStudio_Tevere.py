import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
import datetime
import random
import dateutil.parser

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/casiStudio/Tevere20Octo2011/dati_preci'
pathOut='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/casiStudio/Tevere20Octo2011/plot_cumulata'


df_obs_Bac = pd.read_csv(f"{pathIn}/Baccano/Baccano_201110190100_201110200000_hourly_puliti.csv", skiprows=0, sep=",")
df_sphera_Bac = pd.read_csv(f"{pathIn}/Baccano/SPHERA_hourly_Tevere_19-21Ott2011_BACCANO.csv", skiprows=1, sep=",")
df_era5_Bac = pd.read_csv(f"{pathIn}/Baccano/ERA5_hourly_Tevere_19-21Oct2011_BACCANO.csv", skiprows=1, sep=",")
df_merida_Bac = pd.read_csv(f"{pathIn}/MERIDA/MERIDA_PREC_20111020_tab2vers2_indPar61_Baccano.csv", skiprows=1, sep=",")
df_meridaOI_Bac = pd.read_csv(f"{pathIn}/MERIDA/MERIDA_PREC_OI_20111019-20_tab2vers2_Baccano.csv", skiprows=1, sep=",")

df_obs_Bac = df_obs_Bac[24:].reset_index()
df_sphera_Bac = df_sphera_Bac[23:47].reset_index()
df_era5_Bac = df_era5_Bac[23:47].reset_index()
df_meridaOI_Bac = df_meridaOI_Bac[23:47].reset_index()


df_obs_Rom = pd.read_csv(f"{pathIn}/RomaEUR/Roma_EUR_201110190100_201110200000_hourly_puliti.csv", skiprows=0, sep=",")
df_sphera_Rom = pd.read_csv(f"{pathIn}/RomaEUR/SPHERA_hourly_Tevere_19-21Ott2011_ROMA_EUR.csv", skiprows=1, sep=",")
df_era5_Rom = pd.read_csv(f"{pathIn}/RomaEUR/ERA5_hourly_Tevere_19-21Ott2011_ROMA_EUR.csv", skiprows=1, sep=",")
df_merida_Rom = pd.read_csv(f"{pathIn}/MERIDA/MERIDA_PREC_20111020_tab2vers2_indPar61_Roma_EUR.csv", skiprows=1, sep=",")
df_meridaOI_Rom = pd.read_csv(f"{pathIn}/MERIDA/MERIDA_PREC_OI_20111019-20_tab2vers2_Roma_EUR.csv", skiprows=1, sep=",")

df_obs_Rom = df_obs_Rom[24:].reset_index()
df_sphera_Rom = df_sphera_Rom[23:47].reset_index()
df_era5_Rom = df_era5_Rom[23:47].reset_index()
df_meridaOI_Rom = df_meridaOI_Rom[23:47].reset_index()

df_merida_Rom_NEW = pd.concat([df_meridaOI_Rom[0:3], df_merida_Rom], ignore_index=True)


accum_df_Bac = pd.DataFrame(columns=['date','obs','sphera','era5','merida','merida_OI'])

accum_df_Bac['date'] = pd.to_datetime(df_obs_Bac['Date'])
accum_df_Bac['obs'][0] = df_obs_Bac['Value'][0]
accum_df_Bac['sphera'][0] = df_sphera_Bac['B13011'][0]
accum_df_Bac['era5'][0] = df_era5_Bac['B13011'][0]
accum_df_Bac['merida'][0] = df_merida_Bac['B13011'][0]
accum_df_Bac['merida_OI'][0] = df_meridaOI_Bac['B13011'][0]


for i in np.arange(1,len(accum_df_Bac),1):
    accum_df_Bac['obs'][i] = accum_df_Bac['obs'][i-1] + df_obs_Bac['Value'][i]
    accum_df_Bac['sphera'][i] = accum_df_Bac['sphera'][i-1] + df_sphera_Bac['B13011'][i]
    accum_df_Bac['era5'][i] = accum_df_Bac['era5'][i-1] + df_era5_Bac['B13011'][i]
    accum_df_Bac['merida_OI'][i] = accum_df_Bac['merida_OI'][i-1] + df_meridaOI_Bac['B13011'][i]
    if i< 16:
        accum_df_Bac['merida'][i] = accum_df_Bac['merida'][i-1] + df_merida_Bac['B13011'][i]
    elif i>= 16:
        accum_df_Bac['merida'][i] = accum_df_Bac['merida'][15]
        
accum_df_Rom = pd.DataFrame(columns=['date','obs','sphera','era5','merida','merida_OI'])

accum_df_Rom['date'] = pd.to_datetime(df_obs_Rom['Date'])
accum_df_Rom['obs'][0] = df_obs_Rom['Value'][0]
accum_df_Rom['sphera'][0] = df_sphera_Rom['B13011'][0]
accum_df_Rom['era5'][0] = df_era5_Rom['B13011'][0]
accum_df_Rom['merida'][0] = df_merida_Rom_NEW['B13011'][0]
accum_df_Rom['merida_OI'][0] = df_meridaOI_Rom['B13011'][0]

for i in np.arange(1,len(accum_df_Rom),1):
    accum_df_Rom['obs'][i] = accum_df_Rom['obs'][i-1] + df_obs_Rom['Value'][i]
    accum_df_Rom['sphera'][i] = accum_df_Rom['sphera'][i-1] + df_sphera_Rom['B13011'][i]
    accum_df_Rom['era5'][i] = accum_df_Rom['era5'][i-1] + df_era5_Rom['B13011'][i]
    accum_df_Rom['merida_OI'][i] = accum_df_Rom['merida_OI'][i-1] + df_meridaOI_Rom['B13011'][i]
    
    if i<= 16:
        accum_df_Rom['merida'][i] = accum_df_Rom['merida'][i-1] + df_merida_Rom_NEW['B13011'][i]
    elif i>= 16:
        accum_df_Rom['merida'][i] = accum_df_Rom['merida'][15]
        



fig, ax1 = plt.subplots(figsize=(7,7))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
ax1.plot(accum_df_Bac['date'], accum_df_Bac['obs'], '-',  lw=2, color='black', label='OBS')
ax1.plot(accum_df_Bac['date'], accum_df_Bac['sphera'], '-',  lw=2, color='orange', label='SPHERA')
ax1.plot(accum_df_Bac['date'], accum_df_Bac['era5'], '-',  lw=2, color='#87489D', label='ERA5')
ax1.plot(accum_df_Bac['date'], accum_df_Bac['merida'], '--',  lw=2, color='red', label='MERIDA')
ax1.plot(accum_df_Bac['date'], accum_df_Bac['merida_OI'], ':',  lw=2, color='blue', label='MERIDA OI')

ax1.set_yticks([0,50,100,150,200,250])
datemin = datetime.datetime(2011, 10, 20, 0)  
datemax = accum_df_Bac['date'][23] 
ax1.set_xlim(datemin, datemax)

start = dateutil.parser.parse("20 October 2011")
end = dateutil.parser.parse("20 October 2011")

data = [start + (end - start) * random.random() for _ in range(1000)]

ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax1.xaxis.set_minor_locator(mdates.HourLocator((3,6,9,12,15,18,21,)))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))

ax1.tick_params(axis="x", which="major", pad=12)

plt.setp(ax1.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")

ax1.legend(title='', fontsize=14, ncol=2)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 15)
ax1.set_xlabel('Date', fontsize=17)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Accumulated precipitation [mm]')
plt.title('Accumulated precipitation in Baccano, 20 Oct 2011', fontsize=15)

plt.savefig(f'{pathOut}/cumul_preci_Tevere_BACCANO_vs_MERIDA.png', bbox_inches='tight')




fig, ax1 = plt.subplots(figsize=(7,7))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
ax1.plot(accum_df_Rom['date'], accum_df_Rom['obs'], '-',  lw=2, color='black', label='OBS')
ax1.plot(accum_df_Rom['date'], accum_df_Rom['sphera'], '-',  lw=2, color='orange', label='SPHERA')
ax1.plot(accum_df_Rom['date'], accum_df_Rom['era5'], '-',  lw=2, color='#87489D', label='ERA5')
ax1.plot(accum_df_Rom['date'], accum_df_Rom['merida'], '--',  lw=2, color='red', label='MERIDA')
ax1.plot(accum_df_Rom['date'], accum_df_Rom['merida_OI'], ':',  lw=2, color='blue', label='MERIDA OI')


ax1.set_yticks([0,50,100,150,200,250])
datemin = datetime.datetime(2011, 10, 20, 0)  
datemax = accum_df_Bac['date'][23] 
ax1.set_xlim(datemin, datemax)

start = dateutil.parser.parse("20 October 2011")
end = dateutil.parser.parse("20 October 2011")

data = [start + (end - start) * random.random() for _ in range(1000)]

ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax1.xaxis.set_minor_locator(mdates.HourLocator((3,6,9,12,15,18,21,)))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))

ax1.tick_params(axis="x", which="major", pad=12)

plt.setp(ax1.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")

ax1.legend(title='', fontsize=14, ncol=2)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 15)
ax1.set_xlabel('Date', fontsize=17)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Accumulated precipitation [mm]')
plt.title('Accumulated precipitation in Roma EUR, 20 Oct 2011', fontsize=15)

plt.savefig(f'{pathOut}/cumul_preci_Tevere_ROMAEUR_vs_MERIDA.png', bbox_inches='tight')


