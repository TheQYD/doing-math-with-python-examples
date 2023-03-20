#!/usr/bin/env python3

from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
  var = Symbol(var)
  d = Derivative(f, var).doit()
  pprint(d)

if __name__ == '__main__':
  f = input('Differentiating the function: ')
  var = input('With respect to :')
  
  try:
    f = sympify(f)
  except:
    print('Invalid input')
  else:
    derivative(f, var)
