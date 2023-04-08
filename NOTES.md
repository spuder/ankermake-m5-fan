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

eps32 has better hardware PWM than esp8266
https://esphome.io/components/output/esp8266_pwm.html

## ESPHome

ESPHome has native support for writing PWM and there _might_ be a library for eading PWM


esphome clean config.yaml
esphome config config.yaml
esphome compile config.yaml
esphome upload --device /dev/cu.wchusbserial21140 config.yaml
esphome dashboard . --open-ui --address 127.0.0.1 --port 6053
esphome logs config.yaml --device /dev/cu.wchusbserial21140




### Wemos d2 mini

Doesn't work reliably with esphome. here this user couldn't get it working for PWM

https://community.home-assistant.io/t/wemos-s2-mini-doesnt-support-pwm/524560/5

https://github.com/esphome/esphome/pull/3264

https://community.home-assistant.io/t/wemos-s2-mini-doesnt-support-pwm/524560/2




# Hardware

## Digispark
- too unreliable

## Pi Pico
- too large
- not working with circuity python

### Pi Pico
- micropython only supports 1 timer, board has 2 timers
- hours and hours of GPT tring to read a PWM signal with no luck

### WaveShare RP2040-Zero

circuit python doesn't seem to have the fast enough PWM library
micropython is hard to get working
esphome doesn't register (it should work with the wireless version)

## AtMega 168/328

- Theoretically have dedicatd hardware for PWM 
- I don't have any small boards
- All the boards I have are 5V


## Arduino pro micro

- Should work with 20Khz by using register manipulation
- has 3 haredware timers
- I've tried 2 anc I can't get them to show up in arduino IDE, need reset? t

## ESP32-S3

- fast PWM
- expensive ($20 each)

## Wemos D1 mini

- Works well with ESPHome
- Maxes out at 1Khz PWM (might be fast enough for a fan? )


## STM32

### STM32F103C8T6

- works with 20khz


## Teensy
- expensive

## ESP32-C3

Can't find working configs for this board. 
esphome claims c3 has limited support

#-----------------------


Got the D1 mini S2 working
Had to use the cli and follow these steps
1. hold D0 button
2. press reset
3. release D0 button
