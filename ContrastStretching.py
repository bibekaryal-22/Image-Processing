import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("lena.jpg", 0)

# Get minimum and maximum intensity values
r_min = np.min(img)
r_max = np.max(img)

# Apply contrast stretching formula
L = 255  # for 8-bit image

stretched = ((img - r_min) / (r_max - r_min)) * (L - 1)

# Convert to unsigned 8-bit integer
stretched = np.array(stretched, dtype=np.uint8)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Contrast Stretched Image", stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()