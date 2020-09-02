# =============================================== #
#   Lesson 0.3
#   string variables and operations
# =============================================== #

# notes is a string variables
# it's value must be enclosed by single or double quotes
notes = "c"

# Strings can hold letters, numbers, and special characters.
# The can be virtually any length

# following example_string contains a few sentences with words, numbers and special characters.
# There is eve a single quote mark used! Because the string itself uses double quotes this works with no problem.
example_string = "Hello There! 3 Quick foxes ran up the hill. The fox's fur was red and brown."

# We can print strings like this
print(example_string)

name = "Sally" # change this to your name if you'd like

# We can combine strings with the plus sign
prompt = "Hello " + name + " how are you?"
print(prompt)

# We can use the astrisks symbol with strings to multiply them
# e.x. "a" * 3 would result in the string "aaa"

# notes = 'a' * 2 + 'b' * 3 + "ccdg"  # this results in the string "aabbbccdg"


# =============================================== #
# ^^ For now just focus on the code above this ^^
# =============================================== #
import time
from adafruit_circuitplayground.express import cpx
import board


NOTE_TO_FREQUENCY = {
    "c": 261.63,
    "d": 293.66,
    "e": 329.63,
    "f": 349.23,
    "g": 392.00,
    "a": 440.00,
    "b": 493.88,
}
print("Playing notes: {}".format(notes))
for note in notes:
    if note in NOTE_TO_FREQUENCY.keys():
        cpx.play_tone(NOTE_TO_FREQUENCY[note], 0.15)
