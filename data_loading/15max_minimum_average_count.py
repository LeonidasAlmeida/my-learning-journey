#problem: you want to find the min, max,sum,average or count of numeric column
#solution: pandas comes with some built-in methods for commonly used descriptive statistics such as min,max,mean sum and count
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
print('Maximum:',dataframe['Age'].max())
print('Minimum:',dataframe['Age'].min())
print('Mean:',dataframe['Age'].mean())
print('Sum:',dataframe['Age'].sum())
print('Count:',dataframe['Age'].count())