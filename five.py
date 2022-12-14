import pandas as pd

'''Возвращаемся к выгрузке про пользователей из социальной сети. 
Снова загрузите ее в датафрейм, оставьте только столбцы username, name, sex и сохраните в формате json (кодировка utf8).
Сохранение выполните таким образом чтобы ключами были названия колонок, а значениями вложенные словари, которые будут хранить лейбл строки и само значение:
'''

df = pd.read_csv('users.csv', sep=';')
df = df[['username', 'name', 'sex']]
df.to_json('out_2.json')

# NEW RESULT
# pd.read_csv(url, sep=';', usecols=['username', 'name', 'sex']).to_json('json_example.json', orient='columns')

# ONE MORE
# pd.read_csv('users.csv', sep=';', usecols=['username', 'name', 'sex']).to_json('users.json')


# print(df.keys())
