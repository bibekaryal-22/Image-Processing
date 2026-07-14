import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lena.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(img_opening, cmap='gray')
plt.title('Opening'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(img_closing, cmap='gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])
plt.show()

