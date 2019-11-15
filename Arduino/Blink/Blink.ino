/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/
extern HardwareSerial Serial;

int value = 0;
const char LED_OFF = '0';
const char LED_ON =  '1';
const char LED_BLINK = '3';



// the setup function runs once when you press reset or power the board
void setup() {
  
  Serial.begin(9600);

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println("connection established! Waitting...");
}

int blink() {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(500);                       // wait for a second

  return 0;

}

// the loop function runs over and over again forever
void loop() {

  while (Serial.available())
  {
    value = Serial.read();
  }

  switch (value)
  {
    
  case LED_ON:
     digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    break;
  case LED_OFF:
     digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
     break;
  case LED_BLINK:
    blink();   // turn the LED on (HIGH is the voltage level)
     break;
  
  default:
    break;
  }

  delay(1000);                       // wait for a second
}
