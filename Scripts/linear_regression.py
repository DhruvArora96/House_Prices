from sklearn.linear_model import LinearRegression
import pandas as pd 
import numpy as np 

df_train = pd.read_csv("../Data/train.csv")
df_test = pd.read_csv("../Data/test.csv")
print(df_train.head())