#parameters I/P:Category,Color,Discount
#If the user has blocked return 0

def blocklist():
   #importing libraries
   import pandas as pd
   from sklearn.externals import joblib


   #importing dataset
   dataset=pd.read_csv(r'C:\Users\ankita1999\Desktop\SIHfinal\User.csv')

   #Now wishlist dataset has Category,color,discount as independent variables 
   #Interest as dependent variable


   #categorising
   x=dataset.iloc[:,:-1].values
   y=dataset.iloc[:,3].values


   from sklearn.preprocessing import LabelEncoder,OneHotEncoder
   labelencoder=LabelEncoder()


   #categorising category
   x[:,0]=labelencoder.fit_transform(x[:,0])
   joblib.dump(labelencoder ,'Catfile')


   #categorising color
   x[:,1]=labelencoder.fit_transform(x[:,1])
   joblib.dump(labelencoder ,'Colfile')

   #onehotencoder category
   onehotencoder= OneHotEncoder(categorical_features= [0])
   x = onehotencoder.fit_transform(x).toarray()
   joblib.dump(onehotencoder ,'Catfile1')

   #onehotencoder color
   onehotencoder= OneHotEncoder(categorical_features= [4])
   x = onehotencoder.fit_transform(x).toarray()
   joblib.dump(onehotencoder ,'Colfile1')


   from sklearn.model_selection import train_test_split
   xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

   from sklearn import tree,metrics
   dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
   dtree.fit(xtrain, ytrain)


   joblib.dump(dtree,'trainfile')


   y_pred=dtree.predict(xtest)
   #0.80

   ip=dataset.iloc[0:1,:-1].values

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
   #blocked or not
   return predict
blocklist()