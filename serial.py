import serial
from time import sleep

arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1,xonxoff=0,rtscts=0)
sleep(3)
# Toggle DTR to reset Arduino
arduino.setDTR(False)
sleep(2)
# toss any data already received, see
# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
arduino.flushInput()
arduino.setDTR(True)

with arduino:
	print('ready to transmit data')
	while True:
		d = input()
		arduino.write(d.encode('utf-8'))
		print(arduino.read())



