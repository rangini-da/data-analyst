#1. Program to retrieve data from CSV files for the first 9 rows 
data = np.genfromtxt('Sales.csv', delimiter=',', skip_header=1)
print(data[:9])

#2. Program to generate Row and Column numbers 
import numpy as np 
data = np.genfromtxt('Sales.csv', delimiter=',', skip_header=1) 
rows, columns = data.shape 
print(f"Number of rows: {rows}") 
print(f"Number of columns: {columns}") 

#3. Program to Find Min, Max, Mean and Standard Deviation of the data 
import numpy as np 
data = np.genfromtxt('Sales.csv', delimiter=',', skip_header=1) 
min_values = np.min(data, axis=0) 
max_values = np.max(data, axis=0) 
mean_values = np.mean(data, axis=0) 
std_dev_values = np.std(data, axis=0) 
print("Minimum values for each column:", min_values) 
print("Maximum values for each column:", max_values) 
print("Mean values for each column:", mean_values) 

#4. Program to find unique values and the count 
import numpy as np 
data = np.genfromtxt('Sales.csv', delimiter=',', dtype=str, skip_header=1) 
item_type_column = data[:, 5] 
unique_values, counts = np.unique(item_type_column, return_counts = True) 
print("Unique values in 'Item_Type':", unique_values) 
print("Counts for each unique value:", counts)

#5. Program to Filter and display a specific data 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
low_fat_data = data[data['Item_Fat_Content'] == 'Low Fat'] 
low_fat_array = low_fat_data.to_numpy() 
print(low_fat_array)

#6. Program to extract data from specific column or columns 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
item_mrp = data['Item_MRP'].to_numpy() 
item_outlet_sales = data['Item_Outlet_Sales'].to_numpy() 
print("Item MRP:", item_mrp) 
print("Item Outlet Sales:", item_outlet_sales)

#7. Program to find maximum, minimum and the difference 
import pandas as pd 
import numpy as np 
data = pd.read_csv('sales.csv') 
item_weights = data['Item_Weight'] 
max_weight = np.max(item_weights) 
min_weight = np.min(item_weights) 
print(f"Maximum Weight is: {max_weight}") 
print(f"Minimum Weight is: {min_weight}") 
weight_difference = max_weight - min_weight 
print(f"The difference between the maximum and minimum item weights is:{weight_difference}")

#8. Program to find sales in each Outlet type 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
outlet_types = data['Outlet_Type'].values 
item_sales = data['Item_Outlet_Sales'].values 
outlet_sales_count = {} 
for outlet, sales in zip(outlet_types, item_sales): 
if outlet in outlet_sales_count: 
outlet_sales_count[outlet] += 1 
else: 
outlet_sales_count[outlet] = 1 
outlet_sales_array = np.array(list(outlet_sales_count.items())) 
print("Count of Items Sold in Each Outlet Type:") 
print(outlet_sales_array) 

#9. Program to find the highest and lowest Item 
outlet sales 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
sales_data = data['Item_Outlet_Sales'].to_numpy() 
highest_sales_index = np.argmax(sales_data) 
lowest_sales_index = np.argmin(sales_data) 
highest_sales_item = data.iloc[highest_sales_index] 
lowest_sales_item = data.iloc[lowest_sales_index] 
print("Item with the highest sales:") 
print(highest_sales_item) 
print("\nItem with the lowest sales:") 
print(lowest_sales_item)

#10. Program to find if any column has missing values 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
data_numeric = data.apply(pd.to_numeric, errors='coerce') 
data_array = data_numeric.to_numpy() 
missing_values = np.isnan(data_array).any(axis=0) 
for i, has_missing in enumerate(missing_values): 
column_name = data.columns[i] 
if has_missing: 
print(f"The column '{column_name}' has missing values.") 
else: 
print(f"The column '{column_name}' has no missing values.")

#11. Program to find the total sales amount in the dataset 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
sales_data = data['Item_Outlet_Sales'].to_numpy() 
total_sales = np.sum(sales_data) 
print(f'Total Sales Amount: {total_sales}')

#12. Program to find the rows with missing values in Item weight 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
missing_values_count = np.sum(data['Item_Weight'].isnull()) 
print(f'Number of rows with missing values in Item_Weight: {missing_values_count}')

#13. Program to find the average sales amount 
for each outlet 
import pandas as pd 
import numpy as np 
data = pd.read_csv('salesa.csv') 
average_sales= data.groupby('Outlet_Identifier') 
['Item_Outlet_Sales'].mean().reset_index() 
print(average_sales) 

#14. Program to find the top 5 outlets with the highest total sales 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
total_sales = data.groupby('Outlet_Identifier') 
['Item_Outlet_Sales'].sum().to_numpy() 
top_outlets_indices = np.argsort(total_sales)[-5:][::-1] 
print("Top 5 Outlets with Highest Total Sales:") 
for outlet in top_outlets: 
print(outlet) 
top_outlets = data['Outlet_Identifier'].unique()[top_outlets_indices]

#15. Program to Analyse sales growth over the years 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
years = data['Outlet_Establishment_Year'].unique() 
sales_growth = {} 
for year in years: 
total_sales = data[data['Outlet_Establishment_Year'] == 
year]['Item_Outlet_Sales'].sum() 
sales_growth[year] = total_sales 
years_array = np.array(list(sales_growth.keys())) 
sales_array = np.array(list(sales_growth.values())) 
print("Yearly Sales Growth:") 
for year, sales in sales_growth.items(): 
print(f"Year: {year}, Total Sales: {sales}")
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 

#16. Program to find the total sales amount 
total_sales = data.groupby('Outlet_Location_Type')['Item_Outlet_Sales'].sum(). to_numpy() 
print("Total Sales by Outlet Location Type:") 
for location, sales in zip(data['Outlet_Location_Type'].unique(), total_sales): 
print(f"{location}: {sales}") 

#17. Program to create Chart of total sales amount 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv('sales.csv') 
total_sales = data.groupby('Outlet_Location_Type') ['Item_Outlet_Sales'].sum() 
total_sales_array = total_sales.to_numpy() 
plt.bar(total_sales.index, total_sales_array, color='skyblue') 
plt.xlabel('Outlet Location Type') 
plt.ylabel('Total Sales') 
plt.title('Total Sales by Outlet Location Type') 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show()

#18. Program to Analyze the total sales in outlet types 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
total_sales_by_outlet = data.groupby('Outlet_Type') 
['Item_Outlet_Sales'].sum().to_numpy() 
outlet_types = data['Outlet_Type'].unique() 
for outlet, sales in zip(outlet_types, total_sales_by_outlet): 
print(f'Total sales for {outlet}: ${sales:.2f}') 
print("Standard deviation for each column:", std_dev_values)

#19. Program to find how Item Visibility affects Item Outlet Sales with chart 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv('Sales.csv') 
bins = np.linspace(0, data['Item_Visibility'].max(), num=5) 
data['Visibility_Bin'] = np.digitize(data['Item_Visibility'], bins) 
average_sales = data.groupby('Visibility_Bin') ['Item_Outlet_Sales'] .mean() 
plt.figure(figsize=(10, 6)) 
average_sales.plot(kind='bar', color='skyblue') 
plt.title('Average Item Outlet Sales by Item Visibility Bins') 
plt.xlabel('Item Visibility Bins') 
plt.ylabel('Average Item Outlet Sales') 
plt.xticks(ticks=np.arange(len(average_sales)), labels=[f'Bin {i}' for i in 
range(1, len(average_sales) + 1)], rotation=0) 
plt.show()

#20. Program to find total sales for each Item type Unique method 
import numpy as np 
data = np.genfromtxt('Sales.csv', delimiter=',', dtype=None, encoding='utf-8', 
names=True) 
item_types = data['Item_Type'] sales = data['Item_Outlet_Sales'] 
unique_item_types = np.unique(item_types) 
total_sales = {item_type: np.sum(sales[item_types == item_type]) for 
item_type in unique_item_types} 
print(total_sales)

#20. Program to find Minimum, Maximum, Mean and StdDev 
import pandas as pd 
df = pd.read_csv('Sales1.csv') 
min_values = df.min() 
max_values = df.max() 
mean_values = df.mean() 
std_dev_values = df.std() 
print("Minimum values:\n", min_values) 
print("\nMaximum values:\n", max_values) 
print("\nMean values:\n", mean_values) 
print("\nStandard Deviation values:\n", std_dev_values)

#21. Program to find Count of Low Fat 
import pandas as pd 
df = pd.read_csv('Sales.csv') 
low_fat_items = df[df['Item_Fat_Content'] == 'Low Fat'] 
print(low_fat_items)

#22. Program to find data from selected columns 
import pandas as pd 
df = pd.read_csv('Sales.csv') 
selected_columns = df[['Item_MRP', 'Item_Outlet_Sales']] 
print(selected_columns)

#23. Program to Sort data by Item outlet sale column 
import pandas as pd  
df = pd.read_csv('sales.csv')  
sorted_df = df.sort_values(by='Item_Outlet_Sales', ascending=False)  
print(sorted_df.head()) 

#24. Program to find unique values in Outlet type column 
import pandas as pd  
df = pd.read_csv('sales.csv')  
unique_outlet_types = df['Outlet_Type'].unique()  
print(unique_outlet_types) 

#25. Program to create a new column 
import pandas as pd  
df = pd.read_csv('sales.csv')  
df['Price_per_Weight'] = df['Item_MRP'] / df['Item_Weight']  
max_value = df['Price_per_Weight'].max()  
min_value = df['Price_per_Weight'].min()  {min_value}") 
print(f"Max Price per Weight: {max_value}, Min Price per Weight:
       
#26. Program to create a new column of sales above average 
import pandas as pd  
df = pd.read_csv('sales.csv')  
average_sales = df['Item_Outlet_Sales'].mean()  
df['High_Sales'] = df['Item_Outlet_Sales'] > average_sales  
print(df.head())

#27. Program to create a chart 
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('sales.csv')  
df['Item_Outlet_Sales'].head(50).plot(kind='line')  
plt.title('Sales for First 50 Rows')  
plt.xlabel('Index')  
plt.ylabel('Sales')  
plt.show()

#28. Program to find Average of Item outlet type 
import pandas as pd 
df = pd.read_csv('sales.csv')  
avg_sales_per_outlet = df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()  
print(avg_sales_per_outlet)

#30. Program to write a custom function 
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('sales.csv') 
def categorize_sales(Item_Outlet_sales): 
if Item_Outlet_sales < 500: 
return 'Low' 
elif 500 <= Item_Outlet_sales < 1500: 
return 'Medium' 
else: 
return 'High'  
df['Sales_Category'] = df['Item_Outlet_Sales'].apply(categorize_sales)  
print(df.head())


numpy pandas matplotlib