 /*
 The circuit:


 * LCD RS pin to digital pin  12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
  * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin  to digital pin 2
 * LCD R/W pin to ground
 * LCD VSS pin to ground
 * LCD  VCC pin to 5V
 * LCD K pin to ground
 * LCD A pin to 5V
 * LCD V0 pin to  digital pin 6
 * LED to pin 13



 put a 110 ohm resitance in series  with the thermistor, the side of 110 resitance to 5V
 the side of the thermistor  to GND and the point where the thermistor and the resitence meet
 to analog input  A0
 */

#include <LiquidCrystal.h>
#include <stdlib.h>
#include <math.h>

LiquidCrystal  lcd(12,11,5,4,3,2);//configure the lcd

#define a A0 // analog input to read  the voltage of the thermistor
double R;
void setup() {
analogWrite(6,120);// configure the contrast of the lcd
lcd.begin(16,2);
Serial.begin(115200);//  using serial to send data to the computer
}

void loop() {
  R=analogRead(a);//  get the value in the A0
  float outR = sqrt(abs(0 + (100 - 0) * ((R - 1007) / (100 - 1007)))) * 10;
  Serial.println(outR);// send the temperature  in using serial

  // display the temperature in the lcd
  lcd.clear();
  lcd.print("Rot is: ");
  lcd.print(outR);
  lcd.print(" D");

  // trigger the security alarm if the temperature is higher than 60 degree
  if ((R)>60){
      digitalWrite(13,HIGH);
      delay(500);
      digitalWrite(13,LOW);
      delay(500);
  }
 else{
  delay(1000);
  }
  // in the both  cases there will be a delay of 1s between sending the temperature to the computer  and display in in the lcd
 }
