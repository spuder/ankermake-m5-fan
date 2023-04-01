#include <Arduino.h>

#define LED_PIN 1 // Define LED pin

void setup() {
  pinMode(LED_PIN, OUTPUT); // Set LED pin to output mode

  TCCR1 = _BV(CS10); // Set prescaler to 1
  TCCR1 |= _BV(PWM1A); // Set PWM mode for OCR1A

  OCR1A = 412; // Set PWM duty cycle to 50% (412 = 255 * 0.5 * 16.5 / 20)
}

void loop() {
  // Do nothing
}
