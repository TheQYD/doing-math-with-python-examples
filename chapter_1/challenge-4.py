#!/usr/bin/python3

from fractions import Fraction

def add(a,b):
  print('Result of Addition: {0}'.format(a+b))

def subtract(a,b):
  print('Result of Subtraction: {0}'.format(a-b))

def multiply(a,b):
  print('Result of Multiplication: {0}'.format(a*b))

def divide(a,b):
  print('Result of Dividing First Fraction by the Second: {0}'.format(a/b))

if __name__ == '__main__':
  a = Fraction(input('Enter first fraction: '))
  b = Fraction(input('Enter second fraction: '))
  operation = input('Operation to perfrom - Add, Subtract, Multiply, Divide: ')

  if operation == 'Add':
    add(a,b)

  if operation == 'Subtract':
    subtract(a,b)

  if operation == 'Multiply':
    multiply(a,b)

  if operation == 'Divide':
    divide(a,b)

