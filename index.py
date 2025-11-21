import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('./Customer-Churn-Records.csv')

count_exited = df['Exited'].value_counts(normalize=True).multiply(100).round(2)

balance_churn_pivot = df.pivot_table(
    values="Balance",
    index="Exited",
    aggfunc='mean'
)

Product_churn_rate = df.groupby('NumOfProducts')['Exited'].mean().mul(100).round(2)

age_bins = pd.cut(df['Age'], bins=4)

age_churn_rate = df.groupby(age_bins)['Exited'].mean().mul(100).round(2)
# print(age_churn_rate)
satisfaction_pivot = df.pivot_table(
    values="Satisfaction Score",
    index="Exited",
    aggfunc='mean'
)

products_churn_rate_df = df.groupby('NumOfProducts')['Exited'].mean().mul(100).round(2).reset_index()

# plt.figure(figsize=(8, 5))

# sns.barplot(
#     x='NumOfProducts',
#     y='Exited',
#     data=products_churn_rate_df,
#     palette=['green', 'blue', 'red', 'darkred']
# )

# plt.title('Operational Risk: Churn Rate by Number of Products', fontsize=14)
# plt.ylabel('Churn Rate (%)', fontsize=12)
# plt.xlabel('Number of Products Held by Customer', fontsize=12)
# plt.yticks(np.arange(0, 101, 20))
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.show()

High_risk_customers = df[
    (df['Balance']>100000) & (df['Satisfaction Score']<=2)
] 

risk_churn_rate = (High_risk_customers['Exited'].mean()*100).round(2)

satisfaction_balance_pivot = df.pivot_table(
    index = 'Balance',
    values = 'Satisfaction Score',
    aggfunc='mean'
)

# satisfaction_percentage = df['Satisfaction Score'].value_counts(normalize=True).mul(100).round(2)
satisfaction_percentage = df['Satisfaction Score'].value_counts()

name_with_country = df[['Surname','Geography']]
sorted_name_with_country = name_with_country.sort_values(by='Surname',ascending=True)

# customer who earn points maximum

customer_earns_max_points  = df.groupby('Surname')['Point Earned'].value_counts()
# print(customer_earns_max_points/)

# selected columns

target = 'Hill'
selected_columns = df[['Surname','Balance','Exited']]

# find target column how?


target_cus = df[df['Surname']== target]
selected_columns = ['Surname','Balance','Exited']
specific_columns = target_cus[selected_columns]

# sum_bal = specific_columns['Balance'].sum().round(2)
sum_bal = specific_columns[specific_columns['Balance']>150000].loc[899]

pd.options.display.float_format = 'Rs {:,.2f}'.format

# finder geography balance
geography_balance = df.pivot_table(
    index='Geography',
    values='Balance',
    columns='Gender',
    aggfunc='sum',
    margins=True
).round(2)

print(geography_balance)