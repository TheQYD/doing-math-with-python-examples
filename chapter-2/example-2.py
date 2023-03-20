#!/usr/bin/env python3

'''
The relationship between gravitational force 
and distance between two bodies
'''

import matplotlib.pyplot as plt

def initValues():
  mass1 = 0.5
  mass2 = 1.5
  radius = range(100, 1001, 50)
  gravitational_force = []
  gravitational_constant = 6.67*(10**-11)

  for distance in radius:
    force = gravitational_constant*(mass1*mass2)/(distance**2)
    gravitational_force.append(force)

  drawGraph(radius, gravitational_force)

def drawGraph(x, y):
  plt.plot(x, y, marker='o')
  plt.xlabel('Distance in Meters')
  plt.ylabel('Gravitational force in Newtons')
  plt.title('Gravitational force and distance')
  plt.show()

if __name__ == '__main__':
  initValues()
