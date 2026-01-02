#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data as a dataframe
dataframe = pd.read_csv(url)
#show first 5 row
print(dataframe.head(5))