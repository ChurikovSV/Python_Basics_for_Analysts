# Составьте несколько сводных таблиц.
# Данные находятся в файле kc_house_data.csv.
#     среднюю стоимость домов в зависимости от количества спален и сохраните в avg.
#     Отсортируйте от меньшей стоимости к большей.
#     Найдите минимальную min, среднюю mean и максимальную max стоимости домов в зависимости от состояния дома и сохраните в price.
#     Постройте таблицу с подсчетом количества домов в данных в зависимости от вида на набережную waterfront и оценкой вида view и сохраните ее в view_waterfront.
#     Каких домов в зависимости от этажности и количества спален больше? Постройте эту таблицу, содержащую в себе информацию о спальнях и этажности, и сохраните ее в bedrooms_floors.
#     Постройте таблицу с подсчетом медианной стоимости домов в данных в зависимости от состояния дома и оценки дома и сохраните в 'median_price'.

import pandas as pd
import numpy as np

df = pd.read_csv("kc_house_data.csv")
avg = df.pivot_table(index='bedrooms', values='price', aggfunc='mean').sort_values(by='price')
price = df.groupby('condition').agg({'price': ['min', 'mean', 'max']})
print(price)
view_waterfront = df.pivot_table(index='waterfront', columns='view', values='id', aggfunc='count', fill_value=0)
bedrooms_floors = df.pivot_table(index='floors', columns='bedrooms', values='id', aggfunc='count', fill_value=0)
median_price = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)