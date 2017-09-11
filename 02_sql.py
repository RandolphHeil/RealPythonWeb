# INSERT stuff in the SQL database


import sqlite3

#connect to db
with sqlite3.connect("new.db") as connection:
    #cursor
    c = connection.cursor()
    #some cities
    cities = [
        ('Boston', 'MA', 600000),
        ('Fulda', 'Hessen', 50000),
        ('Huston', 'TX', 2700000),
        ('Phoenix', 'AZ', 1500000)
    ]

    #insert data to table
    c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)




