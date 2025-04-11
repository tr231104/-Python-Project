from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Compliments logic
compliments = [
    "You're awesome!", "You're doing great!", "You’re built different!"
]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/compliment', methods=['POST'])
def compliment():
    name = request.form['name']
    message = random.choice(compliments)
    return render_template("compliment.html", name=name, message=message)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template("calculator.html", result=result)
    return render_template("calculator.html", result=None)


app.run(host='0.0.0.0', port=81)
