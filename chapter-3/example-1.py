#!/usr/bin/env python3

'''
Calculating the Mean
'''

def calculate_mean(numbers):
  total = sum(numbers)
  length = len(numbers)

  # Calculate the mean
  mean = total/length

  return mean

if __name__ == '__main__':
  donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
  mean = calculate_mean(donations)
  length = len(donations)
  print('Mean donation over the last {0} days is {1}'.format(length, mean))
