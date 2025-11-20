import pandas as pd 

df = pd.read_csv('./Customer-Churn-Records.csv')

count_exited = df['Exited'].value_counts(normalize=True).multiply(100).round(2)

