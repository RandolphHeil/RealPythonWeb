#import stuff from CSV

import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    #employees = csv.reader(open("employees.csv", "rU"))

    #UPDATE DATA
    c.execute("UPDATE population SET population = 999999999 WHERE city='New York City'")

    # DELETE DATA
    c.execute("DELETE FROM population WHERE city = 'Hanover'")

    print("\n NEW DATA\n")
    c.execute("SELECT * FROM population")
    rows = c.fetchall()
    for r in rows:
        print(r)
