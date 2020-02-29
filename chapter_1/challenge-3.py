#!/usr/bin/python

'''
Unit Converter
'''

def print_menu():
    # Distance
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

    # Mass
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')

    # Temperature
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')


# Distance
def kilometers_to_miles():
    kilometers = float(input('Enter distance in kilometers: '))
    miles = kilometers / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_to_kilometers():
    miles = float(input('Enter distance in miles: '))
    kilometers = miles * 1.609

    print ('Distance in kilometers: {0}'.format(kilometers))

# Mass
def kilograms_to_pounds():
    kilograms = float(input('Enter mass in kilograms: '))
    pounds = kilograms * 2.20462

    print('Weight in pounds: {0}'.format(pounds))

def pounds_to_kilograms():
    pounds = float(input('Enter weight in pounds: '))
    kilograms = pounds / 2.20462

    print('Mass in kilograms: {0}'.format(kilograms))


if __name__ == "__main__":
    print_menu()
    choice = str(input('Which conversion would you like to do?: '))

    if choice == '1':
        kilometers_to_miles()

    if choice == '2':
        miles_to_kilometers()

    if choice == '3':
        kilograms_to_pounds()

    if choice == '4':
        pounds_to_kilograms()

