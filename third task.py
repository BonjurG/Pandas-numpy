import pandas as pd

'''Скачайте выгрузку и организуйте её чтение чанками.
Размер каждого чанка установите в 30 строк.
Для пятого чанка с данными определите сколько пользователей с группой крови A+'''

df = pd.read_csv('users.csv', sep=';', chunksize=30)
totals = pd.Series([])
for i in df:
    totals = totals.add(i['blood_group'].value_counts(), fill_value=0)
    print(totals)
    break
