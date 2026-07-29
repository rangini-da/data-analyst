#1. Program to retrieve data from CSV files for the first 9 rows
import numpy as np 
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
print("Standard deviation for each column:", std_dev_values)

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

#6. Program to find maximum, minimum and the 
difference 
import pandas as pd 
import numpy as np 
data = pd.read_csv('sales.csv') 
item_weights = data['Item_Weight'] 
max_weight = np.max(item_weights) 
min_weight = np.min(item_weights) 
weight_difference = max_weight - min_weight 
print(f"Maximum Weight is: {max_weight}") 
print(f"Minimum Weight is: {min_weight}") 
print(f"The difference between the maximum and minimum item weights is: {weight_difference}")

#7. Program to find sales in each Outlet type 
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
#8. Program to find the top 5 outlets with the 
highest total sales 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
total_sales = data.groupby('Outlet_Identifier') 
['Item_Outlet_Sales'].sum().to_numpy() 
top_outlets_indices = np.argsort(total_sales)[-5:][::-1] 
top_outlets = data['Outlet_Identifier'].unique()[top_outlets_indices]
print("Top 5 Outlets with Highest Total Sales:") 
for outlet in top_outlets: 
  print(outlet)
       
#9. Program to Analyze the total sales in outlet 
types with chart 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv('sales.csv') 
total_sales_by_outlet = 
data.groupby('Outlet_Type')['Item_Outlet_Sales'].sum() 
plt.figure(figsize=(10, 6)) 
total_sales_by_outlet.plot(kind='bar', color='green') 
plt.title('Total Sales by Outlet Type') 
plt.xlabel('Outlet Type') 
plt.ylabel('Total Sales ($)') 
plt.xticks(rotation=45) 
plt.grid(axis='y') 
plt.tight_layout()  
plt.show()

#10. Program to find item type with highest total sales 
import numpy as np 
import pandas as pd 
data = pd.read_csv('sales.csv') 
total_sales = data.groupby('Item_Type')['Item_Outlet_Sales'].sum() 
highest_sales_item_type = total_sales.idxmax() 
highest_sales_value = total_sales.max() 
print(f'The item type with the highest total sales is: {highest_sales_item_type} with sales of {highest_sales_value}') 

numpy pandas matplotlib
