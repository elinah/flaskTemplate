from flask import Flask

app = Flask(__name__)

@app.route("/") 
def message():
    return __name__ + "\thello"

@app.route("/map")
def mess():
    return "hey"

@app.route("/yay")
def hello():
    return "bye"

if __name__ == '__main__':
    app.run()
