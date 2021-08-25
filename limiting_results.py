import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()



# Database ORder/LIMIT
c.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC LIMIT 4")




items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close()
