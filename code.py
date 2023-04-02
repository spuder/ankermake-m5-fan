import machine
import neopixel
import utime

# Set up the neopixel
np = neopixel.NeoPixel(machine.Pin(16), 1)

# Set up the fan control
fan_in = machine.PWM(machine.Pin(2))
fan_out = machine.PWM(machine.Pin(29))
fan_out.freq(20000)

# Define the duty cycles and colors
duty_cycles = [0, 3276, 6553, 9830] # 0%, 25%, 50%, 75%
colors = [(0, 255, 0), (0, 0, 255), (128, 0, 128), (255, 0, 0)] # green, blue, purple, red

# Initialize the time of the last PWM signal printout
last_print_time = 0

while True:

    # Cycle through the duty cycles and colors
    for i in range(4):

        # Set the duty cycle of the fan output
        fan_out.duty_u16(duty_cycles[i])

        # Check if at least one second has passed since the last printout
        current_time = utime.ticks_ms()
        if current_time - last_print_time >= 1000:
            # Read the PWM signal on pin 2 and print it out
            #pwm_signal = fan_in.duty_u16()
            #print("PWM signal on pin 2:", pwm_signal)
            # Update the time of the last printout
            print("PWM out: ", duty_cycles[i])
            last_print_time = current_time

            # Set the color of the neopixel
            #np[0] = colors[i]
            #np.write()

