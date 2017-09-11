# ---- Flask Hello World ---- #

#import the Flask class form the flask package
from flask import Flask

# create application object
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

# use the decorator pattern to
# link the view function to a url

@app.route("/")
@app.route("/hello")

#define the view usin a function which returns a string
def hello_world():
    return "Hello World!!!!!!!!!!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/name/<name>")
def index(name):
    if name.lower() == "randolph":
        print("test")
        return "Hello {}.".format(name), 200
    else:
        return "Not found!", 404

#start the development server usint the run() method

if __name__ == "__main__":
    app.run()