import sqlite3

# database in memory(will delete after close the program)
#conn = sqlite3.connect(":memory:")

# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Create ta Table
c.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email text
)""")

# Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB


# Commit our command
conn.commit()

# Close out connection
conn.close