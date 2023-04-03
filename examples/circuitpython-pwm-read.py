# Read a PWM signal
# Note that this isn't super accurate, especially with low duty cycles at high frequencies
# A better apporach is to use micropython with the PIO assemtpy


import board
import neopixel
import pulseio
import time

# Define the PWM input pin
led_pin = board.GP16
pwm_input_pin = board.GP3  # Replace with the appropriate pin you're using

num_leds = 1
pixels = neopixel.NeoPixel(led_pin, num_leds)


# Create a PulseIn object for reading PWM signals
pwm_reader = pulseio.PulseIn(pwm_input_pin, maxlen=2, idle_state=False)

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

def get_pwm_info(pwm_reader):
    if len(pwm_reader) < 2:
        return (None, None)
    pulse_high = pwm_reader[0]
    pulse_low = pwm_reader[1]
    pulse_total = pulse_high + pulse_low
    frequency = 1_000_000 / pulse_total
    duty_cycle = (pulse_high / pulse_total) * 100
    return (frequency, duty_cycle)

while True:
    time.sleep(0.1)  # Adjust the delay as needed

    if len(pwm_reader) == 2:
        frequency, duty_cycle = get_pwm_info(pwm_reader)
        if frequency and duty_cycle:
            # if frequency == 20000.00:
            pixels[0] = colors[int(duty_cycle / 10)]
            print("Frequency: {:.2f} Hz, Duty Cycle: {:.2f}%".format(frequency, duty_cycle))
        pwm_reader.clear()

## Note this code _mostly_ works, but sometimes get the frequency wrong
#Here is an example, where everything should read 20000
# Frequency: 14285.71 Hz, Duty Cycle: 50.00%
# Frequency: 32258.06 Hz, Duty Cycle: 51.61%
# Frequency: 20000.00 Hz, Duty Cycle: 70.00%
# Frequency: 14285.71 Hz, Duty Cycle: 50.00%
# Frequency: 20000.00 Hz, Duty Cycle: 80.00%
# Frequency: 12500.00 Hz, Duty Cycle: 50.00%
# Frequency: 47619.05 Hz, Duty Cycle: 47.62%
# Frequency: 20000.00 Hz, Duty Cycle: 80.00%
# Frequency: 50000.00 Hz, Duty Cycle: 50.00%
# Frequency: 20000.00 Hz, Duty Cycle: 80.00%