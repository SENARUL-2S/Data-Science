import numpy as pn 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px

# data gathering -> collect data
# 1. import -> database/sql , csv, excel, text,json file 
# .csv= comma separated values, .tsv= tab seperated values
# .json=javascript on notation
# csv files

# opening a local csv file 
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv')
# print(df.head())

# # opening a csv file from URL. but required internet
# tips =pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# print(tips.head(5))

# # sep parameter 

# df=pd.read_csv('movie_tittles_metadata.tsv',sep='\t')
# print(df.head()) # akhane first index ta ke colum baniya debe

# # abar ami colum ar name o dite parbo
# df=pd.read_csv('movie_tittles_metadata.tsv',sep='\t',names=['joi ta colum tototi name pass kore dibo coma diya'])
# print(df.head())

# # index_col parametar-> index ke soriye dei
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',index_col='id')
# print(df.head())

# # header parameter -> index/row 0 te thakbe take colum name banaiye dibe
# df=pd.read_csv('test.csv',header=1)
# print(df.head())


# # use_col parameter -> jegula colum dorkar nai seigula bad diya dibo
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',usecols=[' jegula chai coma diye bosai dibo '])
# print(df.head())

# # skiprows/nrows parameter -> je sari gula dorkar nai segula hoteya dibe
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',skiprows=[0,5])
# print(df.head())

# # nrows -> sorboccho  jotogula row dorkar segula nibe 
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',nrows=100)
# print(df.head())

# #Encoding parameter -> kono file ar encoding alada thakle ta kono code editor a conver kore nibo abong sei encoding bosaiya dibo
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',encoding='latin-1')
# print(df.head())


# # skip bad lines-> jokhon kono row a besi colum thake thokhon ta skip kore dei 
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',error_bad_lines=False)
# print(df.head())

# # dtypes parametar -> data type change kore . integer a conver korle
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',dtype={'name of colum':int})
# print(df.head())

# # handling dates-> date jodi onno kono type a thake tobe 
# # take data a convert kore like string to date
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',parse_dates=['name of col'])
# print(df.head())

# convertors-> jodi kono full form thake tahole take short a ana jai arokom kichu
def rename(name):
    if name =="Royal Challengers Bangalore":
        return "RCB"
    else:
        return name
    
df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\matches - matches.csv',converters={'team1':rename})
print(df.head())

# # na_values parameter-> nan bose jabe
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv',na_values=['jar poriborte nan tar name'])
# print(df.head())




# # excel file 

# df=pd.read_excel('C:\\LEVEL-2 SEM-2\\data science\\bpl.xlsx',sheet_name='sheet ar name')
# print(df.head())

# # sob function or parameter same as csv



# #text file -> age dekhte hobe tada ta tab separate naki 
# df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.txt',sep='\t')
# print(df.head())

# # badbaki sob aki like csv



# # json file
# # opening a local json file 
# df=pd.read_json('C:\\LEVEL-2 SEM-2\\data science\\bpl.json')
# print(df.head())

# # opening a json file from URL. but required internet
# tips =pd.read_json('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.json')

# print(tips.head()) # same as csv but see json documentation



# databse/ sql file

# sql data import korar jonno software install kora lagbe

import mysql.connector  #import kora lagbe
import seaborn as sns 
# xaamp open thaka lagbe
conn= mysql.connector.connect(host='localhost',user='root',password='',database='university')
df=pd.read_sql_query("select student_name,cgpa from student_results where cgpa>3.499 order by cgpa",conn)
#print(df)# jekono query likha jabe condition sob kichu

# df['cgpa'].plot(kind='pie',labels=df['student_name'].values, autopct='cgpa')
# plt.show()

# df['cgpa'].plot(kind='pie', labels=df['student_name'].values, autopct=lambda p: f'{p * df["cgpa"].sum() / 100:.2f}')
# plt.title('student cgpa above 3.50 for nabarun-19 after 3rd sem.')
# plt.show()
# same as csv but see sqlquery documentation



# EXPORT FILE TO -> database/sql , csv, excel, text,json file
