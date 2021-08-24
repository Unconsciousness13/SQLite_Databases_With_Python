import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Delete records
c.execute("DELETE FROM customers WHERE rowid == 1 ")

# Commit our command
conn.commit()


# Query database
c.execute("SELECT rowid,* FROM customers")



items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close
