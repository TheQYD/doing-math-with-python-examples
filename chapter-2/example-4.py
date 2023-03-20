#!/usr/bin/env python3
'''
Comparing the Trajectory at Different Initial Velocities
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
  u_list = [20, 40, 60]
  theta = 45
  for u in u_list:
    drawTrajectory(u, theta)

  plt.legend(['20', '40', '60'])
  plt.show()
