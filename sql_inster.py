from random import randint
import sqlite3

numberlist = []
#create list to fill up db

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    #c.execute("CREATE TABLE numbers (number INTEGER)")
    """
    for i in range(100):
        x = randint(0,100)
        c.execute("INSERT INTO numbers(number) VALUES (?)", (x,))
    """


    while True:
        what_to_do = input("What do you want to do?")
        if what_to_do == "AVG":
            sql_input = "SELECT avg(number) FROM numbers"

        elif what_to_do == "MAX":
            sql_input = "SELECT max(number) FROM numbers"

        elif what_to_do == "MIN":
            sql_input = "SELECT min(number) FROM numbers"

        elif what_to_do == "SUM":
            sql_input = "SELECT sum(number) FROM numbers"

        elif what_to_do == "exit":
            exit()
        else:
            print("Possible commands are AVG, MAX, MIN, SUM.")
            continue

        c.execute(sql_input)
        result = c.fetchone()
        print(result)
