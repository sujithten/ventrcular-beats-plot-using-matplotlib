# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 15:50:02 2019

@author: Sujith Tenali
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:30:58 2019

@author: Sujith Tenali
"""

import pandas as pd
import random

data = pd.read_csv('df_rhythmInfo_42346_1562149974649155.csv') 



data['epochTime'] = data['epochTime']/1000
data['time2'] = pd.to_datetime(data['epochTime'],unit='ms',utc=None, box=True, format=None)
data['time3']=data['time2'].dt.tz_localize('UTC').dt.tz_convert('Asia/Calcutta')
data['start_date_time'] = data['time3'].apply(lambda t: t.strftime('%Y-%m-%d %H:%M'))

times=[]
times = data['start_date_time'].unique()


table2 = pd.pivot_table(data, values='time2', index=['start_date_time'],
                    columns=['HRRhythm'], aggfunc='count', fill_value=0)



table2['real_time'] = data['start_date_time'].unique()

table2['normal_time'] = pd.to_datetime(table2['real_time'])


table2['percent'] = (table2['Ventricular Rhythm']/(table2['Sinus Rhythm']+table2['Ventricular Rhythm']))*100    
    

tickspos =[]
ticklabels= []

i=0
t= 12*60

while (i<len(table2['normal_time'])):
    tickspos.append(table2['normal_time'][i].replace(minute=0))
    i=i+(12*60)
    
    
    
    
tickspos.append(table2['normal_time'][-1])


for tickpo in tickspos:
    ticklabels.append(tickpo.strftime('%b %d,%Y %I:%M %p'))


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

prop = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Bold.ttf')
prop2 = fm.FontProperties(fname='C:/Users/Sujith Tenali/Desktop/Intern/DayWise/Montserrat-Medium.ttf')


fig= plt.figure(figsize=(10,5))



plt.grid(b=None, which='major', axis='both',linewidth=0.2)
plt.xlim(table2['normal_time'][0],table2['normal_time'][-1])

if((table2['Ventricular Rhythm'].max())%2==0):
    plt.ylim(0,int(table2['Ventricular Rhythm'].max()+2))
else:
    plt.ylim(0,int(table2['Ventricular Rhythm'].max()+3))

    




plt.xticks(tickspos,ticklabels,rotation=35,fontproperties=prop,ha='right',va='top')
plt.yticks(fontproperties=prop)

plt.ylabel('Num of Ventricular Beats per minute', fontproperties=prop,size=12)
plt.title('Ventricular Beats per minute',fontproperties=prop,size=18,color = '#22ACE2')

x2=pd.Series(table2['normal_time'])
y2=pd.Series(table2['Ventricular Rhythm'])
plt.scatter(x=x2, y=y2,c='#FF2B00', alpha=0.9,
            label="Luck")
plt.savefig('No.of_Beats_'+str(random.randint(1,100000))+'.png', dpi=200, facecolor='w', edgecolor='w',
       orientation='landscape', papertype=None, format=None,
      transparent=False, bbox_inches='tight', pad_inches=0.1,
       frameon=None, metadata=None)



yticks = []
ypos=[]
fig= plt.figure(figsize=(10,5))

i=0
while(i<(table2['percent'].max()+3)):
    ypos.append(i)
    yticks.append(str(i)+'%')
    i = i+5
    

plt.grid(b=None, which='major', axis='both',linewidth=0.2)
plt.xlim(table2['normal_time'][0],table2['normal_time'][-1])


if((table2['percent'].max())%2==0):
    plt.ylim(0,int(table2['percent'].max()+2))
else:
    plt.ylim(0,int(table2['percent'].max()+3))

plt.xticks(tickspos,ticklabels,rotation=35,fontproperties=prop,ha='right',va='top')
plt.yticks(ypos,yticks,fontproperties=prop)

plt.ylabel('% of Ventricular Beats per minute', fontproperties=prop,size=12)
plt.title('% of Ventricular Beats per minute',fontproperties=prop,size=18,color = '#22ACE2')

x2=pd.Series(table2['normal_time'])
y2=pd.Series(table2['percent'])
plt.scatter(x=x2, y=y2,c='#FF2B00', alpha=0.9,
            label="Luck")
plt.savefig('percentage_'+str(random.randint(1,100000))+'.png', dpi=200, facecolor='w', edgecolor='w',
       orientation='landscape', papertype=None, format=None,
      transparent=False, bbox_inches='tight', pad_inches=0.1,
       frameon=None, metadata=None)




