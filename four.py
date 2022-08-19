import pandas as pd

"""Загрузите данные в датафрейм и определите самый дешевый тариф."""

df = pd.read_json('data-399-2022-07-01.json', encoding="windows-1251")
print(df.NameOfTariff[df.TicketCost == df.TicketCost.min()])
