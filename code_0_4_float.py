# =============================================== #
#   Lesson 0.4
#   float variables
# =============================================== #
import adafruit_thermistor
import board
thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)


temp_c = thermistor.temperature
temp_f = thermistor.temperature * 9 / 5 + 32
print("Temperature is: %f C and %f F" % (temp_c, temp_f))


# =============================================== #
# ^^ For now just focus on the code above this ^^
# =============================================== #