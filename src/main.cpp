// This should work, but it isn't working
// Aborting because while the digispark is perfect (can run on 24v with heatsync), its just too flakey


#include <Arduino.h>

const int PWM_PIN = 4;
const int PWM_FREQ = 20000; // PWM frequency in Hz

void setup() {
  // Set Phase Correct PWM mode for Timer0
  TCCR0A |= _BV(WGM00) | _BV(WGM01);
  
  // Set PWM frequency
  OCR0A = F_CPU / (2 * 2 * PWM_FREQ);
  
  // Enable PWM on pin 4
  DDRB |= _BV(PWM_PIN);
  TCCR0A |= _BV(COM0B1);
}


void loop() {
  // Alternate between 50% duty and 0% duty every 5 seconds
  static uint32_t last_toggle = 0;
  if (millis() - last_toggle >= 5000) {
    last_toggle = millis();
    if (OCR0B == 0) {
      OCR0B = 127;
    } else {
      OCR0B = 0;
    }
  }

  // Turn on LED on pin 1 when duty cycle is 50%
  if (OCR0B == 127) {
    digitalWrite(1, HIGH);
  } else {
    digitalWrite(1, LOW);
  }
}

