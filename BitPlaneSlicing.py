import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('cameraman.jpg', 0)

# Store bit planes
bit_planes = []

# Extract 8 bit planes (0 to 7)
for i in range(8):
    bit_plane = (img >> i) & 1   # Extract i-th bit
    bit_planes.append(bit_plane * 255)  # Scale to 0–255 for display

# Display original + bit planes
plt.figure(figsize=(10,8))

plt.subplot(3,3,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

# Show all 8 bit planes
for i in range(8):
    plt.subplot(3,3,i+2)
    plt.title(f'Bit Plane {i}')
    plt.imshow(bit_planes[i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()