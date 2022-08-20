import pandas as pd

'''Загрузите файл XML в датафрейм и посчитайте сколько пользователей женского пола с группой крови B+ в выгрузке. '''

df = pd.read_xml('users.xml')  # загружаем html-файл
df.loc[(df['sex'] == 'F') & (df['blood_group'] == 'B+'), 'name'].count()
