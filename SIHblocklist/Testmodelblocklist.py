#importing libraries
import pandas as pd
from sklearn.externals import joblib


#importing dataset
dataset=pd.read_csv(r'crowddatasetforsihmodified.csv')

wishlist=pd.DataFrame(dataset)
wishlist=wishlist.iloc[0:50]
wishlist=wishlist[['Catagory','Color','Discount']]

#input
ip=wishlist.iloc[0:1,:].values

def block():
    global ip
    """wishlist['Interest']=1
index=wishlist.index[wishlist['Catagory']=="Fashion"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Color']=="Tomato"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Discount']==5].tolist()
wishlist.loc[index,'Interest']=0"""

   

    #checkingforcategory labelencoder
    mj=joblib.load('catfile')
    ip[:,0]=mj.transform(ip[:,0]) 

    #checkingforcolor encoder
    mj1=joblib.load('colfile')
    ip[:,1]=mj1.transform(ip[:,1]) 

    #checkingforcategory onehotencoder
    mj2=joblib.load('catfile1')
    ip=mj2.transform(ip).toarray()  

    #checkingforcolor onehotencoder
    mj3=joblib.load('colfile1')
    ip=mj3.transform(ip).toarray()  

    #for final prediction
    mj4=joblib.load('trainfile')
    predict=mj4.predict(ip)  
    print(predict)
    return predict

#function call
block()