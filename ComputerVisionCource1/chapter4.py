import cv2
import numpy as np
#Shapes and Texts
# learn how to draw shapes on images and line and teext in images

#First we need create matrax // black = 0 // the size of our matraix = ( 512,512)
imag = np.zeros((512,512,3) , np.uint8)

#print(imag.shape)
# To color the complete image // imag[:] = to all image // 255,0,0 = blue
#imag[:] = 255,0,0
#imag[200:300,100:300] = 255,0,0

# To create line // cv2.line(image you want , start point = (0,0) , End point = (300,300) , color = (0,255,0) , Thickness = 3) // (0,255,0) = Green
#cv2.line(imag , (0,0) , (300,300) , (0,255,0) , 3 )
# imag.shape[1] = whaith // imag.shape[0] = Hiath
cv2.line(imag , (250,350) , (imag.shape[1],imag.shape[0]) , (0,255,0) , 3 )

#Rectangle
cv2.rectangle(imag , (0,0) , (250,350) , (0,0,255) , 2)
#cv2.rectangle(imag , (0,0) , (250,350) , (0,0,255) , cv2.FILLED)
# (0,0,255) = Read // cv2.FILLED = to filed the rectangle

#Circles
# center point = (400,50) // Radius = 30 // color = ( 255,255,0) // thickness = 5
cv2.circle(imag , (400,50) , 30 , (255,255,0) , 5)

#Text on images
# text you want show = " HMZ12 " // origin where we srart it = (300,100) // defind the fornt = cv2.FONT_HERSHEY_COMPLEX // Scale = 1 // color (0,150,0) // thickness = 2
cv2.putText(imag , " HMZ12 " , (300,200) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,150,0) , 2)



cv2.imshow("Image" , imag)

cv2.waitKey(0)
