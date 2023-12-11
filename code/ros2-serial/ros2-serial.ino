#include <SoftwareSerial.h>

uint8_t send_data[32];
uint8_t receive_data[32];

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  for (int a = 0; a < 32; a++) send_data[a] = a;
  Serial.write(send_data, 32);

  //delay(100);  

  if (Serial.available() >= 32) {
    Serial.readBytes(receive_data, 32);

    if (receive_data[0] >= 2 && receive_data[0] <= 8) {
      digitalWrite(LED_BUILTIN, HIGH);
    } else {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
