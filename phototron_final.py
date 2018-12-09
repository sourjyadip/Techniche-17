import cv2
import numpy as np
import serial
from time import sleep

def main():
	arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1,xonxoff=0,rtscts=0)
	sleep(3)
	# Toggle DTR to reset Arduino
	arduino.setDTR(False)
	sleep(2)
	# toss any data already received, see
	# http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
	arduino.flushInput()
	arduino.setDTR(True)
	cam = cv2.VideoCapture(1)

	k=cv2.waitKey(1)
	
	if k%256 == 32: #space pressed
		ret, frame = cam.read()
		given=shape(frame)

	flag=0
	c=cv2.waitKey(1)

	if k%256 == 32: #space pressed
		arduino.write('t'.encode('utf-8'))
	
		while(flag==0):
			d=arduino.read()
			if(d=='k'):
				ret, frame = cam.read()
				now=shape(frame)
				if(given==now):
					arduino.write('f'.encode('utf-8'))
					flag=1
				else:
					arduino.write('t'.encode('utf-8'))






def shape(frame):

	
	 
	img=frame
	crop_img = img[0:480, 80:560]

	res = cv2.resize(img,(64,64), interpolation = cv2.INTER_CUBIC)
	gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(gray,127,255,1)

	_,contours,h = cv2.findContours(thresh,1,2)

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print len(approx)
		if len(approx)==10:
			return "star"
	        
		elif len(approx)==3: 
			return "triangle"
	        
		elif len(approx)==4:
			return "square"
	        
	    
		elif len(approx) > 11:
			return "circle"
	        



if __name__=="__main__":
	main()