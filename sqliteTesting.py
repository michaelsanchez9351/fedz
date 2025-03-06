import sqlite3 

# Connect to SQLite database (creates file if it doesn’t exist)
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Clear the table
cursor.execute("DELETE FROM registry")

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS registry (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, birthDate TEXT)")

# Insert data
cursor.execute("INSERT INTO registry (name, age, birthDate) VALUES (?, ?, ?)", ("Alice", 30, "1994-03-06 14:30:00")) 
cursor.execute("INSERT INTO registry (name, age, birthDate) VALUES (?, ?, ?)", ("Lucas", 111, "1914-01-11 19:48:00"))

# Commit changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM registry")
rows = cursor.fetchall()
for row in rows:
    print(f"Id: {row[0]}, Name: {row[1]}, Age: {row[2]}, Birthday: {row[3]}")

# Close connection
conn.close()