import os
os.chdir(r'C:\Users\212410226\Python & R\Python_workingDirectory\pandas_basics')

#==============================================================================
# Importing libraries - Creating data sets - Creating data frames 
# Reading from CSV - Exporting to CSV - Finding maximums - Plotting data
#==============================================================================
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas

#==============================================================================
# Create Data
#==============================================================================
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = zip(names,births)

df = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
df.to_csv('births1880.csv',index=False,header=False)

#==============================================================================
# Reading Data
#==============================================================================
df = pd.read_csv('births1880.csv',header=None,names=['Names','Births'])
os.remove('births1880.csv')

#==============================================================================
# Analyze Data
#==============================================================================
Sorted = df.sort(['Births'], ascending=False)

print df
print df.dtypes
print df.Births.dtype
print Sorted
print Sorted.head(2)
print Sorted.tail(4)
print df['Births'].max()
# Get the name with max births
print df.loc[df['Births'] == df['Births'].max(),:]
text = str(df['Names'][df['Births'] == df['Births'].max()].values) + '  ' + str(df['Births'][df['Births'] == df['Births'].max()].values)
df['Births'].plot()
plt.annotate(text, 
             xy=(1, df['Births'][df['Births'] == df['Births'].max()]), 
             xytext=(8, 0), 
             xycoords=('axes fraction', 'data'), textcoords='offset points')