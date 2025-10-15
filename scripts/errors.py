# Check what tables were created
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("\n📋 Tables in database:", tables)
