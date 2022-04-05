import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import itertools
import datetime
import random
import dateutil.parser

pathIn='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/casiStudio/SecchiaPanaro2014/dati_preci_hourly_CIVAGO'
pathOut='/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/casiStudio/SecchiaPanaro2014/plot_cumulata'


df_obs = pd.read_csv(f"{pathIn}/Civago_20140116_20140120_hourly_puliti_NEW.csv", skiprows=1, sep=",")

df_sphera = pd.read_csv(f"{pathIn}/SPHERA_hourly_CIVAGO_16-20Jan2014_NEW.csv", skiprows=1, sep=",")

df_era5 = pd.read_csv(f"{pathIn}/ERA5_hourly_CIVAGO_16-20Jan2014_NEW.csv", skiprows=1, sep=",")


accum_df = pd.DataFrame(columns=['date','obs','sphera','era5'])

accum_df['date'] = pd.to_datetime(df_obs['Date'])
accum_df['obs'][0] = df_obs['B13011'][0]
accum_df['sphera'][0] = df_sphera['B13011'][0]
accum_df['era5'][0] = df_era5['B13011'][0]


for i in np.arange(1,len(accum_df),1):
    accum_df['obs'][i] = accum_df['obs'][i-1] + df_obs['B13011'][i]
    accum_df['sphera'][i] = accum_df['sphera'][i-1] + df_sphera['B13011'][i]
    accum_df['era5'][i] = accum_df['era5'][i-1] + df_era5['B13011'][i]


fig, ax1 = plt.subplots(figsize=(7,7))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)
ax1.plot(accum_df['date'], accum_df['obs'], '-',  lw=2, color='black', label='OBS')
ax1.plot(accum_df['date'], accum_df['sphera'], '-',  lw=2, color='#87489D', label='SPHERA')
ax1.plot(accum_df['date'], accum_df['era5'], '-',  lw=2, color='#32AAB5', label='ERA5')

ax1.set_yticks([0,50,100,150,200,250,300,350,400])
datemin = datetime.datetime(2014, 1, 16, 0)  
datemax = accum_df['date'][113] 
ax1.set_xlim(datemin, datemax)

start = dateutil.parser.parse("16 January 2014")
end = dateutil.parser.parse("20 January 2014")

data = [start + (end - start) * random.random() for _ in range(1000)]

ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax1.xaxis.set_minor_locator(mdates.HourLocator((6,18,)))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))

ax1.tick_params(axis="x", which="major", pad=12)

plt.setp(ax1.get_xticklabels(), rotation=30, ha="right", rotation_mode="anchor")

ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 15)
ax1.set_xlabel('Date [day - hour]', fontsize=17)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Accumulated precipitation [mm]')
plt.title('Accumulated precipitation in Civago, 16-20 Jan 2014', fontsize=15)

plt.axvline(x=pd.to_datetime('2014-01-17 11:00:00'), lw=0.75, linestyle='--', color='blue')
plt.axvline(x=pd.to_datetime('2014-01-19 06:00:00'), lw=0.75, linestyle='--', color='red')

plt.text(pd.to_datetime('2014-01-17 11:00:00'), 280, "Max hourly cumulation: 14.2 mm/h" % i, rotation=90, verticalalignment='center', 
         color='blue', fontsize=11)
plt.text(pd.to_datetime('2014-01-19 06:00:00'), 200, "Secchia embankment failure" % i, rotation=90, verticalalignment='center', 
         color='red', fontsize=11)


plt.savefig(f'{pathOut}/cumul_preci_Secchia_16-20Jan2014.png', bbox_inches='tight')






