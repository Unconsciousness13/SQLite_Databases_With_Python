import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Update Records
c.execute("""UPDATE customers SET first_name = 'Pakoni' 
            WHERE rowid == 3
""")


# Commit our command
conn.commit()


# Query database
c.execute("SELECT rowid,* FROM customers")


items = c.fetchall()


for item in items:
    print(item)


# Close out connection
conn.close()
