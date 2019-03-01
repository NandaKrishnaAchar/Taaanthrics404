
#popularity number

#Input:Notification id
#Output:1 or 0

#importing libraries
import pandas as pd

#importing dataset
dataset=pd.read_csv(r'C:\Users\ankita1999\Desktop\Popularitydataset.csv')

#function to check whether the product is popular
def popularitycheck(notificationid):
    popularity=dataset.loc[dataset['Notificationid']==notificationid].iloc[:,10].values
    if popularity>=75:
        return 1
    return 0

#function call
popularitycheck(200)
     
