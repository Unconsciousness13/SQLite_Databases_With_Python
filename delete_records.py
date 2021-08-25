import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Order By Database - Order BY
c.execute("SELECT rowid,* FROM customers ORDER BY rowid ")

# Order Descending
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")



items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close()
