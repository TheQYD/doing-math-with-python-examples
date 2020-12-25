#!/usr/bin/python3

def multiplication_table(multipcand):

  for multiplier in range(1, 11):
    print('{0} x {1} = {2}'.format(multiplicand, multiplier, multiplicand*multiplier))


if __name__ == "__main__":

  while True:
      try: 
        multiplicand = input('Enter a number: ')
        multiplication_table(float(multiplicand))

      except ValueError:
        print('Please enter a number.')

    answer = input('Would you like to quit? Press (y) for yes: ')
    if answer == 'y':
      break
