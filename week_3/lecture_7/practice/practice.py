import pandas as pd

# Reads csv and reads it as string 
df = pd.read_csv("sample.csv", dtype=str)

# Cleans the first column and the column names 
df.columns = df.columns.str.strip()
df["100%Q"] = df["100%Q"].str.strip()

# Split the packed numeric column
nums = df["mean(ms)"].str.split(r"\s+", expand=True)
nums.columns = ["mean(ms)", "P50(ms)", "P99(ms)", "p99.9(ms)", "#Samples"]

# Assigns the split values
for col in nums.columns:
    df[col] = nums[col]

# Keep only real columns
df = df[["100%Q", "mean(ms)", "P50(ms)", "P99(ms)", "p99.9(ms)", "#Samples"]]

# Convert numeric columns 
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.to_string(index=False))