import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('cameraman.jpg', 0)

# Apply mean filter (3x3 kernel)
mean_filtered = cv2.blur(img, (3, 3))

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Mean Filtered Image")
plt.imshow(mean_filtered, cmap='gray')

plt.show()