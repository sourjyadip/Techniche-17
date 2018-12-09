import cv2
import numpy as np
    
    
def shape(img):

    thresh=0
     

    #img = img[0:480, 80:560]

    #res = cv2.resize(img,(64,64), interpolation = cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
                    return "square"
                    flag=1
                    break
                elif(w>10 and h>10 and abs(w-h)>3):
                    flag=0
                    break
            if(flag==0):
                return "rectangle"
        elif len(approx) > 11:
            return "circle"
            



img=cv2.imread("square.jpg")
sh=shape(img)
print sh


