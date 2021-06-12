"""
Author : Kathan Shah

File_name : Video_capture.py
"""

import cv2

#create object for capturing video from camera-0
cap = cv2.VideoCapture(0)

#debugging camera (open or not)
if not cap.isOpened():
    print("Fail to capture")
    exit()

#continous capturing frome from capture class using (cap.read())
while True:
   #capture frame by frame 
   ret , frame =  cap.read()
   
   # if frame is read correctly ret is True
   if not ret:
        print("Can't receive frame")
        break
    
   cv2.imshow("Frame",frame)
   
   if cv2.waitKey(1) == ord('e'):
        break
    
cap.release()    	#release the captured frame object at end
cv2.destroyAllWindows()  
