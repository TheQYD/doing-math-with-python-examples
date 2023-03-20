#!/usr/bin/env python3

'''
Even-Odd Vending Machine
'''

def paritycheck(number):
  if number % 2 == 0:
    print("The number {0} is even.".format(number))
  else:
    print("The number {0} is odd.".format(number))

  for factor in range(number, number + 18, 2):
    print(str(factor))


if __name__ == "__main__":

  while True:
    number = int(input('Your number please: '))
    paritycheck(number)

    answer = input('Would you like to quit? Press (y) for yes: ')
    if answer == 'y':
      break
