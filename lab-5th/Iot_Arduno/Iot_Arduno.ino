// #include<SoftwareSerial.h>
int led =  A2;
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  
}

void loop() {
  if(Serial.available() > 0) {
  char c = (int) Serial.read();
  if(c == '1'){
    digitalWrite(led, HIGH);
    Serial.write("Light on\n");
    
  } else if(c == '0'){
    digitalWrite(led, LOW);
    Serial.write("Light off\n");
  }  
  }

}
