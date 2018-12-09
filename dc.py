import RPi.GPIO as GPIO
import time

p1=13
p2=26
p3=18
p4=16
p5=20
p6=19

GPIO.setmode(GPIO.BOARD)

GPIO.setup(p1,GPIO.OUT)
GPIO.setup(p2,GPIO.OUT)
GPIO.setup(p3,GPIO.OUT)
GPIO.setup(p4,GPIO.OUT)
GPIO.setup(p5,GPIO.OUT)
GPIO.setup(p6,GPIO.OUT)

pwm1=GPIO.PWM(p3,100)
pwm2=GPIO.PWM(p6,100)

pwm1.start(0)
pwm2.start(0)

GPIO.output(p1,True)
GPIO.output(p2,False)
GPIO.output(p4,True)
GPIO.output(p5,False)

pwm1.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)

GPIO.output(p3,True)
GPIO.output(p6,True)

time.sleep(10)

GPIO.output(p3,False)
GPIO.output(p6,False)
