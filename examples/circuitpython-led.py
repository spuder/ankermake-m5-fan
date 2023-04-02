import board
import neopixel
import time

# Define the pin that the LED is connected to
led_pin = board.GP16

# Define the number of LEDs and create a neopixel object
num_leds = 1
pixels = neopixel.NeoPixel(led_pin, num_leds)

# Define a list of colors to loop through
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Loop through the colors
while True:
    for color in colors:
        pixels[0] = color
        time.sleep(0.5)
