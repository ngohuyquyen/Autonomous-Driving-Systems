import numpy as np 
from PIL import ImageGrab 
import cv2 
import time 
from Keypress import PressKey, ReleaseKey, A, D, S, W


def process_img(original_img) :
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


last_time = time.time() 
while(True) :
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640))) 
    new_screen = process_img(screen)
    print('down')
    PressKey(W)
    time.sleep(3)
    print('up')
    ReleaseKey(W)


    print('Loop took {} seconds'.format(time.time()-last_time)) 
    last_time = time.time() 
    cv2.imshow('window', new_screen)


#    cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        cv2.destroyAllWindows()  
        break