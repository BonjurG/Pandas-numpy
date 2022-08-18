import pandas as pd

'''Прочитайте первые 50 записей выгрузки и определите количество мужчин.'''

df = pd.read_csv('users.csv', sep=';')
print(df.sex[0:50].value_counts()['M'])
