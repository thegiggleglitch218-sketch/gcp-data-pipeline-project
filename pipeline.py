import pandas as pd
import numpy as np
import os

print("Files:", os.listdir())

# Load dataset
df = pd.read_csv('customers-1000.csv')

print("\n--- BEFORE CLEANING ---")
print(df.head())
print(df.info())

# -----------------------------
# 1. STANDARDIZE SCHEMA
# -----------------------------
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Trim all string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# -----------------------------
# 2. DATA QUALITY HANDLING
# -----------------------------
# Remove duplicates based on business key
df.drop_duplicates(subset=['customer_id', 'email'], inplace=True)

# Fill missing categorical values
df['country'] = df['country'].fillna('Unknown')
df['city'] = df['city'].fillna('Unknown')

# -----------------------------
# 3. ADVANCED TRANSFORMATIONS
# -----------------------------

# Full Name (Business-friendly field)
df['full_name'] = df['first_name'].str.title() + " " + df['last_name'].str.title()

# Email normalization
df['email'] = df['email'].str.lower()

# Extract domain from email (VERY GOOD TRANSFORMATION)
df['email_domain'] = df['email'].str.split('@').str[1]

# Standardize phone (keep only digits)
df['primary_phone'] = df['phone_1'].str.replace(r'\D', '', regex=True)

# Drop secondary phone (low business value)
df.drop(columns=['phone_2'], inplace=True)

# -----------------------------
# 4. DATE ENGINEERING
# -----------------------------
df['subscription_date'] = pd.to_datetime(df['subscription_date'], errors='coerce')

df['subscription_year'] = df['subscription_date'].dt.year
df['subscription_month'] = df['subscription_date'].dt.month
df['subscription_quarter'] = df['subscription_date'].dt.to_period('Q').astype(str)

# Customer tenure (advanced logic)
current_year = pd.Timestamp.now().year
df['customer_tenure_years'] = current_year - df['subscription_year']

# -----------------------------
# 5. BUSINESS LOGIC FEATURES
# -----------------------------

# Region mapping (simulate business logic)
region_map = {
    'USA': 'North America',
    'India': 'Asia',
    'UK': 'Europe'
}

df['region'] = df['country'].map(region_map).fillna('Other')

# Customer segmentation based on tenure
df['customer_segment'] = pd.cut(
    df['customer_tenure_years'],
    bins=[0, 1, 3, 5, 100],
    labels=['New', 'Growing', 'Loyal', 'Legacy']
)

# -----------------------------
# 6. DATA MODEL OPTIMIZATION
# -----------------------------

# Reorder columns (like curated layer)
final_columns = [
    'customer_id',
    'full_name',
    'email',
    'email_domain',
    'primary_phone',
    'company',
    'city',
    'country',
    'region',
    'subscription_date',
    'subscription_year',
    'subscription_month',
    'subscription_quarter',
    'customer_tenure_years',
    'customer_segment',
    'website'
]

df = df[final_columns]

print("\n--- AFTER TRANSFORMATION ---")
print(df.head())
print(df.info())

# Save final dataset
df.to_csv('customers_curated.csv', index=False)

print("\n✅ Curated dataset saved as 'customers_curated.csv'")
