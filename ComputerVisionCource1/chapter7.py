import cv2
import numpy as np
#Color Detection
# The color we need we keep it white and the color we do not need we keep it black

def empty(a):
    pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
path = 'Resource/purpleCar.png'

# "TrackBars" this name you chose you should put same in there function you call
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",116,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",136,179,empty)
cv2.createTrackbar("Set Min","TrackBars",32,255,empty)
cv2.createTrackbar("Set Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",44,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


# we have to put in loop to keep runing again and agin to get values
while True:
   imag = cv2.imread(path)

   imgHSV = cv2.cvtColor(imag,cv2.COLOR_BGR2HSV)
# To track the value // the spling have to be the same to which window you track(Ex:"Hue Min")
   h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
   h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
   s_min = cv2.getTrackbarPos("Set Min", "TrackBars")
   s_max = cv2.getTrackbarPos("Set Max", "TrackBars")
   v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
   v_miax= cv2.getTrackbarPos("Val Max", "TrackBars")

   print(h_min,h_max,s_min,s_max,v_min,v_miax)
   # will filter out and give us the filtered out image of that color
   lower = np.array([h_min,s_min,v_min])
   upper = np.array([h_max,s_max,v_miax])
   mask =cv2.inRange(imgHSV,lower,upper)
   # put two image togeter on one image // ( mask=mask ) = like our original image but with a mask applied
   imagResult = cv2.bitwise_and(imag,imag,mask=mask)


  # cv2.imshow("Purple", imag)
 #  cv2.imshow(" HSV", imgHSV)
  # cv2.imshow(" Mask", mask)
  # cv2.imshow(" Result", imagResult)


   imagStack = stackImages(0.6, ([imag, imgHSV], [mask, imagResult]))

   cv2.imshow("Stacked Images", imagStack)
   cv2.waitKey(1)