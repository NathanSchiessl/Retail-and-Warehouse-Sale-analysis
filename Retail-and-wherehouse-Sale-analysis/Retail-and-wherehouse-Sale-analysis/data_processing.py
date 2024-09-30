import pandas as pd 

df = pd.read_csv(r"Retail and Warehouse Sale.csv")


print(f"\nMissing info: \n{df.info()}")

if df['RETAIL SALES'].isnull().sum() > 0:
    df['RETAIL SALES'] = df['RETAIL SALES'].fillna(0)
    print("Missing values in 'RETAIL SALES' = 0.")
else:
    print("No missing values in 'RETAIL SALES'.")

if df['RETAIL TRANSFERS'].isnull().sum() > 0:
    df['RETAIL TRANSFERS'] = df['RETAIL TRANSFERS'].fillna(0)
    print("Missing values in 'RETAIL TRANSFERS' = 0.")
else:
    print("No missing values in 'RETAIL TRANSFERS'.")

if df['WAREHOUSE SALES'].isnull().sum() > 0:
    df['WAREHOUSE SALES'] = df['WAREHOUSE SALES'].fillna(0)
    print("Missing values in 'WAREHOUSE SALES' = 0.")
else:
    print("No missing values in 'WAREHOUSE SALES'.")

print("\nUpdated missing info: \n", df.isnull().sum())

df.to_csv(r"cleaned_retail_sales_data.csv", index=False)
print("\nData preprocessing complete. Cleaned data saved to 'cleaned_retail_sales_data.csv'.")