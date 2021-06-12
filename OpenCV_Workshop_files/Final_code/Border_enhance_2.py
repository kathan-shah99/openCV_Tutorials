"""
@author: kathan

file-name : "Border_enhance_2.py"

-"Car image"
-creating blank image
-Border extraction

"""
#------------------------------Importing modules-----------------
import cv2
import numpy as np
from matplotlib import pyplot as plt
#----------------------------------------------------------------


img1 = '/home/kathan/Desktop/OpenCV_Tutorial/Images/car.jpeg'

BGR = cv2.imread(img1,cv2.IMREAD_COLOR)

RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)
RGB_edit = RGB.copy()       #creating deep copy of original RGB image matrix

#-------------------empty-image-matrix---------------------
"""
dim = RGB.shape
length = dim[0]
width = dim[1]
channel = dim[2]
x = np.empty((length,width,channel))
x = x.astype(np.uint8)
#creating empty image matrix
#RGB_edit = x
"""
#------------------------------------------
#converting image into GRAY scale
GRAY = cv2.cvtColor(BGR,cv2.COLOR_BGR2GRAY)

#thresholding of GRAY scale image 
_,THRESHOLD = cv2.threshold(GRAY,170,255,cv2.THRESH_BINARY)


#finding contours list in image
contours,_ = cv2.findContours(THRESHOLD,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#drawing contours in oriignal image for border enhancing 
for cnt in contours:
    area = cv2.contourArea(cnt)     #finding area of each contours
    if area > 10:
        #drawinf one by one contours on oringal image
        RGB_edit = cv2.drawContours(RGB_edit, [cnt], 0, (0,0,0), 1)   
        
 
#---------------------------plotting images using matplotlib------------
rows = 1
col = 2

fig = plt.figure(figsize=(10, 100))

# Adds a subplot at the 1st position
fig.add_subplot(rows, col, 1)
# showing image
plt.imshow(RGB)
plt.axis('off')
plt.title('Original')
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, col, 2)
# showing image
plt.imshow(THRESHOLD,'gray')
plt.axis('off')
plt.title("border_enhanced")  
