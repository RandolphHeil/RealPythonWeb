import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    try:
        c.execute(""" CREATE TABLE orders (make TEXT, model TEXT, order_date DATE)""")
    except:
        print("Table available!")

    orders = [
        ("Ford", "Fiesta", "2017-05-06"),
        ("Ford", "Fiesta", "2017-01-01"),
        ("Honda", "Freelancer", "2017-12-31"),
        ("Hyundai", "i30", "2017-05-09"),
        ("Honda", "CarCar", "2016-08-08")

    ]

    #c.executemany("INSERT INTO orders VALUES (?,?,?)", orders)

    c.execute("""SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date 
        FROM inventory, orders 
        WHERE inventory.make = orders.make 
        AND inventory.model = orders.model
        ORDER BY orders.order_date ASC""")

    rows = c.fetchall()

    for r in rows:
        print ("Make: ", r[0], ", Model: ",  r[1])
        print("Quanity: ", r[2], ", Order Date: ", r[3])
        print(" ")



