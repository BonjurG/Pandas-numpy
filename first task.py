import pandas as pd

'''Для вас подготовили выгрузку пользователей в формате csv.
Загрузите файл в датафрейм и оставьте только пользователей женского пола. 
Сохраните датафрейм в формате csv без индекса и в кодировке utf8. 
Оставьте только две колонки: username и mail 
Разделитель значений: точка с запятой.'''

df = pd.read_csv('users.csv', sep=';')
df_girl = df[df['sex'] == 'F']
df_girl.to_csv('users_deal.csv', sep=';', columns=['username', 'mail'], index=False, encoding='utf-8')
