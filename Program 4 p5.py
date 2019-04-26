import numpy as np 
from PIL import ImageGrab 
import cv2 
import time 
from Keypress import PressKey, ReleaseKey, A, D, S, W
import pyautogui

def draw_lines(img, lines) :
    try:
        for line in lines:
            coords = lines[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]),[255,255,255], 3)
    except:
        pass



def roi(img, vertices) : #cover unwanted region, only region of interest left
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_img) :
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 0)   #blur image after processed

    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]]) #region of interest in trapezium shape
    processed_img = roi(processed_img,[vertices])

    # edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, 20, 15)
    draw_lines(processed_img, lines)

    return processed_img


def main() :

    last_time = time.time() 
    while(True) :
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640))) 
        new_screen = process_img(screen)

        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time() 
        cv2.imshow('window', new_screen)


        if cv2.waitKey(1) & 0xFF == ord('q'): 
            cv2.destroyAllWindows()  
            break


main()