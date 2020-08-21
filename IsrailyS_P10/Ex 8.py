# imports the sqlite3 library
import sqlite3

# The connect method within the sqlite3 library is used to connect to the database file. 
conn = sqlite3.connect('practice.db')

# Creates a cursor
cur = conn.cursor()

# The avg and group by statements are used to get the average freight cost grouped by country.
# The ORDER BY statement is used to order the results by the average freight coust in the country.
# DESC displays the results in descending order.
# The LIMIT 3 statements limits the results to the top 3.
cur.execute('SELECT avg(Freight), ShipCountry FROM orders GROUP BY ShipCountry ORDER BY avg(Freight) DESC LIMIT 3')

conn.commit()

# We loop through the cursor to print out the result. 
for i in cur:
    print(i)


cur.close()
