#  Rotating and Adjusting Brightness
import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread("example.jpg")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# Rotate the image by 45 degrees around its center
(h,w)=image.shape[:2]
center=(w//2,h//2)
  # rotate by 45 degrees
m=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(image,m,(w,h))
rotated_rgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.show()
# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
