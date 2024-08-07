import cv2
import numpy as np

#Basic Functions

img = cv2.imread("Resource/robot.png")
# ones = want all values to be  1 // (5,5) = size of Matrix // Type of object = (integer = uint8)
kernel = np.ones((5,5),np.uint8)
# Convert to Gray
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("real imge",img)
cv2.imshow("Gray Imahe", imgGray )
cv2.imshow("Blur Imahe", imgBlur )
cv2.imshow("Canny Imahe", imgCanny )
cv2.imshow("Dialation Imahe", imgDialation )
cv2.imshow("Eroded Imahe", imgEroded )


cv2.waitKey(0)
