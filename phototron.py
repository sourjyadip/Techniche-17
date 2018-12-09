import cv2
import numpy as np


def main(): 
	cam = cv2.VideoCapture(2)

	cv2.namedWindow("test")

	img_counter = 0

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
	        shape(frame)

	cam.release()

	cv2.destroyAllWindows()

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
			print "star"
	        
		elif len(approx)==3: 
			print "triangle"
	        
		elif len(approx)==4:
			print "square"
	        
	    
		elif len(approx) > 11:
			print "circle"
	        



if __name__=="__main__":
	main()