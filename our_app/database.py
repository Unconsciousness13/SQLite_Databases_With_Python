import sqlite3

# Querry The DB and Return ALL Records


def show_all():
    # Connect To Database
    conn = sqlite3.connect('customer.db')
    # Create a cursor
    c = conn.cursor()
    # Query The Database
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()

    # Close out connection
    conn.close()

# Add New Record To The Table


def add_one(first: str, last: str, email: str):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # Commit our command
    conn.commit()

    # Close out connection
    conn.close()


# Delete record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid == (?)", id)

    # commit and close connection
    conn.commit()
    conn.close()

# Add may records


def add_many(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (List))
    # Commit our command
    conn.commit()

    # Close out connection
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM  customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)
    # Commit our command
    conn.commit()

    # Close out connection
    conn.close()
