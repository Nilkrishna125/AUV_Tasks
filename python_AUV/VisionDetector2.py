import cv2 as cv
import numpy as np
class VisionDetector:
    def __init__(self):
        self.shapes={"Circle":0,"Triangle":0,"Square":0}
    def shape(self,frame):
        imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        
        cv.imshow('string',thresh)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            # print(contour)
            pixel=frame[contour[0][0][1],contour[0][0][0]]
            print(len(contour))
            b=pixel[0]
            g=pixel[1]
            r=pixel[2]
            if(b==0 and g==0 and r==0):
                print("black")
            elif(r>b and r>g):
                print("red")
            elif(g>r and g>b):
                print("green")
            elif(b>g and b>r):
                print("blue")
            else:
                print("white")
            print(contour)
        print(len(contours))
        print(len(hierarchy[0]))

        x=len(hierarchy[0])
        for i in range(1,x):
            k=0
            for j in range(1,x):
                if(i==j):
                    continue
                
                if(hierarchy[0][i][3]==j):
                    if(abs(cv.contourArea(contours[i])-cv.contourArea(contours[j]))<10000):
                        k=1
                        break
            if(k==1):
                continue
            y=contours[i]
            epsilon = 0.01*cv.arcLength(y,True)
            approx=cv.approxPolyDP(y,epsilon,True)
            if(cv.contourArea(approx)<300):
                continue
            cv.drawContours(frame, [approx], -1, (0, 255, 0), 3)
            l=len(y)
            if(l>10):
                print("circle")
            elif(l==3):
                print("Trinagle ")
            elif(l==4):
                print("Square ")
        
        cv.imshow('contours',frame)
    


V1=VisionDetector()
frame=cv.imread('/home/nilkrishna/Pictures/Screenshots/Screenshot from 2025-01-16 00-18-37.png')


if frame is None:
    raise FileNotFoundError("image uploading error")
     

V1.shape(frame)

cv.waitKey(0)
cv.destroyAllWindows()
