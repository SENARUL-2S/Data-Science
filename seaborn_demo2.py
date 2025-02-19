import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#catagorical plot-> scatter plot,

tips =pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
t=sns.load_dataset('tips')

# print(t.head())

#iris = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\iris.csv')
i=sns.load_dataset('iris')

#print(i.head())

#catagorical plot-> scatter plot

# sns.stripplot(t,x='day',y='total_bill')
# plt.show()

# axes level plot
# sns.stripplot(t,x='day',y='total_bill',jitter=False) # jitter ak line a dekhabe
# plt.show()

# figure level plot
# sns.catplot(t,x='day',y='total_bill',kind='strip',hue='sex',jitter=1) # jitter ar man koma bara jai 
# plt.show()

# swarm plot 
# sns.catplot(t,x='day',y='total_bill',kind='swarm')
# plt.show()
# axes level
# sns.swarmplot(t,x='day',y='total_bill',hue='sex') # swarm plot choto data niya kaj kore 
# plt.show()


# distribution plot -> box,violin plot

# boxplot-> mean,max,min,mediun,quartle
# sns.boxplot(t,x='sex',y='total_bill')
# plt.show()

# sns.boxplot(t,x='day',y='total_bill')
# plt.show()

# figure level
# sns.catplot(t,x='day',y='total_bill',kind='box')
# plt.show()

# sns.catplot(t,x='day',y='total_bill',kind='box',hue='sex')
# plt.show()


# sns.boxplot(t,y='total_bill',hue='sex')
# plt.show()


# violin plot-> (box + kde plot)
# sns.violinplot(t,x='day',y='total_bill')
# plt.show()

# sns.catplot(t,x='day',y='total_bill',kind='violin',hue='sex')
# plt.show()

# sns.catplot(t,x='day',y='total_bill',kind='violin',hue='sex',split=True)
# plt.show()


#estimate plot -> for central tendency

# bar plot
# sns.barplot(t,x='sex',y='total_bill')
# plt.show()

# sns.barplot(t,x='sex',y='total_bill',hue='smoker',estimator=np.std)
# plt.show()

# error bar asbe na
# sns.barplot(t,x='sex',y='total_bill',hue='smoker',estimator=np.std,ci=None)
# plt.show()

# sns.barplot(t,x='sex',y='total_bill',hue='smoker',estimator=np.median)
# plt.show()
# sns.barplot(t,x='sex',y='total_bill',hue='smoker',estimator=np.min)
# plt.show()

# point plot-> different bole dei

# sns.pointplot(t,x='sex',y='total_bill',hue='smoker',estimator=np.min)
# plt.show()

# sns.pointplot(t,x='sex',y='total_bill',estimator=np.min)
# plt.show()


# countplot-> value count kore graph dei
# sns.countplot(t,x='sex')
# plt.show()

# sns.countplot(t,x='sex',hue='day')
# plt.show()


# fecet plot

# sns.catplot(t,x='sex',y='total_bill',col='smoker' ,kind='box')

# sns.catplot(t,x='sex',y='total_bill',col='smoker' ,kind='box',row='time')
# plt.show()


#regresion 
# axses level 
# sns.regplot(t,x='total_bill',y='tip')# hue use kora jai na
# plt.show()

# # figure level 
# sns.lmplot(t,x='total_bill',y='tip',hue='sex')
# plt.show()

# residplot
# sns.residplot(t,x='total_bill',y='tip') # hue use kora jai na
# plt.show()


# facetgrid 

# sns.catplot(t,x='sex',y='total_bill',col='smoker' ,kind='box',row='time')
# plt.show()


# s=sns.FacetGrid(t,col='day',row='time')
# s.map(sns.violinplot,'sex','total_bill')
# plt.show()


# s=sns.FacetGrid(t,col='day',row='time')
# s.map(sns.boxplot,'sex','total_bill')
# plt.show()

# s=sns.FacetGrid(t,col='day',row='time')
# s.map(sns.barplot,'sex','total_bill')
# plt.show()


# pairplot-> prothom colum ar sathe ditio,2 ar sathe 3,..... graph 

# sns.pairplot(i)
# plt.show()

# sns.pairplot(i,hue='species') # speces ar sathe protiti colum ar graph 
# plt.show()


#PairGrid -> last 20 minutes see session-26
# JointPlot

print(sns.get_dataset_names())
