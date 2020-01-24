from body import Body
from generator import Nbodies

from vpython import sphere, vector, rate, scene, color,mag2

G = 6.674*1e-11
dt = 1e5  #for human eyes to percieve mo

scene.caption = """
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
"""

Nbodies(10)
