import cv2

#print("Package Imported")

#How to open Image
"""
img = cv2.imread("Resource/robot.png")
cv2.imshow("Output",img)
cv2.waitKey(0)
"""

# How to open video

# To import the video
"""
cap = cv2.VideoCapture("Resource/test_video.mp4")
# We need WHILE loop to display each fram
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    # break the loop wan you clik q in keybord
    if cv2.waitKey(1) & 0xFF ==ord('2'):
        break
"""

# To open the Webcame
"""
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
    cv2.imshow("Video",img)
    # break the loop wan you clik q in keybord
    if cv2.waitKey(1) & 0xFF ==ord('3'):
        break
"""