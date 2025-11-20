import pandas as pd 

df = pd.read_csv('./Customer-Churn-Records.csv')

count_exited = df['Exited'].value_counts(normalize=True).multiply(100).round(2)

# make pivot table find balance exited customers based on geography

balance_churn_pivot = df.pivot_table(
    values="Balance",
    index="Exited",
    aggfunc='mean'
)

# NumberOfProducts exited customers count average
Product_churn_rate = df.groupby('NumOfProducts')['Exited'].mean().mul(100).round(2)

age_bins = pd.cut(df['Age'], bins=4)

age_churn_rate = df.groupby(age_bins)['Exited'].mean().mul(100).round(2)
print("Churn Rate by Age Groups:",age_churn_rate)