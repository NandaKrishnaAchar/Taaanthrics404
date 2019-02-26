# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 02:33:18 2019

@author: ankita1999
"""

  # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing libraries
import pandas as pd
import random
import numpy as np
import datetime

#importing dataset
dataset=pd.read_csv(r'C:\Users\ankita1999\Downloads\crowddatasetforsihmodified.csv')

#datafreme
df=pd.DataFrame(dataset[0:10])

dates=[]

#assumed input
notificationid=9

#taking today's date
d=datetime.date.today()

#random generation of purchase date and warranty
for i in range(0,10):
    dates.insert(i,(d-datetime.timedelta(days=random.randrange(0,2*365))))
df['Purchased date']=dates
df['Warranty']=[12,24,12,12,1,24,12,1,12,12]

#function to check whether to send notification or not based on warranty
def  expirycheck(): 
     global notificationid
     index=df.index[df['Notificationid']==notificationid]
     purchase=df.loc[index,'Purchased date'].values
     warranty=df.loc[index,'Warranty']
     expiry=(purchase+datetime.timedelta(days=int(warranty)*30))
     tday=(datetime.date.today())
     print(expiry)
     if(expiry <= tday):
        return 1
     else:
        return 0
    
#function call
expirycheck()