#!/usr/bin/env python3

from sympy.plotting import plot
from sympy import Symbol
from sympy import solve
from sympy import pprint
from sympy import SympifyError
from sympy import sympify 

x = Symbol("x")
y = Symbol("y")

def plotExpressions(expression1, expression2):
    print("Plotting expressions.")
    plot(expression1, expression2, legend=True)


if __name__ == "__main__":
    expression1 = input("Enter your first expression: ")
    expression1 = sympify(expression1)

    expression2 = input("Enter your second expression: ")
    expression2 = sympify(expression2)
    
    solution = solve((expression1, expression2), dict=True)
    
    plotExpressions(expression1, expression2)
