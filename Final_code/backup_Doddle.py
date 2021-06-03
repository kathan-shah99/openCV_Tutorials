'''--------------------------------------------------------------------------

                                Author : Kathan Shah

                                File_name : backup_Doddle.py

--------------------------------------------------------------------------'''

#---------------------------------------------------
#importing modules required in program
import numpy as np
import cv2
#----------------------------------------------------

#start capturing video from camaera(number-0)
cap = cv2.VideoCapture(0)   #making class of capturing 

#Debugging Camaera
if not cap.isOpened():
    print("Can't open camera")
    exit()
#-----------------------------------------


#storage for all centroid detected
c = []
#--------------------------------------------

while True:
    #---------------------------------------------------------------
    # Capture frame-by-frame 
    ret, frame = cap.read()
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #-----------------------------------------------------------------
    #--------------------------Color Masking-------------------------
    
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    lower_red = np.array([50,100,100])
    upper_red = np.array([70,255,255])

    mask_red = cv2.inRange(HSV, lower_red, upper_red)

    after_mask = cv2.bitwise_and(frame,frame, mask= mask_red)
    gray_mask = cv2.cvtColor(after_mask,cv2.COLOR_BGR2GRAY)
    
    _,th = cv2.threshold(gray_mask,0,255,cv2.THRESH_BINARY)

    contours,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #center of all frame list
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.001*cv2.arcLength(cnt,True),True)
        if len(approx) > 20:
            if cv2.contourArea(cnt) >500:
                (cx, cy), radius = cv2.minEnclosingCircle(cnt)
                # convert all values to int
                center = (int(cx), int(cy))
                radius = int(radius)
                c.append(center)
                #and draw the circle in white
                #frame = cv2.circle(frame, center,radius, (255, 255, 255), 2)
    #-----------------------------------------------------------------
    #single color in frame
    for j in range(len(c)):
        frame = cv2.circle(frame, c[j],4, (255, 0, 0), 7)
    
    #---------------------------------------------------
    #Dual color in one frame 
    """
    for j in range(len(c)):
        if j < (len(c))/2:
            frame = cv2.circle(frame, c[j],4, (255, 0, 0), 7)
        else:
            frame = cv2.circle(frame, c[j],4, (0, 0, 255), 7)
    """
    #-----------------------------------------------------------------
    
    # Display the resulting frame
    cv2.imshow('frame',after_mask)          #masking Frame
    frame = cv2.flip(frame,1)               #rotating image BGR --> RGB
    cv2.imshow('oringal',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



