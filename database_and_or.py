import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Order Tha database and/or
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'El%' AND rowid = 2")

#Case Or
c.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'El%' OR rowid = 2")




items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close()
