import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:\\LEVEL-2 SEM-2\\New folder\\matches - matches.csv')
#print(df)
head = df.head() # head function just 5 row dekhabe opor theke 
#head= df.head(2/5/133/etc)
#print(head)
tail = df.tail()
#print(tail)
# same as head but nich theke dekhabe
shape= df.shape # shape holo akta attrubute ja row and colum dekhabe kototi ache 
#shape[0] =row
#shape[1]=colum dekhabe
#print(shape)
#info=df.info()
#print(info) # memory koto use kore, data type ,index ,row, entities etc discuss kore.
describe=df.describe()
#print (describe) # numerical data ar opor kaj kore

c1=df['winner'] # shudu winner colum dekhabe
#print(c1)
#print(type(c1)) this is a series.
many_c1=df[['team1', 'team2','winner']]
#print(many_c1)# this is dataframe

#like python
iloc=df.iloc[0]# 0 index a ja ache tai dekhabe 
iloc3=df.iloc[3]# 3 .. ......................
ilocm=df.iloc[1:5] #2,3,4,5..................
ilocn=df.iloc[1:5:2] # 2,4...................
# like numpy 
ilocmn=df.iloc[:,[4,5,10]] # row sob dekhabe abong colum dekhabe 4,5,10 no. index.
#print(ilocmn)

#condition vvi --specific kono condition ar opor data khuja 
mask=df['city']=='Hyderabad' # return korbe true or false
mask1=df[mask] # jader city hydrabad tader dekhabe

#print(mask)
count=mask.shape[0] # hydrabad a kototi match hoyeche ta ber kore ==49
#print(count)
# jokhon 2/3... condition thakbe 
mask2= df['city']=='Hyderabad'
df['date'] = pd.to_datetime(df['date'])
mask3= df['date']>'2010-01-01' # 2010 ar porer match 
mask0=df[mask2 & mask3]
#print(mask0)
count=mask0.shape[0]
#print(count)

# protiti dol koita kore match win koreche ta dekhaw

win =df['winner'].value_counts() # catagory kore output dei. like group by
#print(win)


#plot function 
 
#plot=df['winner'].value_counts().plot(kind='barh')
#plt.show()
#plot=df['winner'].value_counts().head().plot(kind='pie')
#plt.show()
#plot=df['toss_decision'].value_counts().plot(kind='pie')
#plt.show()
#plot=df['win_by_runs'].plot(kind='hist') # numerical value tai value_counts lageni

#plt.show()
myseries= df['winner'].value_counts()
#print(myseries) # this is series
single = myseries['Pune Warriors']
#print(single) # Pune Warriors koto ti match win kore
# operator perfomance in series 

operator=df['team1'].value_counts() + df['team2'].value_counts()
#print(operator) # all operator *, %,+,- etc. but index same howya lagbe.
sortV= (df['team1'].value_counts() + df['team2'].value_counts()).head() # tail() also work
#print(sortV)
sort= (df['team1'].value_counts() + df['team2'].value_counts()).sort_values()# head tail also work after s_values().
#print(sort)
sort_v= (df['team1'].value_counts() + df['team2'].value_counts()).sort_values(ascending= False).head(3)
#print(sort_v)
s=df.sort_values('city')
#s=df.sort_values('city',ascending= False)
#s=df.sort_values('city',ascending= False,inplace=true) #inplace=True data ke permanent change kore dei
# #print(s)

# dui ta colum ar opor base kore sort korbe 
sortvalues=df.sort_values(['city','date'])
#print(sortvalues)
sortval=df.sort_values(['city','date'],ascending=[True,False]) # city asc and date dsc order a sort hobe
#print(sortval)

# duplicate values drop 
#drop=df.drop_duplicates('city')
drop=df.drop_duplicates(subset=['city'])
#drop=df.drop_duplicates(subset=['city','season']) # duitar duplicate value bad diya dei
#print(drop)

# proti sale je final match jita tar sal and name ber koro
wim=df.drop_duplicates('season',keep='last')
winn=wim[['season','winner']].sort_values('season') # duita colum dekhabe base on season
print(winn)