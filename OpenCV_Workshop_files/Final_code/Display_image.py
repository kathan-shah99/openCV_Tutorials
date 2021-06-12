"""
@author: kathan Shah

File-name : Display_image.py
"""
#-------------importing modules---------
import cv2
from matplotlib import pyplot as plt
#---------------------------------------

img1 = '/home/kathan/Desktop/OpenCV_Tutorial/Images/pyhton.png'

BGR = cv2.imread(img1,cv2.IMREAD_COLOR)		   # Image reading 

BGR_2_RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)     # RGB--> BGR

BGR_2_GRAY = cv2.cvtColor(BGR,cv2.COLOR_BGR2GRAY)   # BGR --> GRAY

BGR_2_HSV = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)     # BGR --> HSV

#---------------------------cv2.imshow()-------------------
cv2.imshow("HSV", BGR_2_HSV)
cv2.imshow("RGB", BGR)
cv2.imshow("Gray",BGR_2_GRAY)
#------------------------------matplotlib------------------------
"""
row = 1
col = 3

# showing image
fig = plt.figure()

fig.add_subplot(row,col,1)
plt.imshow(BGR_2_RGB)
plt.title("RGB")
plt.axis("off")

fig.add_subplot(row,col,2)
plt.imshow(BGR_2_GRAY,'gray')
plt.title("GRAY")
plt.axis("off")

fig.add_subplot(row,col,3)
plt.imshow(BGR_2_HSV)
plt.title("HSV")
plt.axis("off")
"""
