#!/usr/bin/env python3
'''
Draw the trajectory of a body in projectile motion.
'''

from matplotlib import pyplot as plt
import math

def frange(start, final, increment):
  numbers = []

  while start < final:
    numbers.append(start)
    start = start + increment

  return numbers

def drawGraph(x, y):
  plt.plot(x, y)
  plt.xlabel('x-coordinate')
  plt.ylabel('y-coordinate')
  plt.title('Projectile Motion of a Ball')

def drawTrajectory(u, theta):
  theta = math.radians(theta)
  gravity = 9.8

  # Time of flight
  t_flight = 2*u*math.sin(theta)/gravity

  # Find time intervals
  intervals = frange(0, t_flight, 0.001)

  # Luist of x and y coordinates
  x = []
  y = []
  for time in intervals:
    x.append(u*math.cos(theta)*time)
    y.append(u*math.sin(theta)*time - 0.5*gravity*time**2)

  drawGraph(x, y)

if __name__ == '__main__':
  try:
    u = float(input('Enter the initial velocity (m/s): '))
    theta = float(input('Enter the angle of projection (degrees): '))
  
  except ValueError:
    print('You entered an invalid input')
  
  else:
    drawTrajectory(u, theta)
    plt.show()
