import yfinance as yf
import pandas as pd
import os

# 1. Create a folder path for saving data
DATA_PATH = "../data"

# 2. Define a list of stock tickers to download (you can add more)
tickers = ["ADCB.AB", "EMIRATESNBD.AE", "DIB.AE", "EMAAR.AE", "ETISALAT.AB"]

# 3. Create the folder if it doesn’t exist
os.makedirs(DATA_PATH, exist_ok=True)

# 4. Loop through each ticker and download data
for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    
    # 5. Save each company's data as a CSV file in the data folder
    file_path = os.path.join(DATA_PATH, f"{ticker}_data.csv")
    data.to_csv(file_path)
    print(f"Saved {ticker} data to {file_path}")

print("\n✅ Data download complete! Check your 'data' folder.")
