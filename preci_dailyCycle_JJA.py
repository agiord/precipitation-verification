import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns
import matplotlib.ticker as ticker

"""
Script per plottare il ciclo giornaliero medio della preci estiva 
"""


pathIn=f'/media/ciccuz/601f31d5-0360-49cb-a57b-e8c29b56843d/phd/ARPAE/SPHERA/analisi/verifica_precipitazioni/timing_preci_hourly_JJA/dati_unboxed_landfilt_pp01'

#sphera_data = pd.read_csv(f"{pathIn}/dhourmean_NEWfilt01_sphera_hourly_JJA15_decumul.csv",sep="\s+")
#era5_data = pd.read_csv(f"{pathIn}/dhourmean_filt01mm_convmm_era5_tpH_JJA_2003-2017_box60_max.csv",sep="\s+")
#dew_data = pd.read_csv(f"{pathIn}/dhourmean_filt01mm_dew_2003-2017_NO-2004-2010-2011-2012.csv",sep="\s+")

hours = [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300]

#stepRanges = [2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199,2200,2201,2202,2203,2204,2205,2206]
#dividere dataframe in diversi df relativi a ore singole:

rean_data_sp = pd.read_csv(f"{pathIn}/spatAvg_dhourmean_cat_sphera_hourly_JJA2003_2017_decumul_filt01_LAND.csv",
                           names=['sphera','hour'],sep=" ")
rean_data_era5 = pd.read_csv(f"{pathIn}/spatAvg_dhourmean_mult1000_era5_hourly_JJA2003-2017_fixed_filt01_LAND.csv",
                             sep=",", skiprows=1, names=['era5'])

rean_data_era5 = rean_data_era5[1:25].reset_index(drop=True)

rean_data = pd.concat([rean_data_sp,rean_data_era5],axis=1)
rean_data['era5'] = pd.to_numeric(rean_data['era5'])

"""
sphera = {}
era5 = {}
dew = {}
    
for hour in [0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300]:
    
    sphera[hour] = pd.DataFrame(columns=['Latitude','Longitude','Value,','dataTime'])
    era5[hour] = pd.DataFrame(columns=['Latitude','Longitude','Value,','dataTime'])
    dew[hour] = pd.DataFrame(columns=['Latitude','Longitude','Value,','dataTime'])

    sphera[hour] = sphera_data.loc[sphera_data['dataTime'] == f'{hour}']
    era5[hour] = era5_data.loc[era5_data['dataTime'] == f'{hour}']
    dew[hour] = dew_data.loc[dew_data['dataTime'] == f'{hour}']
    


pd.set_option('display.float_format', lambda x: '%.6f' % x)

sphera_spat_avg = pd.DataFrame(index=hours, columns=['pp'])
era5_spat_avg = pd.DataFrame(index=hours, columns=['pp'])
dew_spat_avg = pd.DataFrame(index=hours, columns=['pp'])


for hour in hours: 
    
    sphera_spat_avg.loc[sphera_spat_avg.index == hour] = pd.to_numeric(sphera[hour]['Value,']).mean()
    era5_spat_avg.loc[era5_spat_avg.index == hour] = pd.to_numeric(era5[hour]['Value,']).mean()
    dew_spat_avg.loc[dew_spat_avg.index == hour] = pd.to_numeric(dew[hour]['Value,']).mean()
    
"""



#ax1.set_xticks(rean_data['sphera'].index)
#ax1.set_xlim(0,24)
fig, ax1 = plt.subplots(figsize=(7,5))

ax1.set_title(f'', fontsize=15)
ax1.tick_params(axis='both', which='major', labelsize=10)

#ax1.plot(dew_spat_avg.index, dew_spat_avg['pp'], '-',  lw=2, color='black', label='OBS')
ax1.plot(dew_avg_hours['avg'].index, dew_avg_hours['avg'], '-', marker='o',  lw=2, color='#023FA5', label='DEWETRA')
ax1.plot(rean_data['sphera'].index, rean_data['sphera'], '-', marker='o',  lw=2, color='#87489D', label='SPHERA')
ax1.plot(rean_data['sphera'].index, rean_data['era5'], '-', marker='o',  lw=2, color='#32AAB5', label='ERA5')

ax1.set_xlim([-0.5,24])
ax1.xaxis.set_major_locator(ticker.MultipleLocator(6))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax1.set_xticklabels(['','00:00','06:00','12:00','18:00','24:00'])

ax1.legend(title='', fontsize=15)                                                                   
ax1.grid(True, linestyle='--')
ax1.set_ylabel('', fontsize = 15)
ax1.set_xlabel('Hour of the day (UTC)', fontsize=17)

plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylabel('Mean precipitation intensity [mm/h]')
#plt.title('Average JJA daily precipitation, 2003-2017 \n (pp>0.1mm/h, Land grid points only)', fontsize=15)

plt.savefig(f'{pathIn}/diurnalCycle_JJAday_filtered01_nonBoxed_LAND_noTit.png', bbox_inches='tight')
    
    