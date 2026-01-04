#problem: you want to dorp duplicate rows from your dataframe
#solution: use drop_duplicates, but be mindful of the parameters
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#drop duplicates, show first two rows of output
print(dataframe.drop_duplicates().head(2))
#	Drop	duplicates
dataframe.drop_duplicates(subset=['Sex'])