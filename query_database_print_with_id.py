import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Query database
c.execute("SELECT rowid,* FROM customers")


items = c.fetchall()

for item in items:
   print(item)


# Commit our command
conn.commit()

# Close out connection
conn.close()

