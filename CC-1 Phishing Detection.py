#!/usr/bin/env python
# coding: utf-8

# # Project Name- CyberSecurity Detection
# ## Sub-Topic- Phishing Detection
# ### By- Aarush Kumar
# #### Dated: December 05,2021

# In[6]:


import numpy as np
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
from flask import jsonify


# In[7]:


def getResult(url):
    #Importing dataset
    data = np.loadtxt("/home/aarush100616/Downloads/Projects/Eagle's eye on Cybercrime/Data/dataset.csv", delimiter = ",")
    #Seperating features and labels
    X = data[: , :-1]
    y = data[: , -1]
    #Seperating training features, testing features, training labels & testing labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    clf = rfc()
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(score*100)
    X_new = []
    X_input = url
    X_new=FeatureExtraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1,-1)
    try:
        prediction = clf.predict(X_new)
        if prediction == -1:
            return "Phishing Url"
        else:
            return "Legitimate Url"
    except:
        return "Phishing Url"

