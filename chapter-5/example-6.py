#!/usr/bin/env python3

import random

def toss():
  if random.random() < 2/3:
    return 0
  else:
    return 1

print(toss())
