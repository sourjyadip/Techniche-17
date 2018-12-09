const int p1=11;
const int p2=6;
const int p3=12;
const int p4=13;

void setup() {
  pinMode(p1,OUTPUT);
  pinMode(p2,OUTPUT);
  pinMode(p3,OUTPUT);
  pinMode(p4,OUTPUT);
 Serial.begin(9600);

}

void rn()
{
  digitalWrite(p1,HIGH);
  digitalWrite(p2,LOW);
  digitalWrite(p3,HIGH);
  digitalWrite(p4,LOW);
  
}
void stp()
{
  digitalWrite(p1,LOW);
  digitalWrite(p2,LOW);
  digitalWrite(p3,LOW);
  digitalWrite(p4,LOW);
}
void bck()
{
  digitalWrite(p1,LOW);
  digitalWrite(p2,HIGH);
  digitalWrite(p3,LOW);
  digitalWrite(p4,HIGH);
  
}
void turn()
{
  digitalWrite(p1,HIGH);
  digitalWrite(p2,LOW);
  digitalWrite(p3,LOW);
  digitalWrite(p4,HIGH);
  
}

void loop() {
 
rn();
delay(1000);
bck();
delay(1000);
stp();
delay(1000); 

 
}
