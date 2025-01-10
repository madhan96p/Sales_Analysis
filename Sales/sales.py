import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Loads sales data from a specified file path."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def clean_data(data):
    """Cleans the dataset by handling missing or incorrect values."""
    print("Initial Data Info:")
    print(data.info())

    print("\nMissing Values:")
    print(data.isna().sum())

    data = data.dropna()
    
    data['Sales'] = (data['Sales'] - data['Sales'].min()) / (data['Sales'].max() - data['Sales'].min())
    data['Unit'] = (data['Unit'] - data['Unit'].min()) / (data['Unit'].max() - data['Unit'].min())

    print("\nData after cleaning:")
    print(data.info())
    return data

def descriptive_statistics(data):
    """Performs descriptive statistics on Sales and Unit columns."""
    print("\nDescriptive Statistics:")
    print(data[['Sales', 'Unit']].describe())

    for column in ['Sales', 'Unit']:
        print(f"\nColumn: {column}")
        print(f"Mean: {data[column].mean()}")
        print(f"Median: {data[column].median()}")
        print(f"Mode: {data[column].mode()[0]}")
        print(f"Standard Deviation: {data[column].std()}")

def analyze_by_group(data, group_column, value_column):
    """Analyzes sales or units by a specific group column."""
    group_analysis = data.groupby(group_column)[value_column].sum().sort_values(ascending=False)
    print(f"\nAnalysis by {group_column}:")
    print(group_analysis)
    return group_analysis

def create_visualizations(data):
    """Creates visualizations for state-wise and group-wise sales analysis."""
    state_sales = data.groupby("State")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=state_sales.index, y=state_sales.values, palette="viridis")
    plt.title("State-wise Sales Analysis")
    plt.xlabel("State")
    plt.ylabel("Total Sales (Normalized)")
    plt.show()

    group_sales = data.groupby("Group")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=group_sales.index, y=group_sales.values, palette="muted")
    plt.title("Group-wise Sales Analysis")
    plt.xlabel("Group")
    plt.ylabel("Total Sales (Normalized)")
    plt.show()

    time_sales = data.groupby("Time")["Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=time_sales.index, y=time_sales.values, palette="coolwarm")
    plt.title("Time-of-Day Sales Analysis")
    plt.xlabel("Time of Day")
    plt.ylabel("Total Sales (Normalized)")
    plt.show()

if __name__ == "__main__":
    file_path = "Sales_Data.csv"
    sales_data = load_data(file_path)

    if sales_data is not None:
        cleaned_data = clean_data(sales_data)

        descriptive_statistics(cleaned_data)

        state_sales = analyze_by_group(cleaned_data, group_column="State", value_column="Sales")

        group_sales = analyze_by_group(cleaned_data, group_column="Group", value_column="Sales")

        create_visualizations(cleaned_data)
