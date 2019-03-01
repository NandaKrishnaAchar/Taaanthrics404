#importing libraries
import pandas as pd
from sklearn.externals import joblib


#importing dataset
dataset=pd.read_csv(r'crowddatasetforsihmodified.csv')


#adding column called interest
wishlist=pd.DataFrame(dataset)
wishlist=wishlist.iloc[0:50]
wishlist=wishlist[['Catagory','Color','Discount']]
wishlist['Interest']=1
index=wishlist.index[wishlist['Catagory']=="Fashion"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Color']=="Tomato"].tolist()
wishlist.loc[index,'Interest']=0
index=wishlist.index[wishlist['Discount']==5].tolist()
wishlist.loc[index,'Interest']=0

#Now wishlist dataset has Category,color,discount as independent variables 
#Interest as dependent variable 


#categorising
x=wishlist.iloc[:,:-1].values
y=wishlist.iloc[:,3].values


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
print("Accuracy:",metrics.accuracy_score(ytest, y_pred))
#0.80