import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Drop Table
c.execute("DROP TABLE customers")
conn.commit()

# Database from customers
c.execute("SELECT rowid,* FROM customers")




items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close()
