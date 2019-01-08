import pandas as pd
from pandas  import Series,DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


titanic_df=pd.read_csv("train.csv")


print("-----------DATA HEADER---------------")
print(titanic_df.head())
print("----------DATA DESCRIPTION-----------")
titanic_df.info()
titanic_df.describe()
titanic_df=titanic_df.drop(["PassengerId","Name","Ticket"],axis=1)
print("------check if columns are dropped--------")
print(titanic_df.head())
titanic_df["Age"]=titanic_df["Age"].fillna(20)
print(titanic_df["Age"])
print("No of rows in the data set = ",len(titanic_df))
print("No of columns in the data set = ",len(titanic_df.columns))
print("the minimum age = ",titanic_df.Age.min())
print("the maximum age = ",titanic_df.Age.max())
print("the mean age = ",titanic_df.Age.mean())
print("the SD of age = ",titanic_df.Age.std())
titanic_df.Age.hist()
plt.show()
ax1=titanic_df.Age.hist()
ax1.set(xlabel="Age",ylabel="Number of people")
plt.show()
ax2=titanic_df.Age.plot()
ax2.set(xlabel="Age",ylabel="Number of people")
plt.show()

