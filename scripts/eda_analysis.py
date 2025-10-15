import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Define the folder with cleaned data
CLEAN_PATH = "../data/cleaned"

# 2. Load all cleaned CSV files into a dictionary
files = [f for f in os.listdir(CLEAN_PATH) if f.endswith(".csv")]
data = {}

for file in files:
    symbol = file.replace("cleaned_", "").replace("_data.csv", "")
    df = pd.read_csv(os.path.join(CLEAN_PATH, file))
    data[symbol] = df
    print(f"Loaded {symbol} with {len(df)} rows.")

# 3. Pick one stock to explore first (e.g., ADCB)
sample_stock = list(data.keys())[0]
df = data[sample_stock]

print(f"\n📊 Exploring {sample_stock} data...")
print(df.head())

# 4. Basic summary statistics
print("\nSummary statistics:")
print(df.describe())

# 5. Plot Closing Price over time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.title(f'{sample_stock} - Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()

# 6. Compute and plot daily returns
df['Daily Return'] = df['Close'].pct_change() * 100
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Daily Return'], label='Daily Return', color='green')
plt.title(f'{sample_stock} - Daily Returns (%)')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.legend()
plt.grid(True)
plt.show()

# 7. Correlation analysis across multiple stocks (if >1 stock)
if len(data) > 1:
    close_prices = pd.DataFrame()

    for symbol, d in data.items():
        close_prices[symbol] = d['Close']

    corr = close_prices.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation of Closing Prices Between Stocks")
    plt.show()
