import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
try:
    df = pd.read_csv("sample_data.csv")
    print("Dataset Loaded Successfully!\n")
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean data (remove missing rows)
df_clean = df.dropna()

print("\nCleaned Data:")
print(df_clean)

# Filter: Age > 25
filtered = df_clean[df_clean["Age"] > 25]
print("\nFiltered Data (Age > 25):")
print(filtered)

# Group by Department
grouped = df_clean.groupby("Department").mean(numeric_only=True)
print("\nGrouped Data by Department:")
print(grouped)

# Summary statistics
print("\nSummary Statistics:")
print(df_clean.describe())

# Create graph
df_clean["Salary"].plot(kind="bar")
plt.title("Salary Distribution")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()