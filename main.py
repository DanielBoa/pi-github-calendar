#!/usr/bin/env python

import sys
import scrollphathd

width = 17
height = 7

while True:
  try:
    for x in range(0, width):
      for y in range(0, height):
        brightness = round((1.0 / width) * x, 2)
        scrollphathd.set_pixel(x, y, brightness)
    scrollphathd.show()
  except KeyboardInterrupt:
    scrollphathd.clear()
    sys.exit(-1)