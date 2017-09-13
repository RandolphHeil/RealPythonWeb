import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    sql = {"make_model_quantity" :  "SELECT make, model, quantity from orders",

        "order_count" : "SELECT count(DISTINCT model) FROM orders WHERE inventory.model = orders.model"}

    for keys, values in sql.items():
        c.execute(values)
        result = c.fetchall()
        print(keys + " : ", result[0])
        print(keys + " : ", result[1])
        #print(keys + " : ", result[2])





        # make/ model -> quantiy -> ordercount