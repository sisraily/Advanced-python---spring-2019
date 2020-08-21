# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()


cur.execute('SELECT count(ProductID), CategoryName FROM Products JOIN Categories ON Products.CategoryID = Categories.CategoryID GROUP BY CategoryName ORDER BY count(ProductID) DESC')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
