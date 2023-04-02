import machine
import time

# Set up the PWM input on pin 2
pwm_in = machine.PWM(machine.Pin(2))

# Set the frequency of the PWM signal to 20 kHz
pwm_in.freq(20000)

while True:

    # Measure the duty cycle of the PWM signal on pin 2
    pwm_duty_cycle = pwm_in.duty_u16()
    print("PWM duty cycle on pin 2:", pwm_duty_cycle)

    # Measure the time period of the PWM signal on pin 2
    start_time = time.ticks_us()
    while pwm_in.duty_u16() == pwm_duty_cycle:
        pass
    end_time = time.ticks_us()
    time_period_us = end_time - start_time

    # Calculate the frequency of the PWM signal on pin 2
    pwm_frequency = 1000000 / time_period_us
    print("PWM frequency on pin 2:", pwm_frequency)

    # Wait for 1 second
    time.sleep(1)
