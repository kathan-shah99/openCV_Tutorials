"""
@author: kathan

file-name : "color_masking_cube.py"

"""
#----------------Importing modules-----------------
import cv2
import numpy as np
from matplotlib import pyplot as plt
#----------------------------------------------------

img1 = '/home/kathan/Desktop/OpenCV_Tutorial/Images/Cube.png'

BGR = cv2.imread(img1,cv2.IMREAD_COLOR)           #image reading in BGR space

RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)	#BGR --> RGB
HSV = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)	#BGR --> HSV

lower_red = np.array([-10,100,100])     #lower-red HSV values
upper_red = np.array([10,255,255])      #higher-red HSV values

#finding pixels between lower_red & upper_red
mask_red = cv2.inRange(HSV, lower_red, upper_red)

#Bitwise AND opeartion with original(RGB) image for extracting RED color
after_mask = cv2.bitwise_and(RGB,RGB, mask= mask_red)


#---------------------------plotting images using matplotlib------------
rows = 1
col = 3

fig = plt.figure(figsize=(10, 100))

# Adds a subplot at the 2nd position
fig.add_subplot(rows, col, 1)
# showing image
plt.imshow(RGB)
plt.axis('off')
plt.title("RGB")
  
# Adds a subplot at the 2nd position
fig.add_subplot(rows, col, 2)
# showing image
plt.imshow(mask_red,'gray')
plt.axis('off')
plt.title("mask")

# Adds a subplot at the 3nd position
fig.add_subplot(rows, col, 3)
# showing image
plt.imshow(after_mask)
plt.axis('off')
plt.title("color_extraction")
plt.show()
