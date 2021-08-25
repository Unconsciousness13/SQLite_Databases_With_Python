import sqlite3

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Insert one costumer
c.execute("INSERT INTO customers VALUES ('Pako', 'Iliev' , 'pako@pako.es')")


# Insert many customers
many_customers = [('Niki', 'Kolev', 'premier@python.com'),
                  ('Bai', 'Rakiev', 'rakiq@piene.com'),
                  ('Neo', 'Pitonq', 'neo@pitonq.com')]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)


print("Command executed succesfully.")

# Commit our command
conn.commit()

# Close out connection
conn.close()
