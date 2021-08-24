import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM customers")

# # single fetch (the first item)
# c.fetchone() 
# # selected number of fetch (first tree items)
# c.fetchmany(3)
# #  fetch all items
# c.fetchall()

# item by item
items = c.fetchall()
for item in items:
    #print(item)
    #this print item by item

    #with the index of the item we can display only name , lastname or email
    print(item[0]) # for name only



print("Command executed succesfully.")

# Commit our command
conn.commit()

# Close out connection
conn.close
