import pandas as pd

df = pd.read_csv('laptops.csv', sep=';')
#print(df.isnull().sum().sum())
#print(df.isnull().sum())
#print(df.describe(include=['object']))
# print(df.head(10))
#print(df['Company'].value_counts())
# print(df['Price_euros'].min())
# print(df['Price_euros'].max())
#print(df.sort_values('Price_euros', ascending=False).head(1))

#print(df.sort_values('Price_euros', ascending=False).iloc[0])

#print(df[df['Inches'] == df['Inches'].min()][['Company', 'TypeName', 'Inches']])
# print(df[df['Company']=='HP']['Price_euros'].max())
#
# print(df.shape)
#
# print(df.info())
#
# print(df.describe())

# print(df.describe(include=['object']))
#
# print(df.dtypes)

# print(df['Company'].unique())

# print(df['Company'].value_counts(normalize=True))

print(df.isna().sum())