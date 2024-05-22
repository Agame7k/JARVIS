#define LIGHT_PIN 13

void setup() {
  // Initialize the digital pin as an output.
  pinMode(LIGHT_PIN, OUTPUT);
  // Start the serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read
  if (Serial.available()) {
    // Read the incoming data
    String command = Serial.readStringUntil('\n');

    // If the command contains {LGHT}, turn on the light
    if (command.indexOf("{LGHT}") >= 0) {
      digitalWrite(LIGHT_PIN, HIGH);
    }
  }
}