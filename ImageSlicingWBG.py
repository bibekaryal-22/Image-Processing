import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('lena.jpg', 0)

# Define intensity range
A, B = 100, 200

# WITH background slicing (copy original image)
sliced = img.copy()

# Highlight selected intensity range
sliced[(img >= A) & (img <= B)] = 255

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Slicing WITH Background")
plt.imshow(sliced, cmap='gray')

plt.show()