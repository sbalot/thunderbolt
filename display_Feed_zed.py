# This program captures live feed from Zed camera and displays the feed as
# images after saving them
#
#
#
# Created by loopyunicorn, 29 Sept 2016
#
#Reference: https://www.youtube.com/watch?v=v30XjzzeAS4

import cv2
import numpy as np

capture= cv2.VideoCapture(0)                    #0 for ZED cam 
print('Press Esc key for exit')
#open loop while cam is connected
while (capture.isOpened()):
    #BGR image feed from camera
    ret,img=capture.read()
    cv2.imshow('output',img)                    #display BGR image captured
    #BGR to grayscale conversion
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #Convert color to gray scale
    cv2.imshow('black & white',img2)            #display grayscale image
    k=cv2.waitKey(10)                           # Press esc for exit
    if k==27:
        break
capture.release()
cv2.destroyAllWindows()
