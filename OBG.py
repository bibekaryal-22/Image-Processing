import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('lena.jpg', 0)

# Define intensity range
A, B = 100, 200

# Create output image (all zeros → black background)
sliced = np.zeros_like(img)

# Apply slicing WITHOUT background
sliced[(img >= A) & (img <= B)] = 255

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(1,2,2)
plt.title("Slicing WITHOUT Background")
plt.imshow(sliced, cmap='gray')

plt.show()