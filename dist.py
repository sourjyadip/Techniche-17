import cv2
import numpy as np 


cam = cv2.VideoCapture(1)

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
		# SPACE pressed
		img_name = "opencv_frame_{}.png".format(img_counter)
		cv2.imwrite(img_name, frame)
		print("{} written!".format(img_name))
		img_counter += 1
		img = cv2.imread(img_name)
		
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
		_,contours,hierarchy = cv2.findContours(img, 1, 2)
		'''cnt = contours[0]

		(x,y),radius = cv2.minEnclosingCircle(cnt)
		center = (int(x),int(y))
		radius = int(radius)
		cv2.circle(img,center,radius,(0,255,255),-1)'''
		height = np.size(img,0)
		
		width = np.size(img,1)
		x1=0
		x2=0
		print(height)
		print(width)
		hRange = (range(0,height))
		wRange = (range(0,width))
		for i in wRange:
			for j in hRange:
				r=img[j,i]
				if(r==0):
					x1=i
					break



		for k in range(width-1,0,-1):
			for l in range(height-1,0,-1):
				r=img[l,k]
				if(r==0):
					x2=k
					break
		p=x1-x2
		#cv2.imshow('img',img)

		
		w=10.5      #actual width
		f=716.57143 #tested value
		d=(f*w)/p
		print(d)
		cv2.waitKey(0)


cam.release()

cv2.destroyAllWindows()
