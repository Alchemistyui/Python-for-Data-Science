# %matplotlib inline
import numpy as np
from scipy import misc
import cv2
import matplotlib.pyplot as plt

# from skimage import data

img = cv2.imread('./wifire/sd-3layers.jpg')

print(type(img))
print(img.shape)


# plt.figure(figsize=(10,10))
# plt.imshow(img)
# plt.show()


print(img.size)
print(img.min(), img.max(), img.mean())


print(img[150, 250])
print(img[150, 250, 1])

# img[:200, :800, 1] = 255
# plt.figure(figsize=(10,10))
# plt.imshow(img)
# plt.show()

# low_value = img < 200
# img[low_value] = 0
# plt.figure(figsize=(10,10))
# plt.imshow(img)
# plt.show()


row_range = np.arange(len(img))
col_range = row_range
img[row_range, col_range] = 255
# plt.figure(figsize=(5,5))
# plt.imshow(img)
# plt.show()


# ------
img = cv2.imread('./wifire/sd-3layers.jpg')

origin = [int(img.shape[0]/2), int(img.shape[1]/2)]
# circle = img.where(, 0, 1)

X, Y =  np.ogrid[:img.shape[0], :img.shape[1]]
# print(X.shape, Y.shape)
# print(((X - origin[0])**2).shape)
# print(np.square(Y - origin[1]).shape)
distance = (X - origin[0]) ** 2 + np.square(Y - origin[1])
# print(distance.shape)
# print(distance[:50,:50])
circle = distance > np.square(int(img.shape[0]/2))
img[circle] = 0
# plt.figure(figsize=(5,5))
# plt.imshow(img)
# plt.show()

#  ----
img = cv2.imread('./wifire/sd-3layers.jpg')

half = X < origin[0]
mask = np.logical_or(half, circle)
img[mask] = 0
plt.figure(figsize=(5,5))
plt.imshow(img)
plt.show()








