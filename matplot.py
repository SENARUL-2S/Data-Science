import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# types of data 
#numerical data-> age, weight, 
# categorical dta->phone name ,depertment name
# 2D plot->
# kaj kore catagorical-numerical and numerical-numerical

price =[10,15,20,9,5]
year=[2012,2013,2014,2015,2016]
# plt.plot(year,price)
# plt.show()
 
# #plt.plot(year,price)
# plt.xlim(2012,2017) # mane graph a x ar limit man 2012-2017 thakbe
# plt.ylim(0,100)
# plt.show()

df = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\sharma-kohli.csv')
# print(df)
# plt.plot(df['index'],df['V Kohli'])
# #plt.plot(df['index'],df['RG Sharma'])
# plt.show()

# tittle a x,y borabor name deya

# plt.plot(df['index'],df['V Kohli']) # duita colum ar upor
# plt.plot(df['index'],df['RG Sharma']) # akadik add kora jabe aksathe
# plt.title('rohit vs kohli')
# plt.xlabel('season')
# plt.ylabel('runs')
# plt.show()

#line ar color change korte..
# plt.plot(df['index'],df['V Kohli'],color='Green')
# plt.plot(df['index'],df['RG Sharma'],color='red')
# plt.title('rohit vs kohli')
# plt.xlabel('season')
# plt.ylabel('runs')
# plt.show()

#solid,dashed,dotted,dashdot a line ke style kora jai
# plt.plot(df['index'],df['V Kohli'],color='Green',linestyle='solid')
# plt.plot(df['index'],df['RG Sharma'],color='red',linestyle='dashed')
# plt.title('rohit vs kohli')
# plt.xlabel('season')
# plt.ylabel('runs')
# plt.show()

# line mota mihi dekhabe
# plt.plot(df['index'],df['V Kohli'],color='Green',linestyle='solid',linewidth=3)
# plt.plot(df['index'],df['RG Sharma'],color='red',linestyle='dashed',linewidth=2)
# plt.title('rohit vs kohli')
# plt.xlabel('season')
# plt.ylabel('runs')
# plt.show()

# marker joint a ai shape dekhabe + ,.,o,>,d and marker ar size o deyajabe 
# plt.plot(df['index'],df['V Kohli'],color='Green',linestyle='solid',linewidth=3,marker='d')
# plt.plot(df['index'],df['RG Sharma'],color='red',linestyle='dashed',linewidth=2,marker='o',markersize=10)
# plt.title('rohit vs kohli')
# plt.xlabel('season')
# plt.ylabel('runs')
# plt.show()

# konta line kar ta dekhar jonno label + legend() function kaj kore
# plt.plot(df['index'], df['V Kohli'], color='green', linestyle='solid', linewidth=3, 
#          marker='d', markersize=5, label='Kohli')
# plt.plot(df['index'], df['RG Sharma'], color='red', linestyle='dashed', linewidth=2, 
#          marker='o', markersize=10, label='Rohit')

# plt.title('Rohit vs Kohli')
# plt.xlabel('Season')
# plt.ylabel('Runs')
# plt.legend()
# plt.show()

# indicate korbe je legend ta kothai hobe
#'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'
# plt.plot(df['index'], df['V Kohli'], color='green', linestyle='solid', linewidth=3, 
#          marker='d', markersize=5, label='Kohli')
# plt.plot(df['index'], df['RG Sharma'], color='red', linestyle='dashed', linewidth=2, 
#          marker='o', markersize=10, label='Rohit')

# plt.title('Rohit vs Kohli')
# plt.xlabel('Season')
# plt.ylabel('Runs')
# plt.legend(loc='best') # best means jekhane faka pabe bose jabe
# plt.show()

# grid point ke nirdharon korte sahajjo kore
# plt.plot(df['index'], df['V Kohli'], color='green', linestyle='solid', linewidth=3, 
#          marker='d', markersize=5)
# plt.plot(df['index'], df['RG Sharma'], color='red', linestyle='dashed', linewidth=2, 
#          marker='o', markersize=10)

# plt.title('Rohit vs Kohli')
# plt.xlabel('Season')
# plt.ylabel('Runs')

# plt.grid()
# plt.show()
# one problem line dekhai na 

#scatter plots- numerical to numerical data niya kaj kore

dft = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\batter.csv')
pf=dft.head(50)
# # 50 joner opor kaj korbe
# plt.scatter(pf['avg'],pf['strike_rate'])
# #print(pf)
# plt.show()

# dot ar size: joto besi man toto dot boro dekhai 
# look seaborn scatter plot

# replace for scatter plot - line draw kore dibe
# plt.plot(pf['avg'],pf['strike_rate'])
# plt.show()

#same as scatter plot
# plt.plot(pf['avg'],pf['strike_rate'],'o')
# plt.show() 


# scatter- choto data niya kaj kore and slower
# plt. plot -big data niya kaj kore and faster


#Bar chart
# numerical(aggregate) vs catagoricals 
# child=[20,13,15,30,25]
# color=['red','blue','green','yellow','pink']
# plt.bar(color,child)# akhane o tittle etc. posible
# plt.show()

#vertical bora bor name dekhabe
# child=[20,13,15,30,25]
# color=['red','blue','green','yellow','pink']
# plt.bar(color,child)# akhane o tittle etc. posible
# plt.xticks(rotation='vertical')
# plt.show()

# color change 
# child=[20,13,15,30,25]
# color=['red','blue','green','yellow','pink']
# plt.bar(color,child, color='red')# akhane o tittle etc. posible
# plt.show()

# horigental  bar 
# child=[20,13,15,30,25]
# color=['red','blue','green','yellow','pink']
# plt.barh(color,child, color='red')# akhane o tittle etc. posible
# plt.show()


#multiple bar plot vvi
d = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\batsman_season_record.csv')
# plt.bar(d['batsman'],d['2015'],width=0.5) # width bar ar size komabe
# plt.show()

# matplotlib_advanced a easy way te deya acse

# d.plot(kind='bar')
# plt.show()

#or
# plt.bar(np.arange(d.shape[0])-0.2,d['2015'],width=0.2)
# plt.bar(np.arange(d.shape[0]),d['2016'],width=0.2)
# plt.bar(np.arange(d.shape[0])+0.2,d['2017'],width=0.2)
# plt.show()

# name niche dekhar jonno 
# plt.bar(np.arange(d.shape[0])-0.2,d['2015'],width=0.2 , color='red')
# plt.bar(np.arange(d.shape[0]),d['2016'],width=0.2)
# plt.bar(np.arange(d.shape[0])+0.2,d['2017'],width=0.2)
# plt.xticks(np.arange(d.shape[0]),d['batsman']) # ...............
# plt.show()


#stacked bar chart - aktar opor arekta thake 

# matplotlib_advanced a easy way te deya acse
# df.plot(kind='bar',stacked=True)
# plt.show()

# plt.bar(d['batsman'],d['2015'] , color='red')
# plt.bar(d['batsman'],d['2016'] ,bottom=d['2015'] , color='blue')
# plt.bar(d['batsman'],d['2017'] ,bottom=(d['2015'] +d['2016'] ), color='yellow')
# plt.show()


#histogram -numerical , frequency count

vk = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\vk.csv')
# plt.hist(vk['batsman_runs'])
# plt.show()
# plt.style.use('ggplot')
# plt.hist(vk['batsman_runs'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
# plt.show()


#pie chart - catagoricals , numericals => 100 a koto % 

# age=[20, 25,30,15,100]
# plt.pie(age)
# plt.show()

# karage koto ta bole deya 
# age=[20, 25,30,15,100]
# name=['A','B','C','D','E']

# plt.pie(age ,labels= name )
# plt.show()

gale=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\gayle-175.csv')

# plt.pie(gale['batsman_runs'],labels=gale['batsman'],autopct= '%0.1f%%')
# plt.show()

#color change 

# chart save hobe-> plt.savefig("sample.png")

# plt.pie(gale['batsman_runs'],labels=gale['batsman'],autopct= '%0.1f%%',colors=['red','blue','green','yellow','pink','brown'])
# plt.savefig("sample.png") 
# plt.show()

# bahir howya
# plt.pie(gale['batsman_runs'],labels=gale['batsman'],autopct= '%0.1f%%',explode=[0.1,0,0,0,0,0])
# plt.show()

#styles 
# plt.style.available

# plt.style.use('color_name dite hobe')
#exaple
plt.style.use('ggplot')
age=[20, 25,30,15,100]
name=['A','B','C','D','E']
plt.pie(age ,labels= name )
plt.show()