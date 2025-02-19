import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import mysql.connector 

# pandas export ->csv,excel,html,json,sql
#

# to_csv file

df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\matches - matches.csv')

# print(df)
# # ai data theke batsman ar tader total run dekhaw abong ta csv te save koro
# d=df.groupby('id')['winner'].sum().reset_index()
# print(df.info())

## akhane d ke filter kora ache chaile pura data ke onno file a convert korte parbo

# # d.to_csv('id_winner.csv',index=False) # index thakbe na

# # pivot table create ar niyum

# p=df.pivot_table(index='id',columns='city',values='win_by_runs',aggfunc='sum')
# print(p)
# d.to_csv('id_winner.csv',index=True)


# d=df.groupby('id')['winner'].sum().reset_index()
# d.to_csv('id_winner.xlsx',index=True)

# To_excel file

# d=df.groupby('id')['winner'].sum().reset_index()
# d.to_excel("SENARUL1.xlsx",sheet_name='senarul') # auto index niya nibe alada kore

# d=df.groupby('id')['winner'].sum().reset_index()
# d.to_excel("SENARUL1.xlsx",sheet_name='senarul',index=False)

# ak sathe 2 ta sheet banano jabe 
# d1=df.groupby('id')['winner'].sum()
# d2=df.groupby('id')['winner'].sum().reset_index()
# with pd.ExcelWriter('output.xlsx') as writer:
#    d1.to_excel(writer,sheet_name='senarul2')
#    d2.to_excel(writer,sheet_name='senarul3')


# to_html table
# ht=df.groupby('id')['winner'].sum().reset_index()
# ht.to_html('senarul.html') 

# ht=df.groupby('id')['winner'].sum().reset_index()
# ht.to_html('senarul.html',index=False) # index thakbe na id anujai thakbe



# To_json file

ht=df.groupby('id')['winner'].sum().reset_index()
ht.to_json('senarul.json') 



# To_sql file 
import pymysql
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://root:@localhost/data_gathering")
ht=df.groupby('id')['winner'].sum().reset_index()
ht.to_sql('import',con=engine,if_exists='append') 
#pip install pymysql sqlalchemy

