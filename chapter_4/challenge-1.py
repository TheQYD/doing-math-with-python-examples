#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from sympy import Symbol
from sympy import factor
from sympy import expand

x = Symbol('x')
y = Symbol('y')

def factorFinder(expression):
    factors = factor(expression)
    return factors

if __name__ == '__main__':
    while True:
        try: 
            expression = input("Input your expression: ")
            print(factorFinder(expression))

        except tokenize.TokenError:
            print("Please input a valid expression.")
