# Данные находятся в файле kc_house_data.csv.
# Считать данные с помощью pandas.
# Вывести на экран первые 5 строк.
# Создать новый признак price_per_sq_lot, который будет содержать avg = среднюю стоимость за один кв. метр общей площади.
# Создать новый признак delta_renovated, который будет содержать разницу в годах между годом реновации дома и годом постройки дома и сохраните в renv. Если реновации дома не было, то в новом признаке поставьте 0.
# Создайте признаки года продажи, месяца продажи и сохраните в year_ch, month_ch.
# Удалите признаки date, zipcode, lat, long и сохраните в new.

import pandas as pd
import numpy as np


hd = pd.read_csv("kc_house_data.csv")
stroki = hd.head()
avg = hd['price_per_sq_lot'] = hd['price'] / hd['sqft_lot']
hd["delta_renovared"] = np.where(hd["yr_renovated"]==0,hd["yr_renovated"], hd["yr_renovated"] - hd["yr_built"])
renv = hd["delta_renovared"]
year_ch = hd["date"].astype("datetime64[ns]").dt.year.astype("int64")
month_ch = hd["date"].astype("datetime64[ns]").dt.month.astype("int64")
new = hd.drop(columns=['date','zipcode', 'lat', 'long'], inplace=True)