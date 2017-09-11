# Create a SQLLite3 database and table

# import sqllight library
import sqlite3

# create a new database if the database doesnt exist

conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

#clsoe connection
conn.close()