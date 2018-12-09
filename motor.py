import RPi.GPIO as GPIO
import time

GPIO.setmode(GIO.BOARD)

p1=23
p2=24
p3=25
p4=2

GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT) 
GPIO.setup(p4, GPIO.OUT)

GPIO.output(p1,GPIO.HIGH)
GPIO.output(p2,GPIO.LOW)
GPIO.output(p3,GPIO.HIGH)
GPIO.output(p4,GPIO.HIGH)

time.sleep(5)

GPIO.output(p1,GPIO.LOW)
GPIO.output(p2,GPIO.LOW)
GPIO.output(p3,GPIO.LOW)
GPIO.output(p4,GPIO.LOW)


