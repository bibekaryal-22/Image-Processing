import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"lena.jpg",0)

if img is None:
    print("Image not found")
else:
    c = 255 / np.log(1 + np.max(img))
    log_img = c * np.log(1 + img)
    log_img = np.array(log_img, dtype=np.uint8)

    # Display side by side
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(log_img,cmap='gray')
    plt.title("Log Transformed")
    plt.axis("off")

    plt.show()