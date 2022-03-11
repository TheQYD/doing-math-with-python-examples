#!/usr/bin/env python3

from matplotlib import pyplot as plt

def drawGraph(x, y):
  plt.plot(x, y)
  plt.xlabel('Hours')
  plt.ylabel('Temperature')
  plt.title('Weather In NYC')
  plt.show()

if __name__ == '__main__':
  temperature = [42, 40, 37, 39, 48, 51, 48, 46]
  hours = range(0, len(temperature))
  drawGraph(hours, temperature)
