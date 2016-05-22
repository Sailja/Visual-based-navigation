from pyimagesearch.transform import four_point_transform
import cv2
import numpy as np
import argparse
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import math
#ask the user to double click on four points
print("Click on four corners")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())
image = mpimg.imread(args["image"])

im=plt.imread(args["image"])

#taking input from usser
ax = plt.gca()
fig = plt.gcf()
implot = ax.imshow(im)
coord=[]
def onclick(event):
    if event.xdata != None and event.ydata != None:
        coord.append((int(event.xdata), int(event.ydata)))
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
print(coord)
warped = four_point_transform(image, np.array(coord))

#taking input from usser
ax = plt.gca()
fig = plt.gcf()
implot = ax.imshow(im)
coor=[]

# show the original and warped images
plt.imshow(image),plt.show()
#cv2.imshow("Original", image)
plt.imshow(warped),plt.show()
#cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.imwrite('Q1a.jpg', warped) 
cv2.destroyAllWindows()
im=cv2.imread("Q1a.jpg",-1)
look=[(134, 307), (163, 311), (196, 313), (224, 314), (257, 316), (285, 317), (312, 318), (341, 318), (370, 320), (132, 319), (163, 320), (193, 322), (223, 322), (256, 324), (287, 327), (317, 327), (347, 329), (377, 329), (128, 330), (160, 329), (192, 332), (225, 333), (258, 334), (289, 336), (320, 339), (353, 339), (381, 340), (122, 340), (156, 339), (192, 342), (225, 342), (259, 345), (292, 346), (326, 346), (356, 349), (388, 349), (121, 351), (156, 353), (192, 353), (228, 355), (261, 356), (297, 357), (330, 360), (366, 360), (394, 362), (117, 362), (151, 362), (189, 366), (227, 367), (265, 368), (297, 371), (334, 371), (370, 373), (404, 373), (112, 376), (150, 379), (188, 379), (228, 380), (266, 381), (302, 381), (340, 384), (378, 385), (412, 384), (106, 390), (146, 393), (188, 391), (229, 393), (268, 396), (306, 397), (345, 398), (383, 398), (417, 399)]
print(len(look))
count=0
for i in range(1,im.shape[0],im.shape[0]//7):
	for j in range(1,im.shape[1],im.shape[1]//8):
		cv2.circle(im,(j-1,i-1), 0, (0,0,255), -1)
		cv2.imshow("vdsf",im)
		count+=1
cv2.imshow("dfsdfd",im)
cv2.waitKey(0)	
cv2.imwrite("cal.jpg",im)
print(count)
ox=[(0, 0), (31, 1), (69, 1), (105, 0), (144, 1), (182, 0), (223, 0), (264, 0), (305, 0), (1, 16), (31, 15), (69, 15), (104, 14), (144, 13), (182, 11), (223, 11), (265, 10), (305, 9), (1, 28), (33, 28), (69, 27), (106, 26), (143, 24), (182, 25), (224, 24), (265, 22), (305, 21), (0, 39), (33, 39), (70, 38), (106, 38), (144, 38), (183, 37), (223, 36), (266, 35), (305, 35), (0, 52), (34, 51), (69, 51), (107, 51), (144, 49), (184, 49), (225, 49), (267, 50), (305, 47), (0, 63), (34, 62), (70, 64), (106, 62), (145, 62), (185, 61), (226, 62), (267, 62), (305, 61), (0, 75), (34, 76), (70, 74), (106, 75), (146, 75), (186, 75), (227, 75), (268, 74), (306, 74), (0, 85), (33, 85), (71, 85), (108, 85), (146, 85), (186, 85), (227, 85), (270, 85), (306, 85)]
print(len(ox))
error=0
on=[]
for i in range(1,im.shape[0],im.shape[0]//7):
	for j in range(1,im.shape[1],im.shape[1]//8):
		on.append((j-1,i-1))
print(on)
for i in range(0,len(ox)):
	error+=math.sqrt((ox[i][0]-on[i][0])**2+(ox[i][1]-on[i][1])**2)
print(error)

	
