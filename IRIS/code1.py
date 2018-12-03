# make sure csv file is in working directory

import pandas as pd
from pandas import Series,DataFrame

iris_df = pd.read_csv("iris.csv")
print ( " printing...... \n" )
print(iris_df)
iris_df

print("...................g.ggggggg.......")
iris_df.info()
print("...................g.ggggggg.......")

print(iris_df.describe())
