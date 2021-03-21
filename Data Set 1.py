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



