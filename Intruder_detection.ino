//ARDUINO CODE

#define LED 15

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');

    if (msg == "ALERT") {
      for(int i=0; i<6; i++){
        digitalWrite(LED, HIGH);
        delay(250);
        digitalWrite(LED, LOW);
        delay(250);
      }
    }
  }
}