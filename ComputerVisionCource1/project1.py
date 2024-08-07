import cv2
import numpy as np
#Virtual Paint


# The list of colors we want to detect // ylow - bing - green
myColors = [[0,10,255,44,177,255],
            [149,7,103,150,79,255],
            [41,22,61,157,83,255]]
# we take value of colors (BGR) from web (https://www.rapidtables.com/web/color/RGB_Color.html)
mycolorValues = [[255,255,0],
                 [255,0,127],
                 [51,255,51]]
myPoints =[] ## [x ,y , colorId]

# To find color // chapter7
def findColor(imag,myColors,mycolorValues):
    imgHSV = cv2.cvtColor(imag, cv2.COLOR_BGR2HSV)
    cont = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getContours(mask)
        cv2.circle(imagResult,(x,y),10,mycolorValues[cont],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,cont])
        cont +=1
        #cv2.imshow(str(color[0]), mask)
    return newPoints

# chapter8
def getContours(imag):
    contours,hierarchy = cv2.findContours(imag,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imagResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imagResult,(point[0],point[1]),10,mycolorValues[point[2]],cv2.FILLED)






# To open the Webcame // chapter1

# in filed path we Id of camra here we use 0 to the defualt camra but when i have more than 1 i can write id of camra same as 1
cap = cv2.VideoCapture(0)
#Whith
cap.set(3,640)
#Hight
cap.set(4,480)
#brightness
cap.set(10,100)

# We need WHILE loop to display each fram
while True:
    success, img = cap.read()
    imagResult = img.copy()
    newPoints = findColor(img, myColors,mycolorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,mycolorValues)

    cv2.imshow("Video",imagResult)
    # break the loop wan you clik q in keybord
    if cv2.waitKey(1) & 0xFF ==ord('3'):
        break
