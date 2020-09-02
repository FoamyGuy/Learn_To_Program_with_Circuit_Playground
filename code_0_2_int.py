# =============================================== #
#   Lesson 0.1
#   int variables and basic math
# =============================================== #

# x is an int variable.
# it can hold any positive or negative whole number, or zero
# we assign it's value with a single equals sign like the next line
x = 0
# 0 is now stored inside of the variable x

# we can print the value to the serial console
print(x)

# we can change the value by using equals sign again
x = 1

# print the value to see if it changed
print(x)





# =============================================== #
# ^^ For now just focus on the code above this ^^
# =============================================== #

import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.02, auto_write=False)
pixels[x] = (255,0,0)
pixels.show()