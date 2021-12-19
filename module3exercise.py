import pandas as pd
companySales = pd.read_csv("supermarket_sales.csv")
print(companySales.head(5))
print(companySales.info())
print(companySales.isnull().sum())

companySales = companySales.dropna()
print(companySales.info())
print(companySales.isnull().sum())

print(companySales.head(5))