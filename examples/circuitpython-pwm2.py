# Generate a 20khz 50% duty cycle PWM signal on pi pico on pin 2
# Read the PWM signal on pin 3 and print it out
# While this mostly works, it produces a fair amount of 
# flutter where it reads randomly between 40% and 60%
# This likely is because pulseio has limited time resolution

import pwmio
import pulseio
import board
import time

# Set up PWM output on GP2 (pin 3)
pwm_out = pwmio.PWMOut(board.GP2, frequency=20000, duty_cycle=32768)

# Set up PWM input on GP3 (pin 2)
pwm_in = pulseio.PulseIn(board.GP3, maxlen=2, idle_state=True)

while True:
    # Write 50% duty cycle to GP2 (pin 3)
    pwm_out.duty_cycle = 32768
    
    # Read duty cycle on GP3 (pin 2) and print it out
    time.sleep(0.1)
    
    if len(pwm_in) == 2:
        pulse_on = pwm_in[0]
        pulse_off = pwm_in[1]
        pwm_in.clear()
        period = pulse_on + pulse_off
        frequency = 1 / (period * 1e-6)
        duty_cycle = pulse_on / period * 65535
        if duty_cycle > 65535:
            duty_cycle = 65535
        print("PWM frequency: {} Hz, duty cycle: {:.1f}%".format(frequency, duty_cycle / 65535 * 100))
