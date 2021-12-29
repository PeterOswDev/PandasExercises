import pandas as pd
# A pandas dataframe with two-dimensional list
lst = [['Geek',25], ['is', 30],
       ['for',26],['GeeksForGeeks',22]]

df = pd.DataFrame(lst, columns=['Tag', 'number'])
print(df)