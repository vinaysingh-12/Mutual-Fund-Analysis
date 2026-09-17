import sqlite3
import pandas as pd
import os

db_path = "bluestock_mf.db"
schema_path = "schema.sql"

print(f"Connecting to {db_path}...")
conn = sqlite3.connect(db_path)

# 1. Drop the generic tables created by pandas
tables_to_reset = [
    "dim_date", "dim_fund", "fact_nav", 
    "fact_transactions", "fact_performance", "fact_aum"
]
for table in tables_to_reset:
    conn.execute(f"DROP TABLE IF EXISTS {table};")
print("Cleared old generic tables.")

# 2. Apply the strict schema from schema.sql
with open(schema_path, 'r') as file:
    schema_sql = file.read()
    conn.executescript(schema_sql)
print("Strict schema applied successfully!")

# 3. Reload the cleaned data into the new strict tables
print("Reloading data from processed CSVs...")
for table in tables_to_reset:
    csv_path = f"data/processed/{table}.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        # Use 'append' so it respects your strict schema constraints
        df.to_sql(table, conn, if_exists='append', index=False)
        print(f" -> Loaded {len(df)} rows into {table}")
    else:
        print(f" -> Warning: {csv_path} not found.")

conn.close()
print("\nSuccess! Database is now fully configured with strict constraints and loaded data.")