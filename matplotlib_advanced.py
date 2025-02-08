import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\iris.csv')

#print(iris.head())
# print(iris.sample(5))
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'])
# #plt.show()
# iris['Species']=iris['Species'].replace({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'])
# plt.xlabel('sepal')
# plt.ylabel('petal')
# plt.show()

#color chane kore
# iris['Species']=iris['Species'].replace({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='winter') # anek matplotlib cmap color ache
# plt.xlabel('sepal')
# plt.ylabel('petal')
# plt.show()

# pase akta color cmap dei
# iris['Species']=iris['Species'].replace({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='winter') # anek matplotlib cmap color ache
# plt.xlabel('sepal')
# plt.ylabel('petal')
# plt.colorbar()
# plt.show()

# alpha color ar regulation dei
# iris['Species']=iris['Species'].replace({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='winter',alpha=0) # alpha ar man bara koma jabe 0-1
# plt.xlabel('sepal')
# plt.ylabel('petal')
# plt.show()

# figure ar size bara koma
# plt.figure(figsize=[11,10])# width=10 ,length=11
# iris['Species']=iris['Species'].replace({'Iris-setosa': 0,'Iris-versicolor':1,'Iris-virginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='winter') # anek matplotlib cmap color ache
# plt.xlabel('sepal')
# plt.ylabel('petal')
# plt.show()

#text likha figure ar moddhe
# x=[10,20,30,40]
# y=[5,6,7,8]
# plt.scatter(x,y)
# plt.text(10,5,'p1')
# plt.text(20,6,'p2')
# plt.text(30,7,'p3')
# plt.text(40,8,'p4')
# plt.show()

# x=[10,20,30,40]
# y=[5,6,7,8]
# plt.scatter(x,y)
# plt.text(10,5,'p1')
# plt.text(20,6,'p2')
# plt.text(30,7,'p3')
# plt.text(40,8,'p4',fontdict={'size':12,'color':'red'})
# plt.show()


# df = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\batter.csv')
# pf=df.head(50)
# plt.scatter(pf['avg'],pf['strike_rate'])
# for i in range(pf.shape[0]):
#      plt.text(pf['avg'].values[i],pf['strike_rate'].values[i],pf['avg'],pf['batter'].values[i])
# plt.show()

df = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\batter.csv')
# plt.figure(figsize=[12,10])
# pf = df.head(20)
# plt.scatter(pf['avg'], pf['strike_rate'],s=pf['runs']) # s= means jar run besi se dot boro hobe

# for i in range(pf.shape[0]):
#     plt.text(pf['avg'].values[i], pf['strike_rate'].values[i], pf['batter'].values[i])

# plt.show()

# horigental and vertical lines

# plt.figure(figsize=[12,10])
# pf = df.head(20)
# plt.scatter(pf['avg'], pf['strike_rate'],s=pf['runs']) # s= means jar run besi se dot boro hobe
# plt.axhline(130,color='red') # strike rate 130 ar opor jader tader alada korbe
# plt.axvline(30,color='red')#avg 30 ar opor jader tader alada korbe
# for i in range(pf.shape[0]):
#     plt.text(pf['avg'].values[i], pf['strike_rate'].values[i], pf['batter'].values[i])

# plt.show()


# plt.figure(figsize=(12,10))
# plt.scatter(df['avg'], df['strike_rate']) # s= means jar run besi se dot boro hobe
# plt.title('somthing')
# plt.xlabel('avg')
# plt.ylabel('strike_rate')
# plt.show()


# same as above part


# fig, ax= plt.subplots(figsize=(11,10))
# ax.scatter(df['avg'], df['strike_rate'])
# ax.set_title('somthing')
# ax.set_xlabel('avg')
# ax.set_ylabel('strike_rate')
# # fig.show()
# plt.show()


# fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8))  # Create 2 subplots

# # First scatter plot
# ax[0].scatter(df['avg'], df['strike_rate'])
# ax[0].set_title('Something')  # Corrected title method
# ax[0].set_xlabel('Avg')
# ax[0].set_ylabel('Strike Rate')

# # Second scatter plot
# ax[1].scatter(df['avg'], df['runs'])
# ax[1].set_title('Something')  # Corrected title method
# ax[1].set_xlabel('Avg')
# ax[1].set_ylabel('Runs')

# plt.tight_layout()  # Adjust layout for better spacing
# plt.show()


# fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8), sharex=True)  # Create 2 subplots

# # First scatter plot
# ax[0].scatter(df['avg'], df['strike_rate'],color='red')
# ax[0].set_title('Something')  # Corrected title method

# ax[0].set_ylabel('Strike Rate')

# # Second scatter plot
# ax[1].scatter(df['avg'], df['runs'])
# ax[1].set_title('Something')  # Corrected title method
# ax[1].set_xlabel('Avg')
# ax[1].set_ylabel('Runs')

# plt.tight_layout()  # Adjust layout for better spacing
# plt.show()


# ak ar odhik grph ak sathe vvi

# fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))  # Create 2 subplots

# First scatter plot
# ax[0, 0].scatter(df['avg'], df['strike_rate'], color='red')
# ax[0, 1].scatter(df['avg'], df['runs'])
# ax[1, 0].hist(df['avg'])  # You may want to add another argument for the second axis
# ax[1, 1].hist(df['runs'])  # Just an example, you can adjust as needed

# plt.tight_layout()  # Adjust layout for better spacing
# plt.show()


# 3D scatter plots- 3 man niya kaj kore
# ax=plt.subplot(projection='3d')
# ax.scatter3D(df['runs'],df['avg'], df['strike_rate'])
# plt.show()

# ax=plt.subplot(projection='3d')
# ax.scatter3D(df['runs'],df['avg'], df['strike_rate'])
# ax.set_title('somthing')
# ax.set_xlabel('runs')
# ax.set_ylabel('avg')
# ax.set_zlabel('strike_rate')
# plt.show()

# ax=plt.subplot(projection='3d')
# ax.plot3D(df['runs'],df['avg'], df['strike_rate'])
# ax.set_title('somthing')
# ax.set_xlabel('runs')
# ax.set_ylabel('avg')
# ax.set_zlabel('strike_rate')
# plt.show()

ax=plt.subplot(projection='3d')
ax.plot3D(df['runs'],df['avg'], df['strike_rate'],color='red')
ax.set_title('somthing')
ax.set_xlabel('runs')
ax.set_ylabel('avg')
ax.set_zlabel('strike_rate')
plt.show()