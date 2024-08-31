from flask import Flask
from datetime import datetime

# print(__name__)

app = Flask(__name__)

books = {1: "Python book", 2: "Java book", 3: "Flask book"}


@app.route("/")
def index():
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(today)
    return f"<h1>Hello Flask!</h1><h2>Hi Flask!</h2><h3>How are you Flask?</h3><h4>Flask {today}!</h4>"


@app.route("/books")
def showBooks():
    return books


@app.route("/book/<int:id>")
def showBook(id):
    if id in books:
        return f"<h1 style='background-color:black; color:white'>編號{id}: {books[id]}</h1>"
    return f"<h1 style='color:red'>無此編號:{id}</h1>"


@app.route("/sum/x=<x>&y=<y>")
def mySum(x=0, y=0):
    try:
        total = eval(x) + eval(y)
        return f"<h2>{x} + {y} = {total}</h2>"
    except Exception as e:
        print(e)
        return "<h2 style='color:red'>輸入參數錯誤</h2>"


@app.route("/bmi/name=<name>&height=<height>&weight=<weight>")
def getBmi(name, height, weight):
    try:
        bmi = eval(weight) / (eval(height) / 100) ** 2
        return f"<h2>姓名: {name}, BMI: {bmi:.2f}</h2>"

    except Exception as e:
        print(e)
        return "<h2 style='color:red'>輸入參數錯誤</h2>"


app.run(debug=True)
