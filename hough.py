#!/usr/bin/python
'''
This example illustrates how to use Hough Transform to find lines
Usage: ./houghlines.py [<image_name>]
image argument defaults to ../data/pic1.png
'''
import cv2
import numpy as np
import sys
import math

try:
    fn = sys.argv[1]
except:
    fn = "../data/pic1.png"
print __doc__
img=cv2.imread("17_1_cam.jpg",-1)
src = cv2.imread("17_1_cam.jpg",0)
high_thresh, thresh_im = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lowThresh = 0.5*high_thresh
print(lowThresh,high_thresh)
dst = cv2.Canny(src, lowThresh, high_thresh)
cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(cdst,kernel,iterations = 1)
im = cv2.bilateralFilter(dilation, 5, 17,17)
count=0
horizontal=[]
vertical=[]

if True: # HoughLinesP


    lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 20, np.array([]), 25, 10)
    a,b,c = lines.shape
    for i in range(a):
	if abs(lines[i][0][3]-lines[i][0][1])<25 and abs(lines[i][0][0]-lines[i][0][2])>0 :
		horizontal.append((lines[i][0][0], lines[i][0][1],lines[i][0][2], lines[i][0][3]))	
		count+=1
        	cv2.line(im, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
	elif(abs(lines[i][0][3]-lines[i][0][1])>0 and abs(lines[i][0][0]-lines[i][0][2])<10):
		vertical.append((lines[i][0][0], lines[i][0][1],lines[i][0][2], lines[i][0][3]))	
		count+=1
        	cv2.line(im, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
else:    # HoughLines
    print("sdfsdgag")
    lines = cv2.HoughLines(dst, 1, math.pi/180.0, 20, np.array([]), 50, 10)
    a,b,c = lines.shape
    for i in range(a):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0, y0 = a*rho, b*rho
        pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
        pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
        cv2.line(im, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
print(count)
print(horizontal)
print(vertical)

for (a,b,c,d) in horizontal:
	for (x1,y1,x2,y2) in horizontal:
		if ((x1-a)**2+(y1-b)**2<800  or ((x2-a)**2+(y2-b)**2<800)):
		
	
for (a,b,c,d) in horizontal:
	for (x1,y1,x2,y2) in vertical:
		if ((x1-a)**2+(y1-b)**2<800  or ((x2-a)**2+(y2-b)**2<800)):
			print("yes")
			for i in range (min(x1,x2),c+1):
				for j in range(0,max(b,d)):
					img[j][i]=(0,0,0)
			
		if (((x2-c)**2+(y2-d)**2<800) or ((x1-c)**2+(y1-d)**2<800)):
			print("no")
			for i in range (a,max(x1,x2)+1):
				for j in range(0,max(b,d)):
					img[j][i]=(0,0,0)
		if (a<100):
			for i in range (0,c+1):
				for j in range(0,max(b,d)):
					img[j][i]=(0,0,0)
		if (640-a)<100:
			for i in range (a,640):
				for j in range(0,max(b,d)):
					img[j][i]=(0,0,0)	
cv2.imwrite("17mask.jpg",img)
cv2.imwrite("17hl.jpg",im)	
cv2.imshow("source", img)
cv2.imshow("detected lines", im)
cv2.waitKey(0)

