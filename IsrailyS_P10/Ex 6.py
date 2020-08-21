# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()
print('ProductID, ProductName, UnitsInStock, ReorderLevel, ProductsThatNeedReordering (FLAG)')
# The execute statements only selects products that need to be reorderd.
# The ProductID, ProductName, UnitsInstock, ReorderLevel and a new column named ProductsThatNeedReordering
# are selected from the products table. The ProductsThatNeedReordering column evaluates if the UnitsInStock + UnitsOnOrder is less than the ReorderLevel.
cur.execute('SELECT ProductID, ProductName, UnitsInStock, ReorderLevel,(UnitsInStock+UnitsOnOrder <= ReorderLevel AND Discontinued = 0) as ProductsThatNeedReordering FROM Products WHERE ProductsThatNeedReordering = 1')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
