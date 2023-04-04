## Digispark PWM

The digispark can only do 500Hz by default, you can up it to 1Khz on pins 1 and 4 (but not pin 0)

If you do increase the PWM you can't use `delay()`

http://digistump.com/wiki/digispark/tricks

## Pins

This micropython code claims not all pins support PWM equally

https://github.com/phoreglad/pico-MP-modules/tree/main/PWMCounter#pin-selection

>Pico hardware allows only odd numbered GPIOs to be used in counter mode. Some pins share the same PWM slice (see list below) and if they are used in counting mode at the same time the signal seen by counter is a logical OR of both inputs.

```
PWM slice	GPIOs
1	GP1, GP17
2	GP3, GP19
3	GP5, GP21
4	GP7, GP23
5	GP9, GP25
6	GP11, GP27
7	GP13, GP29
8	GP15
```

By this we should use different pins for differnt GPIOs


## Itterations

1. Digispark

Failed because too unreliable

2. Pico with circuit python

works, but duty cycle readings aren't accurate
chatgtp recomends using the PIO feature for more reliable measurements, PIO doesn't work in circuit python. 
micropython can do it with assembly code

3. Micropython



### Esp32

The ESP32 boards may be better because they can produce ISR-based PWM
they also are faster than a pi pico

It is even possible to use esp-home to do this which would be crazy awesome


## ESPHome

ESPHome has native support for writing PWM and there _might_ be a library for eading PWM