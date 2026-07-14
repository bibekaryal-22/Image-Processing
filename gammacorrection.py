import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('lena.jpg')
img_normalized =image/255.0
gamma = 2.2 #>1.1 for darker image, <1.0 for brighter image
gamma_corrected = np.power(img_normalized, gamma)
gamma_corrected = np.uint8(gamma_corrected * 255)
cv2.imshow('Gamma Corrected Image', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

