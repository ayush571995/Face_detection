import numpy as np
import cv2
def nothing(x):
    pass

img=cv2.imread('path',0)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch='0 : OFF \n : ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while 1:
    cv2.imshow('image',img) 
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    else:
        r=cv2.getTrackbarPos('R','image')
        g=cv2.getTrackbarPos('G','image')
        b=cv2.getTrackbarPos('B','image')
        s=cv2.getTrackbarPos(switch,'image')
        if s==0:
            pass
        else:
            img[:]=[b,g,r]
cv2.destroyAllWindows()
