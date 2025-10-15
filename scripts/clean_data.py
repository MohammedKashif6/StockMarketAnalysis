import pandas as pd
import os

# 1. Define the folder where your data is stored
DATA_PATH = "../data"
CLEAN_PATH = "../data/cleaned"

# 2. Create a folder for cleaned data
os.makedirs(CLEAN_PATH, exist_ok=True)

# 3. Get all CSV files in the data folder
files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

# 4. Loop through each file, clean, and save the result
for file in files:
    file_path = os.path.join(DATA_PATH, file)
    print(f"\nCleaning {file}...")

    # Load the CSV into a DataFrame
    df = pd.read_csv(file_path)

     #Remove unwanted symbols
    df = df.replace(r'[\$,%,]', '', regex=True)

    # Convert numeric columns properly
    for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
         df[col] = pd.to_numeric(df[col], errors='coerce')

    #Replace zeros with NaN (since 0 price or volume is invalid)
    df = df.replace(0, pd.NA)
 

    # 5. Handle missing values
    df = df.dropna()  # remove rows with any missing data

    # 6. Remove duplicate rows (if any)
    df = df.drop_duplicates()

    # 6️⃣ Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # 7. Reset index after cleaning
    df = df.reset_index(drop=True)

    # 8. Save cleaned data to new folder
    cleaned_file_path = os.path.join(CLEAN_PATH, f"cleaned_{file}")
    df.to_csv(cleaned_file_path, index=False)

    
    print(f"✅ Cleaned file saved as {cleaned_file_path}")
    
print("\nAll files cleaned successfully!")
