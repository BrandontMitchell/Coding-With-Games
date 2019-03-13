from pygame import *
import random
import time
import math

"""

1. Display
    a. window size
    b. keydown events (space for jump, q for quit)
    c. object placement on load

2. Object movement
    a. Pipes moving left to right at constant speed
        i. once user reaches certain level, move pipes vertically as well as horizontal
    b. bird stays in place, just moves up and down (if past pipes)
    c. Background objects (ground, structures, clouds, etc.)

3. Game physics
    a. bird negative velocity with gravity
    b. bird positive y velocity with help from space bar 

"""