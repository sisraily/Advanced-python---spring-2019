# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()

# Three attributes (Columns) are selected. I wasn't sure if we had to display the ContactName, so I displayed it anyway.
# The WHERE statement displays all the tuples(rows) that don't have empty values in the region attribute.
# The ORDER BY statement orders the results by region and then by customer id. 
cur.execute('SELECT CustomerID, ContactName, Region FROM Customers WHERE Region != "" ORDER By Region, CustomerID')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
