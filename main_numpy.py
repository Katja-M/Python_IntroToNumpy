import cv2
import numpy

#Variable which holds image
# 0: image is read in gray scale; 1: image is read in RGB
im_g = cv2.imread('smallgray.png', 0)
# WE will get a three by five array, aka two-dimensional
# That corresponds to the image which has three row of pixels with 5 pixels in each row
print(im_g)

im_color = cv2.imread('smallgray.png', 1)
print(im_color)

# Creating an image out of a numpy array
cv2.imwrite('newsmallgray.png',im_g)

# Indexing, Slicing, Iterating of numpy arrays

# Getting the shape of the numpy array
print(im_g.shape)

# Getting the first two rows
print(im_g[0:2])
# Getting 'columns' in the array
print(im_g[0:2, 2:4])
# Getting only the specified columns
print(im_g[:,2:4])
# Getting a specific value
print(im_g[2,4])

# Iterating through a numpy array
for row in im_g:
    # prints each rows of the numpy array
    print(row)

for column in im_g.T:
    # Iterate through transposed array to access columns
    print(column)

for value in im_g.flat:
    # Iterates entry by entry
    print(value)

# Stacking and Splitting

# Stacking two arrays horizontally, input argument as tuple
im_hstacked = numpy.hstack((im_g, im_g))
# Stacking horizontally means that the row i of the first array adds all the columns of the second array in its row i
print(im_hstacked)
# Stacking two arrays vertically, input argument as tuple
im_vstacked = numpy.vstack((im_g, im_g))
# Stacking vertically is the equivalent to adding all rows of array2 to array1
print(im_vstacked)

# Splitting an array into smaller arrays
# Splitting array horizontally, second arguemnt is number of new arrays I want to have
im_hsplit = numpy.hsplit(im_g,5)
print(im_hsplit)
# Splitting array vertically
im_vsplit = numpy.vsplit(im_g, 3)
print(im_vsplit)