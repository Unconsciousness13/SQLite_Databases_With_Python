import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM customers WHERE last_name == 'Kolev'")

# Age example
# c.execute("SELECT * FROM customers WHERE age >= 18 ")

# Like axample
#c.execute("SELECT * FROM customers WHERE last_name Like 'Ko%'")

items = c.fetchall()


for item in items:
    print(item)
# Commit our command
conn.commit()

# Close out connection
conn.close
