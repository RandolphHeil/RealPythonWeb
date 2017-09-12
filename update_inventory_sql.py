#import stuff from CSV

import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    #employees = csv.reader(open("employees.csv", "rU"))
    try:
        c.execute("CREATE TABLE inventory (make TEXT, model TEXT, quantity INTEGER)")
    except:
        print("Alrady there")
    """
    new_cars = [
        ("Ford", "Fiesta", 5),
        ("Ford", "Pacific", 2),
        ("Honda", "Freelancer", 6),
        ("Honda", "CarCar", 10),
        ("Hyundai", "i30", 2),
        ("Honda", "MyCar", 3),
    ]

    #Update inventroy Tables
    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", new_cars)
    """
    c.execute("UPDATE inventory SET quantity = 20 WHERE model='Fiesta'")
    c.execute("UPDATE inventory SET quantity = 200 WHERE model='CarCar'")

    print("\n NEW DATA\n")
    c.execute("SELECT * FROM inventory WHERE make='Ford'")
    rows = c.fetchall()
    for r in rows:
        print(r)