# ---- Flask Hello World ---- #

#import the Flask class form the flask package
from flask import Flask

# create application object
app = Flask(__name__)

# use the decorator pattern to
# link the view function to a url

@app.route("/")
@app.route("/hello")

#define the view usin a function which returns a string
def hello_world():
    return "Hello World!"

@app.route("/test")
def test():
    return "Success!"

#start the development server usint the run() method

if __name__ == "__main__":
    app.run()