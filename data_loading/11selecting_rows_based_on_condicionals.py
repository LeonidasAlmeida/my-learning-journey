#problem:you want to select DataFrame rows based on some condition.
#solution: this can be easily done in pandas. For example, if we wanted to select all the women on Titanic
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data 
dataframe = pd.read_csv(url)
#show top two rows where column 'sex' is 'female'
print(dataframe[dataframe['Sex'] == 'female'].head(10))
#Filter rows
print(dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 65 )].head(10))