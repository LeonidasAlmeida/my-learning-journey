#problem: you need to load a JSON file for data preprocessing
#solution: the pandas library provides read_json to convert a JSON file into pandas object
#load library
import pandas as pd
#create a url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.json'
#load data
dataframe = pd.read_json(url, orient='columns')
#view the first two rows
print(dataframe.head(2))