import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.ticker
import itertools
from collections import defaultdict
import seaborn as sns

"""
Script for calculating starting from contingency tables data: 
- Hanssen-Kuiper skill score 
- log-Odds ratio score
- Heidke skill score
and plot them as function of precip. thresholds and aggregating by season
"""

"""
SINGLE SEASON
NESTING
"""

aggr = 'mean'
thresholds = [1,5,10,15,25,50,80]
seas = 'JJA2015'


#upload contingency tables and extract them for each threshold   
cont_sphera_s1 = pd.read_csv(f"/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/articoloInes/nesting/directNudg/TP_{aggr}/{seas}/cont_table_mod.dat",
                           skiprows=0, sep="\s+")

cont_sphera_s2 = pd.read_csv(f"/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/articoloInes/nesting/2NestNudg/TP_{aggr}/{seas}/cont_table_mod.dat",
                           skiprows=0, sep="\s+")

cont_era5 = pd.read_csv(f"/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/articoloInes/era5/{aggr}/{seas}/cont_table_mod.dat",
                           skiprows=0, sep="\s+")



#calc HKS (Hansen Kuiper), ODDS ratio and HSS (Heidke) scores for every season and reanalysis:
HKS_scores = {}
ODDS_scores = {}
logODDS_scores = {}
HSS_scores = {}

HKS_scores = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA_s1', 'SPHERA_s2','ERA5'])
HKS_scores['thresh'] = thresholds

ODDS_scores = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA_s1', 'SPHERA_s2','ERA5'])
ODDS_scores['thresh'] = thresholds

logODDS_scores = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA_s1', 'SPHERA_s2','ERA5'])
logODDS_scores['thresh'] = thresholds

HSS_scores = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA_s1', 'SPHERA_s2','ERA5'])
HSS_scores['thresh'] = thresholds

for rean in ['SPHERA_s1', 'SPHERA_s2', 'ERA5']:
                          
    if rean == 'SPHERA_s1':
        contTabs = cont_sphera_s1
    elif rean == 'SPHERA_s2':
        contTabs = cont_sphera_s2
    else:
        contTabs = cont_era5
        
    for thresh in np.arange(0,len(thresholds),1):
        
        if thresh == 0:
            ct = contTabs.loc[0:1].reset_index(drop=True)
        elif thresh == 1:
            ct = contTabs.loc[3:4].reset_index(drop=True)
        elif thresh == 2:
            ct = contTabs.loc[6:7].reset_index(drop=True)
        elif thresh == 3:
            ct = contTabs.loc[9:10].reset_index(drop=True)
        elif thresh == 4:
            ct = contTabs.loc[12:13].reset_index(drop=True)
        elif thresh == 5:
            ct = contTabs.loc[15:16].reset_index(drop=True)
        elif thresh == 6:
            ct = contTabs.loc[18:19].reset_index(drop=True)
        elif thresh == 7:
            ct = contTabs.loc[21:22].reset_index(drop=True)
    
        if ct.values.all() != None:    
            
            
            a = ct.loc[0][0]
            b = ct.loc[0][1]
            c = ct.loc[1][0]
            d = ct.loc[1][1]
            
            #calc Hanssen-Kuiper skill score: HKS = (ad - bc)/((a+c)*(b+d))
            HKS = (a*d - b*c)/((a+c)*(b+d))
            HKS_scores[rean].loc[thresh] = HKS    
            
            #ODDS = (a*d - b*c)/(a*d + b*c)
            ODDS = (a*d)/(b*c)
            ODDS_scores[rean].loc[thresh] = ODDS  
            
            logODDS = np.log(ODDS)
            logODDS_scores[rean].loc[thresh] = logODDS
            
            #Heidke skill score:
            HSS = 2*(a*d-b*c)/((a+c)*(c+d) + (a+b)*(b+d))
            HSS_scores[rean].loc[thresh] = HSS    



#HKS SCORE PLOT
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
ax.set_title(f'{seas} {aggr}', fontsize=19)  # using the {title_label} of the box', fontsize=17)
ax.set_ylim([-0.05,0.8])

ax.plot(HKS_scores['thresh'], HKS_scores['SPHERA_s1'], '-o',  markersize=10,  color='black', mfc='none', lw=2)
ax.plot(HKS_scores['thresh'], HKS_scores['SPHERA_s2'], '-o',  markersize=10, color='black', lw=2)
ax.plot(HKS_scores['thresh'], HKS_scores['ERA5'], '-o',  markersize=10, color='red', lw=2)

#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['SPHERA'], '-o',  markersize=10, color='#023FA5', label='DJF',lw=2)
#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['ERA5'], '--o',  markersize=10, mfc='none', color='#023FA5',lw=2)

ax.set_xticks(HKS_scores['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/day)', fontsize=19)
ax.set_ylabel('Hanssen-Kuiper skill score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none',  color='black',
                   label='SPHERA_s1',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                   label='SPHERA_s2',scaley=False)
l3, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='red', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2,l3], loc='best', fontsize=18)  
  
plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/Hanssen-Kuiper_score/HKS_nest_{seas}_2015_{aggr}.pdf', bbox_inches="tight")


#logODDS RATIO SCORE PLOT
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
ax.set_title(f'{seas} {aggr}', fontsize=19)  # using the {title_label} of the box', fontsize=17)
#ax.set_ylim([-0.05,0.8])

ax.plot(logODDS_scores['thresh'], logODDS_scores['SPHERA_s1'], '-o',  markersize=10,  color='black', mfc='none', lw=2)
ax.plot(logODDS_scores['thresh'], logODDS_scores['SPHERA_s2'], '-o',  markersize=10, color='black', lw=2)
ax.plot(logODDS_scores['thresh'], logODDS_scores['ERA5'], '-o',  markersize=10, color='red', lw=2)

#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['SPHERA'], '-o',  markersize=10, color='#023FA5', label='DJF',lw=2)
#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['ERA5'], '--o',  markersize=10, mfc='none', color='#023FA5',lw=2)

ax.set_xticks(logODDS_scores['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/day)', fontsize=19)
ax.set_ylabel('Log-Odds ratio', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none',  color='black',
                   label='SPHERA_s1',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                   label='SPHERA_s2',scaley=False)
l3, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='red', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2,l3], loc='upper left', fontsize=18)  

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/logOdds/logOdds_nest_{seas}_2015_{aggr}.pdf', bbox_inches="tight")


#HSS SCORE PLOT
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
ax.set_title(f'{seas} {aggr}', fontsize=19)  # using the {title_label} of the box', fontsize=17)
ax.set_ylim([-0.05,0.8])

ax.plot(HSS_scores['thresh'], HSS_scores['SPHERA_s1'], '-o',  markersize=10,  color='black', mfc='none', lw=2)
ax.plot(HSS_scores['thresh'], HSS_scores['SPHERA_s2'], '-o',  markersize=10, color='black', lw=2)
ax.plot(HSS_scores['thresh'], HSS_scores['ERA5'], '-o',  markersize=10, color='red', lw=2)

#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['SPHERA'], '-o',  markersize=10, color='#023FA5', label='DJF',lw=2)
#ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['ERA5'], '--o',  markersize=10, mfc='none', color='#023FA5',lw=2)

ax.set_xticks(HSS_scores['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/day)', fontsize=19)
ax.set_ylabel('Heidke skill score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none',  color='black',
                   label='SPHERA_s1',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                   label='SPHERA_s2',scaley=False)
l3, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='red', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2,l3], loc='best', fontsize=18)  

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/nesting/HeidkeScore/HSS_nest_{seas}_2015_{aggr}.pdf', bbox_inches="tight")



"""
AGGREGATING MANY SEASONS TOGETHER AND CALCULATE AVG SCORE
"""

#set aggregation: max o mean
aggr = 'mean'

#set temporal range: daily or hourly data
time_agg = 'daily'

if time_agg == 'daily':
    pathIn=f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/DEWETRA'
    thresholds = [1,5,10,15,25,50,80,150]
    xlab = 'day'
    
elif time_agg == 'hourly':
    pathIn=f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/ver_oraria'
    thresholds = [0.5,1,1.5,2,5,7.5,10,15,20]
    xlab = 'hour'
    
pathIn = f"/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/dati/articoloInes"
thresholds = [1,5,10,15,25,50,80]
xlab = 'day'
    
#springs = ['MAM03', 'MAM04', 'MAM05', 'MAM06', 'MAM07', 'MAM08', 'MAM09', 'MAM10', 'MAM11', 'MAM12', 'MAM13', 'MAM14', 'MAM15', 'MAM16', 'MAM17']
summers = ['JJA2015', 'JJA2016']#['JJA03', 'JJA04', 'JJA05', 'JJA06', 'JJA07', 'JJA08', 'JJA09', 'JJA10', 'JJA11', 'JJA12', 'JJA13', 'JJA14', 'JJA15', 'JJA16', 'JJA17']
#falls = ['SON03', 'SON04', 'SON05', 'SON06', 'SON07', 'SON08', 'SON09', 'SON10', 'SON11', 'SON12', 'SON13', 'SON14', 'SON15', 'SON16', 'SON17']
winters = ['DJF2015','DJF2016']#['DJF03', 'DJF04', 'DJF05', 'DJF07', 'DJF08', 'DJF09', 'DJF11', 'DJF12', 'DJF13', 'DJF15', 'DJF16']

cont_sphera = {}
cont_era5 = {}

#upload contingency tables and extract them for each threshold   
for season in  summers + winters:  #springs + falls

    cont_sphera[season] = pd.read_csv(f"{pathIn}/oper2015/{aggr}/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
                            #{pathIn}/SPHERA/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat
    cont_sphera[season].columns = ['1','0']
    cont_era5[season] = pd.read_csv(f"{pathIn}/era5/{aggr}/{season}/cont_table_mod.dat",skiprows=0, sep="\s+")
                            #f"{pathIn}/ERA5/box60_{aggr}/all_seasons_2003-2017/{season}/cont_table_mod.dat"
    cont_era5[season].columns = ['1','0']

#sum cont tables over all seasons:
cont_seas_sums_sphera = {}
cont_seas_sums_era5 = {}

all_seas = [summers,winters]  #springs,falls

#inizializzare i df vuoti
for season in ['JJA','DJF']:  #'MAM' , 'SON'
    cont_seas_sums_sphera[season] = pd.DataFrame(index=np.arange(0,23,1),columns=['1','0'])      
    cont_seas_sums_era5[season] = pd.DataFrame(index=np.arange(0,23,1),columns=['1','0'])

for seasons in [summers, winters]:  #springs, falls
    
    #if seasons == springs:
    #    ss = 'MAM'
    if seasons == summers:
        ss = 'JJA'
    #elif seasons == falls:
    #    ss = 'SON'
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

"""
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
"""    

#calc HKS score for every season and reanalysis:
HKS_scores = {}
HSS_scores = {}

for ss in ['JJA','DJF']:  #'MAM','SON'

    HKS_scores[ss] = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA','ERA5'])
    HKS_scores[ss]['thresh'] = thresholds
    
    HSS_scores[ss] = pd.DataFrame(index=np.arange(0,len(thresholds),1), columns=['thresh','SPHERA','ERA5'])
    HSS_scores[ss]['thresh'] = thresholds

    for rean in ['SPHERA', 'ERA5']:
        
        contTabs = cont_seas_sums[rean][ss]
        
        for thresh in np.arange(0,8,1):
            
            if thresh == 0:
                ct = contTabs.loc[0:1].reset_index(drop=True)
            elif thresh == 1:
                ct = contTabs.loc[3:4].reset_index(drop=True)
            elif thresh == 2:
                ct = contTabs.loc[6:7].reset_index(drop=True)
            elif thresh == 3:
                ct = contTabs.loc[9:10].reset_index(drop=True)
            elif thresh == 4:
                ct = contTabs.loc[12:13].reset_index(drop=True)
            elif thresh == 5:
                ct = contTabs.loc[15:16].reset_index(drop=True)
            elif thresh == 6:
                ct = contTabs.loc[18:19].reset_index(drop=True)
            elif thresh == 7:
                ct = contTabs.loc[21:22].reset_index(drop=True)
        
            if ct.values.all() != None:    
                
                #calc Hanssen-Kuiper skill score: HKS = (ad - bc)/((a+c)*(b+d))
                a = ct.loc[0][0]
                b = ct.loc[0][1]
                c = ct.loc[1][0]
                d = ct.loc[1][1]
                
                #Hanssen-Kuiper score
                HKS = (a*d - b*c)/((a+c)*(b+d))
                HKS_scores[ss][rean].loc[thresh] = HKS    
                
                #Heidke skill score:
                HSS = 2*(a*d-b*c)/((a+c)*(c+d) + (a+b)*(b+d))
                HSS_scores[ss][rean].loc[thresh] = HSS    
            
#Plot scores per threshold:

#JJA and DJF
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
ax.set_title(f'{aggr} 2015-2016', fontsize=19)  # using the {title_label} of the box', fontsize=17)
ax.set_ylim([-0.05,0.8])

ax.plot(HKS_scores['JJA']['thresh'], HKS_scores['JJA']['SPHERA'], '--o',  markersize=10, mfc='none', color='#7F000D', lw=2)
ax.plot(HKS_scores['JJA']['thresh'], HKS_scores['JJA']['ERA5'], '-o',  markersize=10, color='#7F000D',lw=2, label='JJA')

ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['SPHERA'], '--o',  markersize=10, mfc='none', color='#023FA5', lw=2)
ax.plot(HKS_scores['DJF']['thresh'], HKS_scores['DJF']['ERA5'], '-o',  markersize=10, color='#023FA5',lw=2, label='DJF')

ax.set_xticks(HKS_scores['JJA']['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/{xlab})', fontsize=19)
ax.set_ylabel('Hanssen-Kuiper skill score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none',  color='black', 
                   label='SPHERA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10,color='black', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2], loc='best', fontsize=18)                

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/2015-2016_spheraVera5/Hanssen-Kuiper_score/HKS_JJA-DJF_2015-2016_{aggr}.pdf', bbox_inches="tight")

#f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/Hanssen-Kuiper_score/HKS_{time_agg}_JJA-DJF_2003-2017_{aggr}60.pdf'

#SON and MAM plot

fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
#ax.set_title(r'$\bf{' + 'DEWETRA' + '}$ (2003-2017)', fontsize=19)  # using the {title_label} of the box', fontsize=17)
ax.set_ylim([-0.05,0.8])

ax.plot(HKS_scores['MAM']['thresh'], HKS_scores['MAM']['SPHERA'], '-o',  markersize=10, color='#027C1E', label='MAM',lw=2)
ax.plot(HKS_scores['MAM']['thresh'], HKS_scores['MAM']['ERA5'], '--o',  markersize=10, mfc='none', color='#027C1E',lw=2)

ax.plot(HKS_scores['SON']['thresh'], HKS_scores['SON']['SPHERA'], '-o',  markersize=10, color='#E8853A', label='SON',lw=2)
ax.plot(HKS_scores['SON']['thresh'], HKS_scores['SON']['ERA5'], '--o',  markersize=10, mfc='none', color='#E8853A',lw=2)

ax.set_xticks(HKS_scores['JJA']['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/{xlab})', fontsize=19)
ax.set_ylabel('Hanssen-Kuiper skill score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, color='black', 
                   label='SPHERA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none', color='black', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2], loc='best', fontsize=18) 

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/Hanssen-Kuiper_score/HKS_{time_agg}_MAM-SON_2003-2017_{aggr}60.pdf', bbox_inches="tight")


#HSS score plot:

#JJA and DJF
fig, ax = plt.subplots(figsize=(10,5))
ax.set_xscale('log')
ax.set_title(f'{aggr} 2015-2016', fontsize=19)  # using the {title_label} of the box', fontsize=17)
ax.set_ylim([-0.05,0.8])

ax.plot(HSS_scores['JJA']['thresh'], HSS_scores['JJA']['SPHERA'], '--o',  markersize=10, mfc='none', color='#7F000D', lw=2)
ax.plot(HSS_scores['JJA']['thresh'], HSS_scores['JJA']['ERA5'], '-o',  markersize=10, color='#7F000D',lw=2, label='JJA')

ax.plot(HSS_scores['DJF']['thresh'], HSS_scores['DJF']['SPHERA'], '--o',  markersize=10, mfc='none', color='#023FA5', lw=2)
ax.plot(HSS_scores['DJF']['thresh'], HSS_scores['DJF']['ERA5'], '-o',  markersize=10, color='#023FA5',lw=2, label='DJF')

ax.set_xticks(HSS_scores['JJA']['thresh'])

ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.tick_params(axis='both', which='major', labelsize=15)

ax.set_xlabel(f'Precipitation threshold (mm/{xlab})', fontsize=19)
ax.set_ylabel('Heidke skill score', fontsize=19)
legend = plt.legend(fontsize=18, loc='lower left')
ax.grid(lw=0.5, linestyle='--')

ax1 = ax.twinx()
ax1.set_yticks([])
    
l1, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10, mfc='none',  color='black', 
                   label='SPHERA',scaley=False)
l2, = ax1.plot(1, 1.5, linestyle='', marker='o', markersize=10,color='black', 
                   label='ERA5', scaley=False)
ax1.legend(handles=[l1,l2], loc='best', fontsize=18)                

plt.savefig(f'/home/ciccuz/phd/ARPAE/analisi/verifica_precipitazioni/articoloInes/2015-2016_spheraVera5/HeidkeScore/HSS_JJA-DJF_2015-2016_{aggr}.pdf', bbox_inches="tight")











