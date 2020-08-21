# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()

# The ProductID, ProductName, UnitsInStock, and ReorderLevel attributes are selected
# from the products table. It is then ordered by the ProductID attribute.

cur.execute('SELECT ProductID, ProductName, UnitsInStock, ReorderLevel FROM Products ORDER BY ProductID')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
