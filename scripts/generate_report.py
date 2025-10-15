import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# --- 1️⃣ Connect to database ---
conn = sqlite3.connect(r"C:\Users\Kashif Hussain\OneDrive\Desktop\DataProjects\StockMarketAnalysis\database\stocks.db")
stocks = ["ADCB.AB", "DIB.AE", "EMAAR.AE", "EMIRATESNBD.AE", "ETISALAT.AB"]

# --- 2️⃣ Fetch data & calculate stats ---
summary_data = []
for stock in stocks:
    df = pd.read_sql_query(f'SELECT Date, Close FROM "{stock}"', conn)
    if df.empty:
        continue
    avg_price = round(df["Close"].mean(), 2)
    max_close = round(df["Close"].max(), 2)
    min_close = round(df["Close"].min(), 2)
    summary_data.append([stock, avg_price, max_close, min_close])

summary_df = pd.DataFrame(summary_data, columns=["Stock", "Avg Close", "Max Close", "Min Close"])

# --- 3️⃣ Plot a chart ---
plt.figure(figsize=(8,5))
plt.bar(summary_df["Stock"], summary_df["Avg Close"], color='skyblue')
plt.title("Average Closing Price per Stock")
plt.xlabel("Stock")
plt.ylabel("Average Close")
plt.tight_layout()
chart_path = r"C:\Users\Kashif Hussain\OneDrive\Desktop\DataProjects\StockMarketAnalysis\outputs\avg_close_chart.png"
plt.savefig(chart_path)
plt.close()

# --- 4️⃣ Create PDF report ---
pdf_path = r"C:\Users\Kashif Hussain\OneDrive\Desktop\DataProjects\StockMarketAnalysis\outputs\Daily_Stock_Report.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>Daily Stock Market Analysis Report</b>", styles["Title"]))
elements.append(Spacer(1, 12))

# Summary table
table_data = [["Stock", "Average Close", "Highest Close", "Lowest Close"]] + summary_data
table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
]))
elements.append(table)
elements.append(Spacer(1, 20))

# Add chart
elements.append(Paragraph("Average Closing Prices:", styles["Heading2"]))
elements.append(Image(chart_path, width=400, height=250))

# Build PDF
doc.build(elements)
conn.close()

print(f"✅ Report generated successfully at: {pdf_path}")
