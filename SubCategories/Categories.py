# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:40:41 2019

@author: Nanda Krishna K S
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv("flipkart_com-ecommerce_sample.csv")

import re
import nltk
from nltk.stem.porter import PorterStemmer

cat=[]

for i in range (0,101):
    raw = re.sub('[^a-zA-Z]',' ',dataset['product_category_tree'][i])
    raw=raw.lower()
    raw=raw.split()
    ps=PorterStemmer()
    raw_new=[]
    for word in raw:
        if(len(ps.stem(word))!=1):
            raw_new.append(ps.stem(word))
    raw_new=' '.join(raw_new)       
    cat.append(raw_new)   
        
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(cat).toarray()
