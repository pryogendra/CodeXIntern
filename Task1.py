import pandas as pd

df = pd.read_csv('departments.csv')  # read CSV file
print("Data Preview:")
print(df.head())

column_name = 'Salary'

# Basic statistical analysis
average_value = df[column_name].mean()
min_value = df[column_name].min()
max_value = df[column_name].max()
median_value = df[column_name].median()
std_dev = df[column_name].std()

print(f'\nStatistics for {column_name}:')
print(f'Average: {average_value}')
print(f'Minimum: {min_value}')
print(f'Maximum: {max_value}')
print(f'Median: {median_value}')
print(f'Standard Deviation: {std_dev}')

summary_stats = df[column_name].describe()
print(f'\nSummary Statistics:\n{summary_stats}')
