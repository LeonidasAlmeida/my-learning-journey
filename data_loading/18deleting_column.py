#problem: you want to delete a column from your dataframe
#solution:the best way to delete a columns is to use drop with the parameter axis = 1
#load library
import pandas as pd
#create a url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
print(dataframe.head(2))
#delete column
print(dataframe.drop('Age',axis=1).head(2))