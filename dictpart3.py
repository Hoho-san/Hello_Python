import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set() # sea born default them and color palette

sales = pd.read_csv("all_sales.csv") # all_sales.csv is now data frame "sales"
print(sales.info())
print(sales.head(7))
print(sales.isnull().sum()) # to check total numbers of blank rows
sales = sales.dropna() # to remove all blanks using dropna() method
print(sales.info())
print(sales.isnull().sum()) 

sales['Month'] = sales['Order Date'].str[0:2] # to create month column from the order date column
print(sales.head ())

# sales['Month'] = sales['Month'].astype('int32') # to convert data type of month column from object to integer, it has an value error 'Or'
Or_dump = sales[sales['Month'] =="Or"]
print(Or_dump.head())

sales = sales[sales['Month'] != 'Or'] # Remove "Or's" from the Month Column

Or_dump = sales[sales['Month'] =="Or"] # Create Or_dump dataframe to check the "Or's" in the Month Column
print(Or_dump.head())

sales['Month'] = sales['Month'].astype('int32') # to convert data type of month column from object to integer

sales.info()
sales.head()

# Convert Quantity Ordered and Price Each columns to the correct data type
sales['Quantity Ordered'] = pd.to_numeric (sales['Quantity Ordered'])
sales['Price Each'] = pd.to_numeric(sales['Price Each']) # to_numeric is to convert to numeric data type(integer or float)
sales.info()

# Add Sales Column
sales['Sales'] = sales['Quantity Ordered']*sales['Price Each'] 
print(sales.head())

print(sales.info())

# to show bar graph
months = range(1,13)
plt.bar(months, sales.groupby(['Month']).sum()['Sales']/1000000)

plt.title("Monthly Sales 2019")
plt.ylabel('Sales in USD ($)')
plt.xlabel('Months')

plt.xticks(months)
# plt.show()


sns.set() # sea born default them and color palette
# to show line graph


fig = plt.figure(figsize= (10,6))

months = range(1,13)
plt.plot(months, sales.groupby(['Month']).sum()['Sales'], color= 'red')

plt.title("Monthly Sales 2019", fontsize = 14, fontweight = 'bold')
plt.ylabel('Sales in USD ($)', fontsize = 12, color = 'blue')
plt.xlabel('Months', fontsize = 12, color = 'green')

plt.xticks(months)

# to remove the edge of the graph called spin
plt.grid(True, color='grey', linestyle=':')
for spine in plt.gca().spines.values(): 
    spine.set_visible(False)

plt.show()

# fig = plt.figure(figsize= (10,6))
# product_group = sales.groupby('Product')
# quantity_ordered = product_group.sum()['Quantity Ordered']
# products = [product for product, df in product_group]
# plt.barh(products, quantity_ordered)
# plt.title("Total Units Sold", fontsize=8)
# plt.ylabel('Products')
# plt.xlabel ('Units sold')
# plt.yticks (products)
# plt.show()

fig = plt.figure(figsize =(12, 8))

product_group = sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

sort_sum = quantity_ordered.sort_values (ascending=True)
sort_sum = pd.DataFrame(sort_sum)
sort_sum = sort_sum.reset_index()

product = sort_sum['Product']
quantity =sort_sum['Quantity Ordered']

plt.barh(product, quantity)

plt.xlabel('Units sold')
plt.yticks(product, size=10)

plt.grid(True,color='grey',linestyle=':')

for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.show()

hphone = sort_sum [sort_sum ["Product"].isin(['Apple Airpods Headphones', 'Bose SoundSport Headphones', 'Wired Headphones'])]
print(hphone)

h_product =  hphone['Product']
h_quantity = hphone ['Quantity Ordered']

plt.bar(h_product, h_quantity)
plt.xticks(h_product, size=8)
plt.show()

phone = sort_sum [sort_sum ["Product"].isin(['Google Phone', 'Vareebadd Phone', 'iPhone'])]
print(hphone)

p_product =  phone['Product']
p_quantity = phone ['Quantity Ordered']

plt.bar(p_product, p_quantity)
plt.xticks(p_product, size=8)
plt.show()

fig = plt.figure(figsize = (12,8))

plt.subplot(1,2,1)  # plot 1
h_product =  hphone['Product']
h_quantity = hphone ['Quantity Ordered']

plt.bar(h_product, h_quantity)
plt.xticks(h_product, size=8)
plt.ylim(0, 22500)

plt.subplot(1,2,2) # plot 2
p_product =  phone['Product']
p_quantity = phone ['Quantity Ordered']

plt.bar(p_product, p_quantity)
plt.xticks(p_product, size=8)
plt.ylim(0, 22500)
plt.show()


sns.set() # sea born default them and color palette

fig, ax = plt.subplots(figsize =(16,9)) 

product_group = sales.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

sort_sum = quantity_ordered.sort_values(ascending=True)
sort_sum = pd.DataFrame(sort_sum)
sort_sum= sort_sum.reset_index()

product = sort_sum['Product']
quantity = sort_sum['Quantity Ordered']

ax.barh(product, quantity)

# Add y values to bars 

for i in ax.patches:
    ax.text(i.get_width()+0.2, i.get_y()+0.5, 
        str(round((i.get_width()), 2)), fontsize = 10 , fontweight = "bold", color="grey")

# Remove x, y Ticks

ax.xaxis.set_ticks_position("none")
ax.yaxis.set_ticks_position("none")

# Add x, y gridlines

ax.grid(b= True, color = "grey", linestyle=":")

#  Add padding/spaces between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10)

# Remove ares spines

for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False)

plt.show()