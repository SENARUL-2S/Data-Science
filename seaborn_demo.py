import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# relatinal plot 

#1. scatterplot

tips =pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
#print(tips.head(5))

t= sns.load_dataset('tips')
# print(t.head())

#scatter plot -> axes level plot
# sns.scatterplot(t,x='total_bill', y='tip')
# plt.show()

# # relplot -> figure level plot-> square shape
# sns.relplot(t,x='total_bill', y='tip',kind='scatter')
# plt.show()
# # figure level function use kora best

# # kar kon point ta ber kora
# sns.scatterplot(t,x='total_bill', y='tip',hue='sex')
# plt.show()
# # aro add kora
# sns.relplot(t,x='total_bill', y='tip',kind='scatter',hue='sex',style='time')
# plt.show()
# sns.scatterplot(t,x='total_bill', y='tip',hue='sex',style='time',size='size')
# plt.show()


# time series ar datai line plot best


#fecet plot _ categori ar opor vitti kore multiple plot a vag kore
# fecet plot ak matro figure level function a kaj kore

# sns.relplot(t,x='total_bill', y='tip',kind='scatter', col='smoker',row='sex',style='time')
# plt.show()

# sns.relplot(t,x='total_bill', y='tip',kind='scatter', col='smoker',row='sex',style='day')
# plt.show()


# sns.relplot(t,x='total_bill', y='tip',kind='line', col='day',style='time',col_wrap=1) # colwrap-> joto toi ta graph rakhbe ak sarite
# plt.show()


# distrubution plot -> works at central tendency(mean, avg, etc) and range
# figure level->displot
# axes level -> histplot,kdeplot,rugplot

# sns.histplot(t,x='total_bill')
# plt.show()

# sns.displot(t,x='total_bill',kind='hist') # figure level
# plt.show()

# sns.histplot(t,x='total_bill', bins=20) # bins = 1,2,3,..10,20 etc
# plt.show()


# sns.histplot(t,x='tip', hue='sex')
# plt.show()

# sns.histplot(t,x='tip', hue='sex',element='step')
# plt.show()


# feceting -> not work with histplot
# sns.displot(t,x='tip',kind='hist' ,col='sex')
# plt.show()


# kdeplot-> axses level 
# sns.kdeplot(t,x='total_bill')
# plt.show() 


# sns.displot(t,x='total_bill',kind='kde')
# plt.show()

# sns.displot(t,x='total_bill',kind='kde',hue='sex')
# plt.show()

# sns.displot(t,x='total_bill',kind='kde',hue='sex',fill=True)
# plt.show()
# sns.displot(t,x='tip',kind='hist' ,col='sex')
# plt.show()

# bivariate histogram -> dui ta colum niya kaj kore
# sns.displot(t,x='total_bill',y='tip')
# plt.show()

# sns.kdeplot(t,x='total_bill',y='tip')
# plt.show()


#matrix plot-> heatmap,clustermap
# bf= pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\batter.csv')
# pf=bf.pivot(index='batter', columns='strike_rate',values='avg')
# sns.heatmap(pf)

# plt.show()
glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
# sns.heatmap(glue)
# plt.show()

# sns.heatmap(glue, annot=True)
# plt.show()

# sns.heatmap(glue, annot=True, fmt=".1f")
# plt.show()
# sns.heatmap(glue, annot=True, fmt=".1f")
# plt.show()

# sns.heatmap(glue, annot=glue.rank(axis="columns"))
# plt.show()
# sns.heatmap(glue, annot=True, linewidth=.5)
# plt.show()
# sns.heatmap(glue, cmap="crest")

# sns.heatmap(glue, cmap=sns.cubehelix_palette(as_cmap=True))
# plt.show()
# sns.heatmap(glue, vmin=50, vmax=100)
# plt.show()