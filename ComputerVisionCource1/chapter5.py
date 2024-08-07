import cv2
import numpy as np

# Warp Prespective
# How to use Warp Prespective on image to get its bird

imag = cv2.imread("Resource/cards.png")

# 2.5 by 3.5 inches can aspect by ratio 250 by 350
width,height = 250,350
# first we want defined the our four comer points of the cards
pts1 = np.float32( [[1202,331] , [1522,580] , [871,739] , [1177,1022] ])
# we have defined the place of our four point
pts2 = np.float32( [[0,0] , [width, 0] , [0, height] , [width,height]])
#our matrix the transformation matrix that will be required for the perspective itself // the points = (pts1 , pts2)
matrix = cv2.getPerspectiveTransform(pts1 , pts2)
#our output image based on this matrix
imagOutput = cv2.warpPerspective(imag,matrix,(width,height))



cv2.imshow("Image" , imag)
cv2.imshow("Output" , imagOutput)


cv2.waitKey(0)