import sqlite3

# Connect to SQLite database (creates file if it doesn’t exist)
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# Commit changes
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(f"Id: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close connection
conn.close()