import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("100 Records.csv")
'''print(data.head())
print(data.tail())
print(data.describe())
print(data.size)
print(data.shape)
print(data.info)'''
print(data["Year of Joining"].value_counts()[0:2018])
list(data["Year of Joining"].value_counts()[0:2018])
plt.figure(figsize=(10,10))
plt.bar(list(data["Year of Joining"].value_counts()[0:2018].keys()),list(data["Year of Joining"].value_counts()[0:2018]),color="r",align="center")
print(plt.show())
