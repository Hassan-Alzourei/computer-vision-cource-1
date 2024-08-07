import cv2
import numpy as np
#Contours & Shape Detection

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
def getContours(imag):
    #to find details
    contours,hierarchy = cv2.findContours(imag,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # find all the area we are finding for each of what we call the shapes that we have detected
        area =cv2.contourArea(cnt)
        print(area)
        #To draw them so that we can see them clearly // -1 = the index we put to draw all shapes
        # To check the minimun area , will give it threshold
        if area>500:
            cv2.drawContours(imagContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor ==3: objectType = 'Tri'
            elif objCor ==4:
                aspRatio= w/float(h)
                if aspRatio >0.95 and aspRatio <1.05:objectType='square'
                else:objectType='Rectangle'
            elif objCor >4: objectType='Circles'
            else:objectType='None'

            cv2.rectangle(imagContour, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(imagContour,objectType ,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)





path = 'Resource/shapes.png'
imag = cv2.imread(path)
# copy the image
imagContour = imag.copy()

# Convert it into grayscale
imagGray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
imagBlur = cv2.GaussianBlur(imagGray,(7,7),1)

# To find the edges in our image
imagCanny = cv2.Canny(imagBlur,50,50)

imagBlank = np.zeros_like(imag)

getContours(imagCanny)


# put the image in one frame
imagStack = stackImages(0.8,([imag,imagGray,imagBlur] , [imagCanny,imagContour,imagBlank]))

cv2.imshow("Stack",imagStack)


cv2.waitKey(0)