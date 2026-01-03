#replacing values
#problem: you need to replace values in a Dataframe
#solution pandas's replace is an easy way to find replace values.
#load library
import pandas as pd
#create URL
url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
#load data
dataframe = pd.read_csv(url)
#replace values, show two rows
print(dataframe['Sex'].replace("female","Woman").head(2))
#replace "female" and  "male with" "Woman" and "Man"
print(dataframe['Sex'].replace(["female","male"],["Woman","Man"]).head(5))
#replace values, show two rows
print(dataframe.replace(1, "One").head(2))
#replace values, show two rows
print(dataframe.replace("1st","First",regex=True).head(10))