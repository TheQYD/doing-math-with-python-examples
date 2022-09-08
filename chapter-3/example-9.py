#!/usr/bin/env python3

# Find the sum of number store in a file

def sum_data(filename):
  s = 0
  with open(filename) as f:
    for line in f:
      s = s + float(line)

  print('Sum of the numbers: {0}'.format(s))


if __name__ == '__main__':
  sum_data('mydata.txt')
