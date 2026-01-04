#problem : you want to delete one or more rows from a dataframe
#solution:use a boolean condition to create a new dataframe excluding the rows you want to delete
#load data
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#delete rows, show first two rows of output
print(dataframe[dataframe['Sex'] != 'male'].head(2))