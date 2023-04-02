# loop through all the colors
# Requires micropython

import machine
import neopixel
import utime

# Set up the neopixel
np = neopixel.NeoPixel(machine.Pin(16), 1)

# Define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Cycle through the colors every second
while True:
    np[0] = RED
    np.write()
    utime.sleep(1)

    np[0] = GREEN
    np.write()
    utime.sleep(1)

    np[0] = BLUE
    np.write()
    utime.sleep(1)
