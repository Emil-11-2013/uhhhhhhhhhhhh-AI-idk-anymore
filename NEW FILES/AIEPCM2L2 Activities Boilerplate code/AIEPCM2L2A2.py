#  Rotating and Adjusting Brightness
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('boy.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Rotate the image by 45 degrees around its center
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightened = cv2.add(rotated, (50, 50, 50, 0))
brightened_rgb = cv2.cvtColor(brightened, cv2.COLOR_BGR2RGB)
plt.imshow(brightened_rgb)
plt.title('Rotated and Brightened Image')
plt.show()