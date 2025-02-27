import numpy as np
import pandas as pd 

dtc=pd.read_csv('C:\\LEVEL-2 SEM-2\\Data-Science\\EDA data\\treatments_cut.csv')
dt=pd.read_csv('C:\\LEVEL-2 SEM-2\\Data-Science\\EDA data\\treatment.csv')
dp=pd.read_csv('C:\\LEVEL-2 SEM-2\\Data-Science\\EDA data\\patients.csv')
da=pd.read_csv('C:\\LEVEL-2 SEM-2\\Data-Science\\EDA data\\adverse_reactions.csv')

#unclean data -> dirty data(quality issue)-(duplicate,missing,corrupt,inaccurate data) ,
# messy data(tidiness issue/structural issues) ->

print(dp.head(1))
#assessment stycle types
# manual, programatic

# with pd.ExcelWriter('output.xlsx') as writer:
#    dt.to_excel(writer,sheet_name='treatment')
#    dp.to_excel(writer,sheet_name='patients')
#    dtc.to_excel(writer,sheet_name='treatments_cut')
#    da.to_excel(writer,sheet_name='adverse_reactions')