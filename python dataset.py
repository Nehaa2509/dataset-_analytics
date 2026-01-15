import pandas as pd
import os
import sys

# ==============================
# CSV File Detection
# ==============================
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
else:
    # Default CSV names to check
    possible_files = ["dataset.csv", "titanic.csv", "StudentsPerformance.csv"]
    csv_file = None

    for file in possible_files:
        if os.path.exists(file):
            csv_file = file
            break

if csv_file is None:
    print("\nERROR: No CSV file found to load.")
    print("Looked for: dataset.csv, titanic.csv, StudentsPerformance.csv")
    print("Script folder:", os.getcwd())
    print("\nFix:")
    print("- Put your CSV file in the same folder as this script, OR")
    print("- Run: python dataset.py <your_file.csv>")
    sys.exit()

print(f"\nLoaded file: {csv_file}")

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv(csv_file)

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Last 5 Records ---")
print(df.tail())


# ==============================
# Dataset Info
# ==============================
print("\n--- Dataset Info ---")
df.info()

print("\n--- Statistical Summary ---")
print(df.describe())


# ==============================
# Feature Types
# ==============================
numerical_features = df.select_dtypes(include=["int64", "float64"]).columns
categorical_features = df.select_dtypes(include=["object"]).columns

print("\nNumerical Features:")
print(list(numerical_features))

print("\nCategorical Features:")
print(list(categorical_features))


# ==============================
# Unique Values
# ==============================
print("\n--- Unique Values in Categorical Columns ---")
for col in categorical_features:
    print(f"\n{col}:")
    print(df[col].unique())


# ==============================
# Missing Values
# ==============================
print("\n--- Missing Values Per Column ---")
print(df.isnull().sum())


# ==============================
# Dataset Size
# ==============================
rows, cols = df.shape
print(f"\nDataset contains {rows} rows and {cols} columns.")

if rows >= 500:
    print("Dataset size is suitable for basic machine learning.")
else:
    print("Dataset is small but usable for learning purposes.")


# ==============================
# Target Variable Note
# ==============================
print("\nNOTE:")
print("Choose the target variable manually based on dataset context.")
