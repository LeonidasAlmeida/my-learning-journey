#problem:you need to sort a dataframe by the values in a column
#solution:use the pandas sort_values function
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#sort the dataframe by Age
print(dataframe.sort_values(by=["PClass"]).head(10))#sorting values by PClass