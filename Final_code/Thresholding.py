"""
Created on Thu Jun  3 14:22:13 2021

@author: kathan Shah
"""


import cv2
from matplotlib import pyplot as plt

img = '/home/kathan/Desktop/OpenCV_Tutorial/Images/openCV.png'

BGR = cv2.imread(img,cv2.IMREAD_COLOR)

RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(BGR,cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(img_gray,160,255,cv2.THRESH_BINARY)


#------------------------------------using openCV-------------------------
cv2.imshow('Threshold',threshold)
cv2.imshow('original',BGR)
#-----------------------------------------------------------------------

#-------------------------------using matplotlib---------------------------
"""
fig = plt.figure(figsize=(10, 100))
row = 1
col = 2
# Adds a subplot at the 1st position
fig.add_subplot(row, col, 1)

# showing image
plt.imshow(RGB)
plt.axis('off')
plt.title("original")

# Adds a subplot at the 2nd position
fig.add_subplot(row, col, 2)
  
# showing image
plt.imshow(threshold,'gray')
plt.axis('off')
plt.title("Threshold")
"""
#-------------------------------------------------------------------
