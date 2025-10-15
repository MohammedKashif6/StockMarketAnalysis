import sqlite3
import pandas as pd
import os

# 1️⃣ Define paths
CLEAN_PATH = "../data/cleaned"
DB_PATH = "../database/stocks.db"

# 2️⃣ Create a folder for the database (if not exists)
os.makedirs("../database", exist_ok=True)

# 3️⃣ Connect to SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("✅ Connected to database!")

# 4️⃣ Loop through cleaned CSVs and store them as SQL tables
files = [f for f in os.listdir(CLEAN_PATH) if f.endswith(".csv")]

for file in files:
    symbol = file.replace("cleaned_", "").replace("_data.csv", "")
    df = pd.read_csv(os.path.join(CLEAN_PATH, file))
    
    # Store DataFrame in SQL (replace if already exists)
    df.to_sql(symbol, conn, if_exists="replace", index=False)
    print(f"📁 {symbol} data loaded into database.")

print("\n🎉 All cleaned files stored in stocks.db successfully!")

# Check what tables were created
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("\n📋 Tables in database:", tables)

# 5️⃣ Example Query
query = """
SELECT Date, Close
FROM "ADCB.AB"
WHERE Close > 7.0
ORDER BY Date DESC
LIMIT 5;
"""
result = pd.read_sql_query(query, conn)
print("\n🧠 Sample Query Result (ADCB closing price > 7):")
print(result)

# 6️⃣ Close connection
conn.close()
print("\n🔒 Database connection closed.")


