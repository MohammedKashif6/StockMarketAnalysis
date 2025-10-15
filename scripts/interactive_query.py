import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("../database/stocks.db")

# List available tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Available tables:\n", tables, "\n")

# Ask user for which stock they want to analyze
table_name = input("Enter the stock table name (e.g. ADCB.AB): ")

# Ask user which query they want
print("\nChoose an option:")
print("1. Show recent 5 records")
print("2. Show days where closing price > X")
print("3. Show average closing price")
choice = input("Enter choice (1/2/3): ")

if choice == "1":
    query = f'SELECT * FROM "{table_name}" ORDER BY Date DESC LIMIT 5;'

elif choice == "2":
    price = float(input("Enter minimum closing price: "))
    query = f'SELECT Date, Close FROM "{table_name}" WHERE Close > {price} ORDER BY Date DESC LIMIT 10;'

elif choice == "3":
    query = f'SELECT AVG(Close) AS Average_Close FROM "{table_name}";'

else:
    print("Invalid choice.")
    conn.close()
    exit()

# Run and display query
result = pd.read_sql_query(query, conn)
print("\nQuery result:\n", result)

# Close connection
conn.close()
