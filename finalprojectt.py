import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


iris=pd.read_csv('IRIS.csv')
print(iris)#prints the csv data

print(iris.head())#prints the first 5 values
print(iris.tail())#prints the last 5 values

print(iris.head(3))#specify the number of rows to be displayed from first
print(iris.tail(3))#specify the number of rows to be displayed from last

print(iris.info())#prints some basic information about the dataset

print(iris.shape)#checks the dimension of the dataset

print(str(iris))#data structure



print(iris.columns)#checks the column names or feature names

#visual representation of dataset
plt.plot(iris["species"])
plt.xlabel("No. of data points")
plt.show()

#to plot a histogram
plt.hist(iris["species"],color="green")
plt.show()




print(iris.describe())#prints some basic information about the dataset

print(iris.max())#max
print(iris.min())#min
print(iris.sum())#sum

print(iris['species'].values_counts())#prints how many points of each class



