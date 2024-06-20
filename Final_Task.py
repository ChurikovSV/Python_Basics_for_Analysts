# Условие 1: Задача 1
# Постройте график
# Назовите график
# Сделайте именование оси x и оси y
# Сделайте выводы

# 1.1. Скачать следующие данные: kc-house-data и laptop_price

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.float_format = '{:20,.2f}'.format
df = pd.read_csv('kc_house_data.csv')
print(df)

# 1.2 Изучите стоимости недвижимости
plt.figure(figsize = (6,4))
plt.hist(df['price'], bins = 10)
plt.xlabel('Стоимость')
plt.ylabel('Количество')
plt.title('Стоимость недвижимости')

plt.figure(figsize=(6,8))

plt.hist(df['price'], bins=100)
plt.title('Стоимость недвижимости')
plt.xlabel('Цена')
plt.ylabel('Количество')

# 1.3 Изучите распределение квадратуры жилой
plt.figure(figsize = (6,4))
sns.histplot(df['sqft_living'], bins = 10)
plt.xlabel('Жилые квадратные метры')
plt.ylabel('Количество')
plt.title('Распределение жилой квадратуры')

plt.figure(figsize = (6,4))
sns.histplot(df['sqft_living'], bins = 100)
plt.xlabel('Жилые квадратные метры')
plt.ylabel('Количество')
plt.title('Распределение жилой квадратуры')

data_yr = df['yr_built'].value_counts(ascending=True)
print(data_yr.head())

# 1.4 Изучите распределение года постройки
years_list = [1900+i*10 for i in range (0,13)]

names = data_yr.index
values = data_yr.values
yr_list = list(range(1900, 2025, 5))
plt.figure(figsize=(16, 6))
plt.bar(names, values, width=0.7, facecolor='c', alpha=0.75)
plt.title('Годы постройки домов')
plt.xlabel('Годы')
plt.ylabel('Количество домов')
plt.grid(True)
plt.xticks(yr_list, rotation=40);
plt.show()

plt.figure(figsize=(16, 6))
sns.set_style("darkgrid")
sns.lineplot(data=data_yr, x=names, y=values)
plt.xlabel('Годы')
plt.ylabel('Количество домов')
plt.xticks(ticks=years_list)

# 2.1 Изучите распределение домов от наличия вида на набережную
data_view = df['waterfront'].value_counts()
val = data_view.values
plt.pie(val,labels=['seaview', 'w/o seaviews'],explode=[0,0.3],
        radius = 1.5, startangle=60,
        labeldistance=1.2, autopct='%.1f%%')