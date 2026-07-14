import cv2
img = cv2.imread("lena.jpg")
print(img.shape)
img_negative=255-img
print(img_negative.shape)
cv2.imshow("window",img_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()
