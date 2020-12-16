#!/usr/bin/python3

'''
Unit Converter: Miles to Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def kilometers_to_miles():
    kilometers = float(input('Enter distance in kilometers: '))
    miles = kilometers / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_to_kilometers():
    miles = float(input('Enter distance in miles: '))
    kilometers = miles * 1.609

    print ('Distance in kilometers: {0}'.format(kilometers))

if __name__ == "__main__":

  while True:
    print_menu()
    choice = str(input('Which conversion would you like to do?: '))

    if choice == '1':
        kilometers_to_miles()

    if choice == '2':
        miles_to_kilometers()

    answer = input('Would you like to quit? Press (y) for yes: ')
    if answer == 'y':
      break
