# import array as arr

# def display_ave(): 
#     print("Average purchased items:")

# def get_ave(): 
#     n = len(items) 
#     get_sum = sum(items) 
#     mean = get_sum / n 
#     m = str(mean) 
#     print (m)

# online_pur= [19, 27, 17, 24,16]

# sample_data= arr.array("i", online_pur) 
# items = sample_data[2:5] 
# sample_data_list = items.tolist()

# display_ave() 
# get_ave()

# import pandas as pd

# items = pd.Series(['a', 'b', 'c', 'd'], index=['index 01', 'index 02', 'index 03', 'index 04']) # if no index it will give the default value 0 to so on.
# print(items)

# # dataframe
# dframe_name = {'Name': ['Ben','Tom', 'Jerry'],
# 'Section': ['A', 'B', 'C']}

# student = pd.DataFrame(dframe_name)
# print(student)
# name = pd.read_csv("Marketing.csv")
# print(name.info())        
# print(name.shape)       # no. of rows and columns
# print(name.head(3))
# print(name.tail(3))

# import pandas as pd

# list_1author = ['E.L. James','Suzanne Collins', 'J.K. Rowling', 'Dan Brown']
# list_2reviews = [410, 211, 314, 178]

# list001 = pd.Series(list_1author)
# list002 = pd.Series(list_2reviews)

# print(list001)
# print(list002)

# combime_series = {'Authors Name': list_1author, 'Review': list_2reviews}
# dframe_combineSeries = pd.DataFrame(combime_series)
# print(dframe_combineSeries)


# import pandas as pd

# bestsellers_dframe = pd.read_csv("bestsellers.csv")
# print(bestsellers_dframe.head())
# print(bestsellers_dframe.shape)
# print(bestsellers_dframe.info())
# print(bestsellers_dframe.isnull().sum())
# print(bestsellers_dframe[bestsellers_dframe['Year'].isna()])

# bestsellers_dframe = bestsellers_dframe.dropna()
# print(bestsellers_dframe.isnull().sum())
# print(bestsellers_dframe.info())

# print(bestsellers_dframe.describe())
# print(bestsellers_dframe['Price'].describe())
# print(bestsellers_dframe[bestsellers_dframe['Year'] == 2015])
# print(bestsellers_dframe[(bestsellers_dframe['Year'] == 2016) & (bestsellers_dframe['Genre'] == 'Non Fiction')])

# bestsellers_dframe = bestsellers_dframe.sort_values(by='Year', ascending=False)
# print(bestsellers_dframe.head())\


# print(bestsellers_dframe.groupby('Year')['Price'].sum())
# print(bestsellers_dframe.groupby('Price', as_index = False).agg({'Year':'sum'}))
# print(bestsellers_dframe[['Author', 'Reviews', 'User Rating']].head())

# import pandas as pd
# import matplotlib.pyplot as plt 
# import seaborn as sns

# train = pd.read_csv('train.csv')
# print(train.head())
# print(train.info())
# print(train.isnull().sum())
# print(train[train['Postal Code'].isna()])
# train['Postal Code'] = train['Postal Code'].fillna('05401')
# print(train.info())
# print(train.isnull().sum())
# print(train.head())
# del train['Row ID']
# print(train.head(6))

# # Converting object to datetime

# train['Order Date'] = pd.to_datetime (train[ 'Order Date'], format='%d/%m/%Y') 
# train['Ship Date'] = pd.to_datetime (train[ 'Ship Date'], format='%d/%m/%Y')

# #Converting float to object/string

# train['Postal Code'] = train['Postal Code'].astype(str)

# train.info()


# #Create Order Year column
# train['Order Year']=train['Order Date'].dt.year
# train.info()
# train.head (2)
# train['Order Year'] = train['Order Year'].astype (str) 
# train.info()

# # Sum of Sales by year
# ysales = train.groupby ('Order Year', as_index = False).agg({'Sales':'sum'})
# print(ysales)

# sns.lineplot(x='Order Year', y='Sales', data = ysales, marker="o") 
# plt.xlabel('')
# plt.show ()
                                               
# sales_2018=train[train['Order Year'] == '2018']
# sales_2018.head ()

# product = sales_2018.groupby ('Product Name', as_index = False).agg ({'Sales':'sum'})
# p=sales_2018.sort_values(by= 'Sales', ascending = False)
# p. head (10)
                                                                                             
# p_top= p[(p['Sales']>=4416.174)]
# sns.barplot(y="Product Name", x="Sales", data=p_top,
# ci=False,orient='h',color='grey')
# plt.title('Top Products in 2018')
# plt.ylabel ('')
# plt.show ()

# p_top= p[(p['Sales']>=4416.174)]
# sns.barplot(y="Product Name", x="Sales", data=p_top, orient='h', color='grey')
# plt.title('Top Products in 2018')
# plt.ylabel ('')
# plt.show ()

# psales = sales_2018.groupby ('Category', as_index = False).agg ({'Sales':'sum'})
# psales

# sns.barplot(x="Category", y="Sales", data=psales, palette= 'Blues')
# plt.title('Sales by Product Category')
# plt.xlabel('')
# plt.ylabel('')

# plt.show ()

# cons_segment = train[train['Segment'] == 'Consumer']
# consumer = cons_segment.groupby ('Order Year', as_index = False).agg({'Sales':'sum'})
# print(consumer)

# home_segment = train[train['Segment'] == 'Home Office']
# home=home_segment.groupby ('Order Year', as_index =  False).agg ({'Sales':'sum'})
# print(home)

# corp_segment = train[train['Segment'] == 'Corporate'] 
# corporate=corp_segment.groupby('0rder Year', as_index = False).agg({'Sales':'sum'})

# print(corporate)

# sns.lineplot(x='Order Year', y='Sales', data = consumer, marker="o")
# sns.lineplot(x='Order Year', y='Sales', data = home, marker="o")
# sns.lineplot(x='Order Year', y='Sales', data = corporate, marker="o")
# plt.legend (['consumer', 'home','corporate'], fontsize=8)
# plt.show ()
