#include <GyverMAX7219.h>

#define AM_W 32  // 4 matrices (32 leds)
#define AM_H 8

MAX7219<4, 1, 14, 16, 15> mtrx; // 4x1 matrix, CS pin is 14, DATA pin is 16 (MOSI), CLK pin is 15

void setup() {
  mtrx.begin();  // Initialize the matrix
  mtrx.setBright(0);  // Set initial brightness to minimum
}

void loop() {
  mtrx.clear(); // Clear the matrix
  mtrx.setBright(255);  // Set the brightness
  
  // Turn on LEDs based on potentiometer values
  for (int i = 0; i <= 20; i++) {
    for (int j = 0; j <= 6; j++) {
      mtrx.dot(i, j, true); // Turn on the dot at (i, j)
    }
  }
  mtrx.update();  // Update the display with the changes
  delay(100);  // Small delay to make changes noticeable
}
