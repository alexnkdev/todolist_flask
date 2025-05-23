#!/usr/bin/env python3

from flask import Flask, request
import math
app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <h1>Solve Quadratic Equation</h1>
    <form action="/solve_quadratic_equation" method="POST">
         <input name="a">x^2+
         <input name="b">x+
         <input name="c">=0
         <br/>
         <input type="submit" value="Submit!">
     </form>
    '''

@app.route("/solve_quadratic_equation", methods=["POST"])
def echo_input():
    if not request.form.get("a", ""):
        return "Please enter a"
    if not request.form.get("b", ""):
        return "Please enter b"
    if not request.form.get("c", ""):
        return "Please enter c"
    a = int(request.form.get("a", ""))
    b = int(request.form.get("b", ""))
    c = int(request.form.get("c", ""))
    if a == 0:
        # b*x + c = 0
        if b == 0:
          # c = 0
          if c == 0:
            return "Infinite many solutions."
          else:
            return "No Solutions."
        else:
            return f"X = {-c/b}"

    else:
        d = b * b - 4 * a * c
        if d < 0:
            return "No real roots"
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return f"x1 = {x1}, X2={x2}"

