import cv2
import numpy as np
#Document Scanner
# The project not work because i had problem with me camera

########################################################
widthImg =640
heightImg = 480
########################################################


cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)

def perProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel =np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)

    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea =0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>5000:
            #cv2.drawContours(imgCount, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgCount, biggest, -1, (255, 0, 0), 3)
    return biggest


def getWarp(img,biggest):

    pts1 = np.float32(biggest)
    # we have defined the place of our four point
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    # our matrix the transformation matrix that will be required for the perspective itself // the points = (pts1 , pts2)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    # our output image based on this matrix
    imagOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    return imagOutput



while True:
    success, img = cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgCount = img.copy()

    imgThres = perProcessing(img)
    biggest=getContours(imgThres)
    print(biggest)
    imgWarped = getWarp(img, biggest)

    cv2.imshow("Result",imgWarped)
    if cv2.waitKey(1) & 0xFF ==ord('3'):
        break