#problem: you want to view some characteristics of a dataframe
#solution: one of de easiest things 
# we can do after loading the data 
# is view the first few rows using head
#load library
import pandas as pd
#create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#show two rows
print(dataframe.head(2))
#show dimensions
print(dataframe.shape)
#show statistics
print(dataframe.describe())
#show info
print(dataframe.info())