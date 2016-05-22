import cv2
import numpy as np
import math

img = cv2.imread("14_1_cam.jpg")

img2 = cv2.imread("14_1_cam.jpg",0)
testimg = np.zeros(img.shape, img.dtype)
testimg[:,:] = (255,255,255)
testimg2 = np.zeros(img.shape, img.dtype)
testimg2[:,:] = (255,255,255)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
high_thresh, thresh_im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lowThresh = 0.5*high_thresh	
edges = cv2.Canny(gray,lowThresh,high_thresh,apertureSize = 3)
kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
#dilation = cv2.dilate(opening,kernel,iterations = 1)

gray = cv2.cvtColor(opening,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,lowThresh,high_thresh,apertureSize = 3)
dilation = cv2.dilate(edges,kernel,iterations = 1)

lines = cv2.HoughLinesP(edges,1,math.pi/2,2, None, 2, 1)
print len(lines)

line = {'x1':'', 'y1':'', 'x2':'', 'y2':''}
horizontal_lines = []
vertical_lines = []
count=0
for ar in lines:	
	if abs(ar[0][1]-ar[0][3])<30 and abs(ar[0][0]-ar[0][2])>0 :
		count+=1
		
		cv2.line(testimg,(ar[0][0],ar[0][1]),(ar[0][2],ar[0][3]),(0,0,255),1)
		
	if abs(ar[0][0]-ar[0][2])<2 and abs(ar[0][1]-ar[0][3])>10:
		
		cv2.line(testimg,(ar[0][0],ar[0][1]),(ar[0][2],ar[0][3]),(0,0,255),1)
		
print(count)
# print horizontal_lines


cv2.imshow("horizontal_lines", testimg)
cv2.waitKey(0)
cv2.imwrite("14hl.jpg",testimg)
cv2.imshow("edges", edges)
