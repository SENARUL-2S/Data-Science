import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\LEVEL-2 SEM-2\\data science\\Fortune .csv', encoding='ISO-8859-1')
sector= df.groupby('Sector')
#print(df.head())
#p=sector.size().sort_values(ascending=False).head() # sector ke groupby kore dibe 
p=sector.size().sort_values(ascending=False).head().plot(kind='bar')
plt.show()
#p=len(sector)
#p= sector.first()
#p= sector.last()
#print(p)
