#!/usr/bin/python3

'''
Enhanced Multiplication Table Generator
'''

def generate_table(mulitplicand, mulitple):
  
  for number in range(1, multiple):
    print('{0} x {1} = {2}'.format(multiplicand, number, multiplicand*number))


if __name__ == '__main__':

  while quit != 'y':
    multiplicand = int(input('Multiply the number: '))
    multiple = int(input('Up to the multiple: '))
    generate_table(multiplicand, multiple)

    quit = input('Would you like to quit? Press (y) for yes: ')

