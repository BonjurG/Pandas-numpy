import pandas as pd

'''Посчитайте суммарную вместительность велосипедных парковок в районе Тропарёво-Никулино.'''

store = pd.HDFStore('data_store2.h5', mode='a')
a = store['parking_table']
df = pd.DataFrame(a)
df = df[['District', 'Capacity']]
df1 = df[df['District'] == 'район Тропарёво-Никулино'].sum()
