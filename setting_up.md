# Mu editor
This guide will use the Mu code editor. To get it set up follow the guide here: https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor

# Circuit Playground Express
Install the latest stable version of Circuit Python on your device. Follow the guide here: https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart

The code in this tutorial also relies on the `adafruit_circuitplayground` library but it's already built into the Circuit Python system image for this device so you don't need to do anything further. You are ready to go you should see `CIRCUITPY` drive now when you connect the device to a PC.

# Circuit Playground Bluefruit
Install the latest stable version of Circuit Python on your device. Follow the guide here: https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuitpython


Download the Circuit Python library bundle, unzip it and copy the required libraries to your device. Follow the guide here: https://learn.adafruit.com/adafruit-circuit-playground-bluefruit/circuit-playground-bluefruit-circuitpython-libraries

The specific libraries we need are:
- `adafruit_bus_device/`
- `adafruit_circuitplayground/`
- `adafruit_lis3dh.mpy`
- `adafruit_thermistor.mpy`
- `neopixel.mpy`

Note that the first 2 are directories, and the latter 3 are individual `mpy` files. 

If you follow the guide linked above it will instruct you to copy these plus a few extra modules for BLE and HID. You can go ahead and copies those extra ones as well if you want, or you can leave them out, either way. But you must copy the ones listed above.