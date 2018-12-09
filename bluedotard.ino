constexpr int LEFT_DIR = 13;
constexpr int LEFT_POWER = 11;
constexpr int enable1=5;
constexpr int enable2=7;
constexpr int RIGHT_DIR = 6;
constexpr int RIGHT_POWER = 2;

/*
    R1 --- R2
    |       |
    |       |
    |       |
    R1 --- R4
*/

void fwd()
{
    digitalWrite(enable1,HIGH);
    analogWrite(enable2,150);
    digitalWrite(LEFT_DIR, HIGH);
    digitalWrite(LEFT_POWER, LOW);
    digitalWrite(RIGHT_DIR, HIGH);
    digitalWrite(RIGHT_POWER, LOW);
   
}

void rev()
{
    digitalWrite(enable1,HIGH);
    analogWrite(enable2,150);
    digitalWrite(LEFT_DIR, LOW);
    digitalWrite(LEFT_POWER, HIGH);
    digitalWrite(RIGHT_DIR, LOW);
    digitalWrite(RIGHT_POWER, HIGH);
    
}

void stop()
{
   digitalWrite(enable1,LOW);
    analogWrite(enable2,0);
}
void turn()
{
  digitalWrite(enable1,HIGH);
    analogWrite(enable2,150);
  digitalWrite(LEFT_DIR,LOW);
  digitalWrite(LEFT_POWER,HIGH);
  digitalWrite(RIGHT_DIR,HIGH);
  digitalWrite(RIGHT_POWER,LOW);
  
}

void setup()
{
    pinMode(LEFT_DIR, OUTPUT);
    pinMode(LEFT_POWER, OUTPUT);
    pinMode(RIGHT_DIR, OUTPUT);
    pinMode(RIGHT_POWER, OUTPUT);
    pinMode(enable1,OUTPUT);
    pinMode(enable2,OUTPUT);
    
    Serial.begin(9600);
}

void loop()
{
  while (Serial.available()) {
    char s = Serial.read();
    
    if (s == 'f') {
      fwd();
    } else if (s == 'b') {
      rev();
    } else if (s == 's') {
      stop();
    }
    else if(s == 'l' || s=='r')
    {
      turn();
    }
    
    }
}

