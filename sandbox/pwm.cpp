#include <Arduino.h>

#define LED_PIN 1 // Define LED pin

int dutyCycle = 0; // Initialize duty cycle variable
int counter = 0; // Initialize counter variable

void setup() {
  pinMode(LED_PIN, OUTPUT); // Set LED pin to output mode

  TCCR1 = _BV(CS10); // Set prescaler to 1
  TCCR1 |= _BV(PWM1A); // Set PWM mode for OCR1A
}

void loop() {
  counter++; // Increment the counter variable
  counter %= 32000; // Keep the counter variable within range (0 - 31999)

  if (counter == 0) { // Every 8 seconds (8 sec * 4000 iterations/sec = 32000 iterations)
    dutyCycle += 25; // Increase duty cycle by 25%
    if (dutyCycle > 75) { // Reset duty cycle to 0% after reaching 75%
      dutyCycle = 0;
    }
    OCR1A = (dutyCycle / 100.0) * 255; // Set PWM duty cycle based on the dutyCycle variable
  }
}
