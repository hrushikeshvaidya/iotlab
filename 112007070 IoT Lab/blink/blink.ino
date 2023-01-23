void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  float reading = analogRead(A0);
  Serial.println(reading);
  delay(100);
}
