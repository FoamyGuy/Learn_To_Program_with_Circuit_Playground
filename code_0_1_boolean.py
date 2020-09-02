# =============================================== #
#   Lesson 0.1
#   boolean variables and basic logic operators
# =============================================== #

# red_led is an boolean variable.
# it can hold the value of either True or False.
# we assign it's value with a single equals sign like the next line
red_led = False
# False is now stored inside of the variable red_led

# we can print the value to the serial console
print(red_led)

# Try changing it's value to True.
# You can edit the line above, or make another line below changing the value.

# boolean values can be used with the logical operators: not, or, and

# not changes the value to the opposite.
# True becomes False and False becomes True.
blue_neopixel = not True
# Try changing the value above and observe the results.

# or combines two logical values and returns true if either of the input values was True.
yellow_neopixel = False or False
# Try changing the values above and observe the results

# and combines two logical values and returns True if both of the input values were True.
pink_neopixel = False and True
# Try changing the values above and observe the results

# the logical operators can be combined together to form more complex logical equations
teal_neopixel = False and not (True or False)
# Try changing the values above and observe the results





# =============================================== #
# ^^ For now just focus on the code above this ^^
# =============================================== #
from adafruit_circuitplayground import cp

cp.red_led = red_led

cp.pixels.brightness = 0.02
if blue_neopixel:
    cp.pixels[0] = (0,0,255)

if yellow_neopixel:
    cp.pixels[1] = (255,255,0)

if pink_neopixel:
    cp.pixels[2] = (255,0,255)

if teal_neopixel:
    cp.pixels[3] = (0,255,255)
while True:
    pass
