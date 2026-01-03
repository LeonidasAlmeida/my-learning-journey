#problem: you need to select all unique values in a column
#solution: use unique to view an array of all unique values in a column
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#select unique values
print(dataframe['Sex'].unique())
#view all unique values and how times appear
print(dataframe['Sex'].value_counts())