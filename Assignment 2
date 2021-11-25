/*Develop an "Automatic garage door opening system". Use an Ultrasonic sensor to detect if there is a vehicle in front of the garage. 
if any vehicle is detected open the garage door (rotate the servo motor) for some time and close it.*/
//Code for Automated Garage Gate
#include<Servo.h>
Servo myservo;
int pos=0;
int trig=5;
int eco=4;
int time;
int dist;
void setup()
{
  myservo.attach(6);
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(eco,INPUT);
  myservo.write(0);
}

void loop()
{
  digitalWrite(trig,1);
  delayMicroseconds(10);
  digitalWrite(trig,0);
  time=pulseIn(eco,1);
  dist=(time*0.034)/2;
  Serial.println(dist);
  delay(1000);
  if(dist<100){
    for(pos=0;pos<=90;pos++){
      myservo.write(pos);
      delay(20);
    }
    Serial.println("Gate Open");
    delay(10000);
    for(pos=90;pos>=0;pos--){
      myservo.write(pos);
      delay(20);
    }
    Serial.println("Gate Closed");
  }
}
