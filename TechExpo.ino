int rm1=6;
int rm2=7;
int lm1=8;
int lm2=9;
int r1=10;
int r2=11;
int l1=12;
int l2=13;
char a;
float x,first_read;


void setup() 
{
  Serial.begin(9600);
  pinMode(rm1,OUTPUT);
  pinMode(rm2,OUTPUT);
  pinMode(lm1,OUTPUT);
  pinMode(lm2,OUTPUT);
  pinMode(r1,OUTPUT);
  pinMode(r2,OUTPUT);
  pinMode(l1,OUTPUT);
  pinMode(l2,OUTPUT);
 
  first_read=analogRead(A0);      
}

void back()
{
  digitalWrite(rm1,HIGH);
  digitalWrite(rm2,LOW);
  digitalWrite(lm1,HIGH);
  digitalWrite(lm2,LOW);
}

void front()
{
  digitalWrite(rm1,LOW);
  digitalWrite(rm2,HIGH);
  digitalWrite(lm1,LOW);
  digitalWrite(lm2,HIGH);
}

void brake()
{
  digitalWrite(rm1,LOW);
  digitalWrite(rm2,LOW);
  digitalWrite(lm1,LOW);
  digitalWrite(lm2,LOW);
}

void right()
{
  digitalWrite(rm1,LOW);
  digitalWrite(rm2,HIGH);
  digitalWrite(lm1,HIGH);
  digitalWrite(lm2,LOW);
}

void left()
{
  digitalWrite(rm1,HIGH);
  digitalWrite(rm2,LOW);
  digitalWrite(lm1,LOW);
  digitalWrite(lm2,HIGH);
}

void clk()
{
  digitalWrite(arm1,HIGH);
  digitalWrite(arm2,LOW);  
}

void aclk()
{
  digitalWrite(arm2,HIGH);
  digitalWrite(arm1,LOW);  
}

void stop_rot()
{
  digitalWrite(arm2,LOW);
  digitalWrite(arm1,LOW);  
}

void loop() 
{
  if(Serial.available())//checking buffer
  {
    a = Serial.read();//reading buffer or from Rx(pin 0)
  }
  switch(a)
  {
    case 'f':front();
             break;
    case 'b':back();
             break;
    case 'l':left();
             break;
    case 'r':right();
             break;
    case 's':brake();
             break;
    case 'a':aclk();
             c=1;
             break;
    case 'c':clk();
             c=-1;
             break;
    case 'o':stop_rot();
  }
/*
  
  if(c>0)
  {
    aclk();
    if(c<100)
      c++;
    else
      c=(-1);
  }
  else if(c<0)
  {
    clk();
    if(c>(-100))
      c--;
    else
      c=1;
  }
*/
 /* 
  x=analogRead(A0);
  Serial.print(first_read);
  Serial.print("    ");
  Serial.println(x);
  if ((x-first_read)>20||(x-first_read)<(-20))
  {
    tone(8,400);
    digitalWrite(13,HIGH);
  }
  else
  {
  noTone(8);
  digitalWrite(13,LOW); 
  }*/
}
