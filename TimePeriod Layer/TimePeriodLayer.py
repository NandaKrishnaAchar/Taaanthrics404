import os
import time
 
def child(t):
   time.sleep(t)
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent(featureList):
   while True:
      #Creating Child Process:
      newpid = os.fork()

      #Importing Dataset
      from datetime import datetime  
      from datetime import timedelta  
      import pandas as pd
      import numpy as np
      
      #Creating Feature List
      featureList.insert(0,int(datetime.now().day)//3)
      x_query=np.asarray(featureList).reshape(1,-1)
      
      #Importing DataSet
      dataset = pd.read_csv("DataSet2.csv")
      X=dataset.iloc[:,1:-1].values
      y=dataset.iloc[:,-1].values
      
      #LabelEncoder and OneHotEncoder
      from sklearn.preprocessing import LabelEncoder,OneHotEncoder
      labelencoder=LabelEncoder()
      X[:,1]=labelencoder.fit_transform(X[:,1])
      x_query[:,1]=labelencoder.transform(x_query[:,1])
      onehotencoder=OneHotEncoder(categorical_features=[-2])
      X=onehotencoder.fit_transform(X).toarray()
      x_query=onehotencoder.transform(x_query).toarray()
      x_query=x_query[:,1:]
      X=X[:,1:]
    
      #Spliting:
      from sklearn.model_selection import train_test_split
      X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25,random_state=1348882)
            
      #MLModel Training:
      from sklearn.neighbors import KNeighborsClassifier 
      knn = KNeighborsClassifier(n_neighbors = 3).fit(X_train, Y_train) 
      """Score is .78,.72,.74,.75,.8,.71,.81,.78"""
    
      #Best Period Prediction:
      tp=[]
      for i in range(0,11):
          l2=x_query.tolist()[0]
          l2[-2]=i
          x_query=np.asarray(l2).reshape(1,-1)
          tp.append((knn.predict(x_query)).tolist())
      tp1=[x for i in tp for x in i]
      dict2=dict(zip(range(0,11),tp1))
      dict2=sorted(dict2.items(), key=lambda kv: kv[1])

      #Correct time Calculation
      today_block=int(datetime.now().day)//3
      if(((int(datetime.now().day)%3)>0)and(today_block!=10)):
          today_block+=1
      popular_block=dict2[-1][0]
      if(popular_block<today_block):
          popular_block+=10
      Waiting_block=popular_block-today_block
      print((datetime.now()+timedelta(days=Waiting_block*3)).date())

      #time=(int((datetime.now()+timedelta(days=Waiting_block*3)).day))*60*60*24
      time=10#Since we cannot wait for many days,i have taken time as 10.Actual time formula is as above. 
      if(newpid==0):
          child(time)
      break
       
parent(['ComputerAndMobile',25])#Category,Discount




