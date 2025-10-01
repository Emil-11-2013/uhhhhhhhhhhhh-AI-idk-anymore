# Color Conversions and Cropping
import cv2 
import matplotlib.pyplot as plt

image = cv2.imread('boy.png')    

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('RGB Image')
plt.show()


# Convert to Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow (image_gray, cmap='gray')
plt.title('Grayscale Image')
plt.show()


# Cropping the image
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
image_cropped = image[100:300, 200:400]
image_cropped1 = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2RGB)
plt.imshow(image_cropped1)
plt.title('Cropped Image')
plt.show()