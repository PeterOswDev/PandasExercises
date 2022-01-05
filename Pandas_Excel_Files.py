import pandas as pd
import numpy as np


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df = pd.read_csv(r'E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv')
# print(df)
# print(df.dtypes)
#
# #Write a Pandas program to read specific columns from a given excel file
# cols = [1, 2, 4]
# df = pd.read_csv('E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv', usecols=cols)
# print(df)


#Write a Pandas program to insert a column in the sixth position of the said excel sheet and fill it with NaN values

df.insert(3,"column1",np.nan)
print(df.head)
