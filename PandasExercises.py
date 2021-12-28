import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

df = pd.read_csv(r'E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv')
print(df)

print(df.head(5))
print(df.tail(5))




