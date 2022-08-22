import pandas as pd

'''Порекомендуйте  ТОП-3 района по количеству зарядных станций. Андрей уже подготовил для вас выгрузку в Excel - данные на двух листах. '''

xlsx = pd.ExcelFile('Зарядные_станции_для_электромобилей.xlsx')
# xlsx.sheet_names
df1 = pd.read_excel(xlsx, sheet_name='0', header=1)
df2 = pd.read_excel(xlsx, sheet_name='1', header=10)
df3 = pd.concat([df1, df2], ignore_index=True)
df3['Район'].value_counts().nlargest(3)
