import cv2
#Face Detection

'''
#Image to Expline
imag = cv2.imread('Resource/facedetectionEx.png')
cv2.imshow("Example" , imag)
cv2.waitKey(0)
'''
faceCasacde = cv2.CascadeClassifier("Resource/haarcascade_frontalface_default.xml")
imag = cv2.imread('Resource/r9andzian.png')
imagGray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

# To find facec use Casacde
faces = faceCasacde.detectMultiScale(imagGray,1.1,4)
#To create Box aroun faces
for(x,y,w,h) in faces:
    cv2.rectangle(imag,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",imag)
cv2.waitKey(0)
