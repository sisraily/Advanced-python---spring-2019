# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()

# The OrderID and OrderDate rows from the Orders table are selected.
# The JOIN statement is used to connect the shipper ID's from the shippers table the ShipVia attribute
# in the orders table. The WHERE statement then limits the results to those that were shipped with Federal Shipping
cur.execute("SELECT OrderID, OrderDate FROM Orders JOIN Shippers ON Orders.ShipVia = Shippers.ShipperID WHERE CompanyName = 'Federal Shipping'")
conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
