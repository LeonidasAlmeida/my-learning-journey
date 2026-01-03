#problem: you want to rename a column in a pandas dataframe
#solution: rename columns using the rename method
#load library
import pandas as pd
#create url
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#rename column, show two rows
print(dataframe.rename(columns={'PClass':'Passanger Class'}).head(2))
print(dataframe.rename(columns={'SexCode':'Sexo_code','Sex':'Gender'}).head(3))