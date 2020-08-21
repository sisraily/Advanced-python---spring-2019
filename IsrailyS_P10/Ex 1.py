# imports the sqlite3 library
import sqlite3

# We connect to the database using the connect method. 
conn = sqlite3.connect('practice.db')

# Create a cursor
cur = conn.cursor()

# The te ProductID, ProductName and companyName attributes(column) are selected from the Products table.
# The JOIN statement is used to join the SupplierId attribute from the Products Table to the
# SupplierID in the Suppliers table.
cur.execute('SELECT ProductID, ProductName, CompanyName FROM Products JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID ORDER BY ProductID')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
