import board
import neopixel
import time
import pwmio

# Define the pin that the LED is connected to
#led_pin = board.GP16
led_pin = board.GP23
# PWM
pwm_pin = board.GP2

# Define the number of LEDs and create a neopixel object
num_leds = 1
pixels = neopixel.NeoPixel(led_pin, num_leds)

# Define a list of colors to loop through
colors = [
    (0,0,0), #off
    (127, 0, 0),               # Red - 1000K
    (127, 64, 0),              # Orange - 2000K
    (127, 127, 0),             # Yellow - 3000K
    (96, 127, 0),              # Chartreuse - 4000K
    (0, 127, 0),               # Green - 5000K
    (0, 127, 127),             # Cyan - 7000K
    (0, 64, 127),              # Azure - 8000K
    (0, 0, 127),               # Blue - 9000K
    (64, 0, 127)               # Purple - 10000K
]

pwm = pwmio.PWMOut(pwm_pin, frequency=20000, duty_cycle=32768)

duty_cycle_percentage = 0

# Initialize duty cycle percentage
duty_cycle_percentage = 0

print("starting up on pi pico")
# Loop through the colors
while True:
    for color in colors:
        pixels[0] = color
        # Increase duty cycle by 10% every second
        duty_cycle_percentage += 10

        # Reset duty cycle to 0% if it goes over 100%
        if duty_cycle_percentage > 100:
            duty_cycle_percentage = 0
        print("Duty Cycle: {}%".format(duty_cycle_percentage))
        pwm.duty_cycle = int(duty_cycle_percentage / 100 * 65535)
        time.sleep(1)
