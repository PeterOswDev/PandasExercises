import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df = pd.read_csv('E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv', na_values={
    'price': ["?", "n.a"],
    'stroke':["?","n.a"],
    'horsepower':["?","n.a"],
    'peak-rpm':["?","n.a"],
    'average-mileage':["?","n.a"]

})
print(df)
#df.to_csv('E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv')

print(df[['company', 'price']][df.price == df['price'].max()])

car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)
print(df['company'].value_counts())


print(car_Manufacturers['company','price'].max())

print(car_Manufacturers['company','average-mileage'].mean())

carsDF =pd.read_csv('E:\Jezyki_programowania_ksiazki\Python\Pandas\Automobile_data.csv')
carsDF = carsDF.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDF.head(5))

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMW','Audi'],'Price':[23845, 171995, 135925, 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)
carsDf = pd.concat([carsDf1,carsDf2], keys = ["Germany", "Japan"])
print(carsDf)



Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_PriceDf=pd.DataFrame.from_dict(Car_Price)
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf_1 = pd.merge(car_PriceDf,carsHorsepowerDf, on="Company")
print(carsDf_1)

