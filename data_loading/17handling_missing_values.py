#problem: you want to select missing values in a Dataframe
#solution: isnull and notnull return booleans indicating whether a valu is missing
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#select missing values, show two rows
print(dataframe.drop('Age',axis=1).head(2))
print(dataframe[dataframe['Age'].isnull()].head(2))
print(dataframe.drop_duplicates().head(2))
