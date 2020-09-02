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
x = 4

# print the value to see if it changed
print(x)

# We can do math with int variables.
print(x + 4)  # addition
print(x - 1)  # subtraction
print(x * 22)  # multiplication
print(x / 2)  # division

# try setting x back to 0 and see which LED is on
# x = 0

# try 1, 2, 3 ,4 and see which LEDs come on.

# Can you guess what will happen with some other numbers like 5, 7 , or 9?

# What about 10?

# Modulus operation - remainder from division

# 4 / 3 = 1 r: 1
# 4 % 3 = 1

# 10 / 10 = 1 r: 0
# 10 % 10 = 0


# x = 10 % 10
# print(x)

# WARNING!
# Python does allow you to change the type of a variable
# x = False
# This will often lead to your program breaking, unless it is accounted for.


# =============================================== #
# ^^ For now just focus on the code above this ^^
# =============================================== #

import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.02, auto_write=False)
pixels[x] = (255, 0, 0)
pixels.show()
