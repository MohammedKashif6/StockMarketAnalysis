import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the same database
conn = sqlite3.connect(r"C:\Users\Kashif Hussain\OneDrive\Desktop\DataProjects\StockMarketAnalysis\database\stocks.db")

# Example 1: Total number of records per stock
query1 = """
SELECT name AS Stock, COUNT(*) AS Total_Records
FROM sqlite_master
WHERE type='table';
"""
print("Tables in Database:")
tables = pd.read_sql_query(query1, conn)
print(tables)

# Example 2: Average closing price per stock
stocks = ["ADCB.AB", "DIB.AE", "EMAAR.AE", "EMIRATESNBD.AE", "ETISALAT.AB"]
avg_prices = {}

for stock in stocks:
    query = f'SELECT AVG(Close) AS Avg_Close FROM "{stock}"'
    avg_close = pd.read_sql_query(query, conn)
    avg_prices[stock] = avg_close.iloc[0, 0]

avg_df = pd.DataFrame(list(avg_prices.items()), columns=["Stock", "Avg_Close"])
print("\nAverage Closing Prices:")
print(avg_df)

# Example 3: Visualize average closing prices
plt.figure(figsize=(8,5))
plt.bar(avg_df["Stock"], avg_df["Avg_Close"])
plt.title("Average Closing Price per Stock")
plt.ylabel("Price")
plt.xlabel("Stock")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Example 4: Highest closing price in each stock
for stock in stocks:
    query = f'SELECT Date, Close FROM "{stock}" ORDER BY Close DESC LIMIT 1;'
    result = pd.read_sql_query(query, conn)
    print(f"\nHighest Close for {stock}:")
    print(result)

conn.close()
