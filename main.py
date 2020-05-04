import cv2

#Variable which holds image
# 0: image is read in gray scale; 1: image is read in RGB
im_g = cv2.imread('smallgray.png', 0)
# WE will get a three by five array, aka two-dimensional
# That corresponds to the image which has three row of pixels with 5 pixels in each row
print(im_g)