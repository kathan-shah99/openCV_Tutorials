"""
@author: kathan

file-name : "Border_enhancing_1.py"
"""

import cv2
from matplotlib import pyplot as plt

img1 = '/home/kathan/Desktop/OpenCV_Tutorial/Images/sinchen_1.jpeg'

BGR = cv2.imread(img1,cv2.IMREAD_COLOR)

RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)
RGB_edit = RGB.copy()       #creating deep copy of original RGB image matrix

#converting image into GRAY scale
GRAY = cv2.cvtColor(BGR,cv2.COLOR_BGR2GRAY)

#thresholding of GRAY scale image 
_,THRESHOLD = cv2.threshold(GRAY,127,255,cv2.THRESH_BINARY)


#finding contours list in image
contours,_ = cv2.findContours(THRESHOLD,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#drawing contours in oriignal image for border enhancing 
for cnt in contours:
    area = cv2.contourArea(cnt)     #finding area of each contours
    if area > 500:
        #drawinf one by one contours on oringal image
        RGB_edit = cv2.drawContours(RGB_edit, [cnt], 0, (0,255,255), 2)   
        
 
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
plt.imshow(RGB_edit)
plt.axis('off')
plt.title("border_enhanced")  
