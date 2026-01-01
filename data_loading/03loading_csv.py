#problem: you need to import a comma-separated values(CSV) file
#solution: use the pandas library read_csv to load a local or hosted csv file into a pandas dataframe:
#load library
#create URL
import pandas as pd
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.csv'
#load dataset
dataframe = pd.read_csv(url)
#view first two rows
print(dataframe.head(3))