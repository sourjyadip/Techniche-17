from time import sleep
import cv2
import serial

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

	flag = 0
	print("start writing")
	while(flag<4):
		k = input()
		if k == 's':
			ret,frame = cam.read()
			given = shape(frame)
			print(given)
			arduino.write('t'.encode('utf-8'))
			sleep(3)
			flag=flag+1
		

def shape(frame):

	
	 
	img=frame
	crop_img = img[0:480, 80:560]

	res = cv2.resize(img,(64,64), interpolation = cv2.INTER_CUBIC)
	gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(gray,127,255,1)

	_,contours,h = cv2.findContours(thresh,1,2)

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print(len(approx))
		
	        
		if len(approx)==3: 
			return "triangle"
	        
		elif len(approx)==4:
			thresh=0
			blur = cv2.GaussianBlur(gray,(5,5),0)
			edges = cv2.Canny(blur,thresh,thresh*2)
			
			# Image to draw the contours
			_,contours,hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
			flag=0
			for cnt in contours:
				x,y,w,h = cv2.boundingRect(cnt) 
				#print w
				#print h
				if(w>10 and h>10 and abs(w-h)<3):
					flag=1
					break
				elif(w>10 and h>10 and abs(w-h)>3):
					flag=0
					break
			if(flag==0):
				return "rectangle"
			elif(flag==1):
				return "square"
		elif len(approx) > 11:
			return "circle"
	        



if __name__=="__main__":
	main()