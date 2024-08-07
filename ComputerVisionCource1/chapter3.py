import cv2
#Resizing and Cropping

"""
#OpenCV Convention
img = cv2.imread("Resource/chapter3(1).png")
cv2.imshow("Example",img)
cv2.waitKey(0)
"""    """
#Resizing 
#we ant resize the image (want know the size of imge)
imag =cv2.imread("Resource/Corolla2020.png")
# To find the size
# Display the waith and Hith of image
print(imag.shape)
# Resize the image and chose the waith and Hith of new image
imgResize = cv2.resize(imag,(1000,500))

print(imgResize.shape)

imgCropped = imag[0:100,200:250]

cv2.imshow("Image",imag)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0)
"""
#Cropping
# can be usful whan you want specific part of image
# to degined specific part we use matrax [Hith,Waith] the size of matrax is size of image
imag =cv2.imread("Resource/Corolla2020.png")
print(imag.shape)

imgCropped = imag[0:100,0:200]

cv2.imshow("Image",imag)

cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0)