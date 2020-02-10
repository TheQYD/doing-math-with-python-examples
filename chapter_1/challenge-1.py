#!/usr/bin/python

'''
Even-Odd Vending Machine
'''

def paritycheck(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

    for factor in range(number, number + 18, 2):
        print(str(factor))


if __name__ == "__main__":

    number = input('Your number please: ')
    paritycheck(number)
