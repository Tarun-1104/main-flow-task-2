import os
import pandas as pd

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Step 1: Reading CSV Files
df = pd.read_csv("C:\\Users\\Tarun poopathi\\OneDrive\\Desktop\\data.csv")  # Update with the correct path
print("Data Frame Head:\n", df.head())

# Step 2: Handling Missing Values
print("\nMissing Values:\n", df.isnull().sum())
df['column1'] = df['column1'].fillna(df['column1'].mean())
df_cleaned = df.dropna()

# Removing Duplicates
df_no_duplicates = df_cleaned.drop_duplicates()
print("\nData Frame after Cleaning:\n", df_no_duplicates)

# Step 3: Data Manipulation
# Filtering Data
filtered_df = df_no_duplicates[df_no_duplicates['column1'] > 50]
print("\nFiltered Data Frame:\n", filtered_df)

# Sorting Data
sorted_df = filtered_df.sort_values(by='column1')
print("\nSorted Data Frame:\n", sorted_df)

# Grouping Data
grouped_df = sorted_df.groupby('column1').mean()
print("\nGrouped Data Frame:\n", grouped_df)
