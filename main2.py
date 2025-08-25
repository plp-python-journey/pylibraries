import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Load the dataset
csv_path = 'employment.csv'
df = pd.read_csv(csv_path)

# 2) Display the first few rows to inspect the data
print("First 5 rows of the dataset:")
print(df.head())
print("\nFirst 10 rows of the dataset:")
print(df.head(10))

# 3) Explore the structure: data types and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# 4) Clean the dataset: only drop rows where Data_value is missing
df_clean = df.dropna(subset=['Data_value'])

# Convert Period into datetime (Period is in YYYY.MM format as float/string)
df_clean['Period'] = pd.to_datetime(df_clean['Period'].astype(str), format='%Y.%m', errors='coerce')

# Drop rows where Period couldn’t be converted
df_clean = df_clean.dropna(subset=['Period'])

print(f"\nShape after cleaning: {df_clean.shape}")

# Visualization 1: Line chart (trend over time for one industry)
agriculture = df_clean[df_clean['Series_title_2'] == 'Agriculture, Forestry and Fishing']

plt.figure(figsize=(10, 5))
plt.plot(agriculture['Period'], agriculture['Data_value'], marker='o', label="Agriculture Jobs")
plt.title("Employment Trend Over Time - Agriculture, Forestry and Fishing")
plt.xlabel("Year")
plt.ylabel("Number of Jobs")
plt.legend()
plt.grid(True)
plt.show()

# Visualization 2: Bar chart (average employment across industries)
avg_jobs = df_clean.groupby('Series_title_2')['Data_value'].mean().sort_values(ascending=False).head(6)

plt.figure(figsize=(10, 5))
avg_jobs.plot(kind='bar', color='skyblue')
plt.title("Average Employment by Industry (Top 6)")
plt.xlabel("Industry")
plt.ylabel("Average Number of Jobs")
plt.xticks(rotation=45, ha='right')
plt.show()

# Visualization 3: Histogram (distribution of job counts)
plt.figure(figsize=(8, 5))
plt.hist(df_clean['Data_value'], bins=30, color='orange', edgecolor='black')
plt.title("Distribution of Employment Values")
plt.xlabel("Number of Jobs")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 4: Scatter plot (relationship between job values and time)
plt.figure(figsize=(10, 5))
plt.scatter(df_clean['Period'], df_clean['Data_value'], alpha=0.6, label="Jobs Data")
plt.title("Scatter Plot of Jobs Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Jobs")
plt.legend()
plt.show()
