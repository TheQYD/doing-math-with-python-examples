#!/usr/bin/env python3

from matplotlib import pyplot as plt

def drawGraph(x, y):
  plt.plot(x, y)
  plt.xlabel('Time of Day')
  plt.ylabel('Temperature')
  plt.title('Weather In NYC')


