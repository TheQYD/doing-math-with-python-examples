#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from sympy.plotting import plot
from sympy import Symbol
from sympy import solve

x = Symbol("x")
y = Symbol("y")

def plotExpressions(expression1, expression2):
	solutions = solve(expression1, expression2)
	plot(expression1, expression2, solutions[0], legend=True)

if __name__ == "__main__":
    expression1 = 3*x + 2
    expression2 = 3*x - 2
    plotExpressions(expression1, expression2)
