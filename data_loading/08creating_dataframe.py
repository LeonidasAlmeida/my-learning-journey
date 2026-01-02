#problem: you want to create a new dataframe
#solution: pandas has many methods of creating a new dataframe object.
#  one easy method is to instantiate a dataframe using a python dictionary.
#load library
import pandas as pd
#create a dictionary
dictionary = {
    "Name":['Jacky Jackson','Steven Stevenson'],
    "Age":[38,25],
    "Drive":[True,False]
}

#Create DataFrame
dataframe = pd.DataFrame(dictionary)
#add a columns to any dataframe using a list of values:
dataframe["Eyes"]=["Brown","Blue"]
#show Dataframe
print(dataframe)
print(dataframe.shape)