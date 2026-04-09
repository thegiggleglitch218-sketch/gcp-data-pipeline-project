import pandas as pd

# Load data
df = pd.read_csv('raw_sales.csv')

# Clean data
df.dropna(inplace=True)
df.columns = df.columns.str.lower()

# Convert date column (if exists)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# Save cleaned data
df.to_csv('cleaned_sales.csv', index=False)

print("Data cleaned successfully")
