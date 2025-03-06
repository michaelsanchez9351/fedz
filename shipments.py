import sqlite3 

# DB initilization 
conn = sqlite3.connect("shipments.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS shipments (id INTEGER PRIMARY KEY, fedzId INTEGER, weight TEXT, shipper TEXT, priority TEXT)")
conn.commit()

conn.close()