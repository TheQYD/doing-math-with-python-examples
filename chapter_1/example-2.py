#!/usr/bin/python

def multiplication_table(multipcand):

    for multiplier in range(1, 11):
        print('{0} x {1} = {2}'.format(multiplicand, multiplier, multiplicand*multiplier))

if __name__ == "__main__":

    multiplicand = input('Enter a number: ')
    multiplication_table(float(multiplicand))
