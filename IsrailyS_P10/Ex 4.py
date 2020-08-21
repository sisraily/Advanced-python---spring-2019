# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()

# We select the count of the CustomerID attribute, as well as the Country and City attributes.
# The Count(CustomerID) is the grouped by country, then city. We then also order the results by the count in descending order.
cur.execute('SELECT count(CustomerID), Country, City From Customers GROUP BY Country, City ORDER BY COUNT(CustomerID) DESC')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
