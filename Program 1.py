import numpy as np #numpy is fundamental package for computing in python
from PIL import ImageGrab #pil is Pillow package to get ImageGrab function
import cv2 #package of opencv
import time #package of counting and tracking time

last_time = time.time() #set initial last_time to be current time
while(True) :
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640))) #bounding box left x top y right x bottom y, get image whole screen resolution
 #   printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8')

    print('Loop took {} seconds'.format(time.time()-last_time)) #print the loop second, take the next time - previous time
    last_time = time.time() #take the next time as the current time

    cv2.imshow('Screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)) #show image on Screen

    if cv2.waitKey(1) & 0xFF == ord('q'): #wait "1" time, 0xFF return 8 bits others are 0, "ord" return ASCII value of the characters maximum 255
        cv2.destroyAllWindows()  #clear previous screen
        break