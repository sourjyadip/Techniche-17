import cv2
import numpy as np

def main(): 
	cam = cv2.VideoCapture(1)

	cv2.namedWindow("test")

	img_counter = 0
	#prev="none"

	while True:
		ret, frame = cam.read()
		cv2.imshow("test", frame)
		if not ret:
			break
		k = cv2.waitKey(1)

		if k%256 == 27:
	        # ESC pressed
			print("Escape hit, closing...")
			break
		elif k%256 == 32:
			now=shape(frame)
			#if(prev=="triangle"):
				#now="rectangle"
			#elif(prev=="square"):
				#now="square"
			#prev=now
			print now

	cam.release()

	cv2.destroyAllWindows()

def shape(frame):

	
	 
	img=frame
	#img = img[0:480, 80:560]

	#res = cv2.resize(img,(128,128), interpolation = cv2.INTER_CUBIC)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(gray,127,255,1)
	cv2.imshow('thresh',thresh)

	_,contours,h = cv2.findContours(thresh,1,2)

	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print len(approx)
		
	        
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
				print w
				print h
				if(w>10 and h>10 and abs(w-h)<1):
					return "square"
					flag=1
					break
			if(flag==0):
				return "rectangle"
		elif len(approx) > 11:
			return "circle"
	        




if __name__=="__main__":
	main()
