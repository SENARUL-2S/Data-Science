
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
df=pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\bpl.csv')
#print(df)
#plot=df['winner'].value_counts().head(7).plot(kind='pie')
plot=df['winner'].value_counts().head(7).plot(kind='bar',levels='matchname',y='jita')
plt.show()


#('line', 'bar', 'barh', 'kde', 'density', 'area', 'hist', 'box', 'pie', 'scatter', 'hexbin')
#win=df['winner'].value_counts().head()
#p=win.plot(kind='pie')
#print(win)
#plt.show()
#ps=win.sort_values()
#print(ps)
pf=df.corr()
#print(pf)

dropna = df.dropna()
#print(dropna.to_string())
replace=df.loc[7, 'Duration'] = 45


