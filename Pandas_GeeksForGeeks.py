import pandas as pd
# A pandas dataframe with two-dimensional list
# lst = [['Geek',25], ['is', 30],
#        ['for',26],['GeeksForGeeks',22]]
#
# df = pd.DataFrame(lst, columns=['Tag', 'number'])
# print(df)
# lst = [['tom', 'reacher', 25], ['krish', 'pete', 30],
#        ['nick', 'wilson', 26], ['juli', 'williams', 22]]
# df = pd.DataFrame(lst,columns=['FName', 'LName','Age'],dtype=float)
# print(df)

#initialise data of lists
# data = {'category': ['Array', 'Stack','Queue'],
#         'Marks':[20,21,19]}
# #Create DataFrame
# df = pd.DataFrame(data)
# print(data)
# print(df)

data = {'Category':['Array','Stack', 'Queue'],
        'Student_1':[20,21,19], 'Student_2':[15,20,14]}

df = pd.DataFrame(data)

print(df.transpose())

#Providing index list to dataframe
df = pd.DataFrame(data, index =['Cat_1', 'Cat_2', 'Cat_3'])
print(df)
