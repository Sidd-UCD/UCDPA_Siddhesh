import numpy as np

import pandas as pd

df_1 = pd.read_csv('/Users/siddheshkotian/Documents/Certification Data Analytics/Project Rubric/Data_Set A.csv')

print(df_1)

# Exploring Dataframe(df_1)

print(df_1.head())

print(df_1.info())

print(df_1.shape)

print(df_1.values)

print(df_1.columns)

print(df_1.index)

# Sorting Dataset(df_1)

df_1_sales = df_1.sort_values("Sales")

print(df_1_sales)

print(df_1_sales.head())

df_1_sales_des = df_1.sort_values(["Sales"], ascending=[False])

print(df_1_sales_des)

print(df_1_sales_des.head())

df_1_sales_units_des = df_1.sort_values(["Sales", "Units"], ascending=[False, False])

print(df_1_sales_units_des)

print(df_1_sales_units_des.head())

df_1_location = df_1.sort_values("Location")

print(df_1_location)

# Dropping duplicates

df_1_unique_location = df_1.drop_duplicates(subset="Location")

print(df_1_unique_location)

print(df_1_unique_location.value_counts())

df_1_unique_location_sales = df_1.drop_duplicates(subset=["Location", "Sales"])

print(df_1_unique_location_sales)

print(df_1_unique_location_sales.sort_values("Sales", ascending=False))

print(df_1_unique_location_sales.sort_values("Sales", ascending=False).head())


# Creating List

list1 = ["Restaurant", "Location", "Sales"]

print(df_1[list1].head())

list2 = ["Restaurant", "Location", "Sales"]

print(df_1[list1].head())

list3_sales = ["Sales"]

print(df_1[list3_sales].head())

list4_units = ["Units"]

print(df_1[list4_units].head())

list5 = ["Restaurant", "Location", "Sales", "Units"]

print(df_1[list5])

# converting list into arrays through Numpy

array3 = np.array(df_1[list3_sales])

print(array3)

array4 = np.array(df_1[list4_units])

print(array4)

# maximum and minimum sales value

print(array3.min())

print(array3.max())

print(array3.sum())

# mean and standard deviation

print(array3.mean())

print(array3.std())

# Indexing arrays

array1 = np.array(df_1[list5])

print(array1)

indexing = np.array([0,3])

array1_index = array1[indexing]

print(array1_index)

# Looping

print("starting the loop example")

filter = ["Restaurant", "Sales"]

Sales_restaurant = df_1[filter]

rest_above_avg = []

rest_below_avg = []

for index, row in Sales_restaurant.iterrows():

    if (row["Sales"]) > 34:

        rest_above_avg.append(row["Restaurant"])
    else:
        rest_below_avg.append(row["Restaurant"])

print(rest_above_avg)

print(rest_below_avg)



