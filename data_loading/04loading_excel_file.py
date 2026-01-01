#problem: you need to import an Excel spredsheet
#solution: use the pandas library read_excel to load an excel spreadsheet
#load library
import pandas as pd
#create a url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.xlsx'
#load data
dataframe = pd.read_excel(url, sheet_name=0)
#view the first two rows
print(dataframe.head(2))