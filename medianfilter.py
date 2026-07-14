import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('cameraman.jpg', 0)

# Apply median filter (kernel size must be odd: 3, 5, 7...)
median_filtered = cv2.medianBlur(img, 3)

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Median Filtered Image")
plt.imshow(median_filtered, cmap='gray')

plt.show()