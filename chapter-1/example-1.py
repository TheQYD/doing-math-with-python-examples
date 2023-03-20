#!/usr/bin/env python3

'''
Find the factors of an integer.
'''

def factors(b):
  for i in range(1, b+1):
    if b % i == 0:
      print(i)

if __name__ == '__main__':

  while True:
    integer_input = False

    while integer_input == False:

      b = input('Your Number Please: ')
      
      try:
        b = float(b)
        if b > 0 and b.is_integer():
          factors(int(b))
          integer_input = True
        else:
          print('Please enter a positive integer!')

      except:
        print('Please enter a number')

    answer = input('Would you like to exit? Press (y) for yes: ')
    if answer == 'y':
      break

