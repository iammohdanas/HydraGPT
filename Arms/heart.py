import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder


def predictHeartDisease():
    dataset=pd.read_csv('C:\\Users\\aaana\HydraGPT\\Arms\\heart.csv')
    X=dataset.iloc[:,:-1].values
    Y=dataset.iloc[:,-1].values  #chosing y as last column with all rows

    #defining object for each column seperately
    le1= LabelEncoder()  #denote first index
    le2= LabelEncoder()  
    le6= LabelEncoder()  # denotes resting ecg and goes on
    le8= LabelEncoder()
    le10= LabelEncoder()

    #we are transforming this into the endcoded form

    X[:,1] = le1.fit_transform(X[:,1])
    X[:,2] = le2.fit_transform(X[:,2])
    X[:,6] = le6.fit_transform(X[:,6])
    X[:,8] = le8.fit_transform(X[:,8])
    X[:,10] = le10.fit_transform(X[:,10])

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train , Y_test  =  train_test_split(X,Y,test_size=0.2,random_state=0)

    from sklearn.preprocessing import StandardScaler
    sc= StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    from sklearn.linear_model import LogisticRegression
    model_logistic = LogisticRegression()  ## instance of the class
    model_logistic.fit(X_train,Y_train) 


    from sklearn.svm import SVC
    model_svm = SVC()  #instance
    model_svm.fit(X_train,Y_train)
    y_pred_logistic = model_logistic.predict(X_test)  ## bcz we are testing model on X_test
    y_pred_svm = model_svm.predict(X_test)

    Age = input('Enter the Age: ')
    Sex = input('Enter the Gender\n(For female Enter 0 and for male Enter 1):\n ')
    ChestPainType= input('Enter the ChestPainType:\n Enter 0 for ASY: \n Enter 1 for ATA:\n Enter 1 for NAP: \n Enter 1 for TA: \n')
    RestingBP = input('Enter RestingBP:\n ')
    Cholestrol = input('Enter the Cholestrol value \n')
    FastingBS = input('Enter the Fasting Blood Sugar \n')
    RestingECG = input('Enter the Resting Electrocardiogram (ECG): \n Type 0 for LVH \n Type 1 for Normal \n Type 2 for ST \n ')
    MaxHR = input('Enter the MaxHR: \n ')
    ExerciseAngina= input('Enter the ExerciseAngina: \n Type 1 if Yes \n Type 0 if No \n')
    Oldpeak = input('Enter the value of Oldpeak: (Type the value in decimal)  \n')
    ST_Slope = input('Enter the value of ST_Slope: \n Type 0 if down: \n Type 1 if flat \n Type 2 if up \n')

    result= model_svm.predict(sc.transform([[Age,Sex,ChestPainType,RestingBP,Cholestrol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]]))
    if result == [0]:
        print("Person is not having any heart disease")
    else:
        print("Person is having heart disease")
