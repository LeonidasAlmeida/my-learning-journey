#problem: you need to select individual data or slices of a dataframe
#solution: use loc or iloc to select one or more rows or values
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#select first row
print(dataframe.iloc[0])
#select four rows
print(dataframe.iloc[1:4])