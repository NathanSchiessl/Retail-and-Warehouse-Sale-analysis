import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"cleaned_retail_sales_data.csv")

print(df.head(15))

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='MONTH', y='RETAIL SALES', hue='ITEM TYPE')
plt.title('Monthly Retail Sales by Item Type')
plt.savefig('visualizations/sales_trends.png')
plt.show()



top_suppliers = df.groupby('SUPPLIER')['RETAIL SALES'].sum().nlargest(40).index
df_top = df[df['SUPPLIER'].isin(top_suppliers)]

plt.figure(figsize=(14, 8))
sns.barplot(x='SUPPLIER', y='RETAIL SALES', data=df_top, palette='Blues_d')
plt.title('Top 20 Suppliers by Total Retail Sales', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=8) 
plt.tight_layout()

plt.savefig('Visualizations/top_suppliers_sales.png')
plt.show()


df.describe().to_csv('visualizations/summary_statistics.csv')

print("\nData analysis complete. Visualizations saved.")