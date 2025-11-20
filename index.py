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

satisfaction_pivot = df.pivot_table(
    values="Satisfaction Score",
    index="Exited",
    aggfunc='mean'
)

products_churn_rate_df = df.groupby('NumOfProducts')['Exited'].mean().mul(100).round(2).reset_index()

plt.figure(figsize=(8, 5))

sns.barplot(
    x='NumOfProducts',
    y='Exited',
    data=products_churn_rate_df,
    palette=['green', 'blue', 'red', 'darkred']
)

plt.title('Operational Risk: Churn Rate by Number of Products', fontsize=14)
plt.ylabel('Churn Rate (%)', fontsize=12)
plt.xlabel('Number of Products Held by Customer', fontsize=12)
plt.yticks(np.arange(0, 101, 20))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()