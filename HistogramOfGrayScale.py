import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread('cameraman.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Display image
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display histogram
plt.subplot(1,2,2)
plt.plot(hist)
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()