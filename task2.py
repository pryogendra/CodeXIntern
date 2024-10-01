import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(df):
    sns.set(style="whitegrid")

    # 1. Bar Chart
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='DEPARTMENT_NAME')
    plt.title('Count of Departments')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 2. Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='DEPARTMENT_ID', y='Salary')
    plt.title('Scatter Plot of Salary by Department ID')
    plt.xlabel('Department ID')
    plt.ylabel('Salary')
    plt.tight_layout()
    plt.show()

    # 3. Heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()


def create_simple_heatmap(df):
    plt.figure(figsize=(8, 6))

    # Calculate the correlation matrix
    correlation_matrix = df.corr()

    # Create the heatmap
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Simple Correlation Heatmap')
    plt.tight_layout()
    plt.show()


def main():
    df = pd.read_csv("departments.csv")
    print("Data Preview:")
    print(df.head())

    visualize_data(df)

    create_simple_heatmap(df)


if __name__ == '__main__':
    main()
