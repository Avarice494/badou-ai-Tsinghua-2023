import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
"""
cv2.imread
shape
np.zeros
cv2.imshow
"""
img = cv2.imread("lenna.png",flags=1)
# print(img)
h,w = img.shape[:2]

img_gray = np.zeros([h,w],dtype= img.dtype)


for i in range(h):
    for j in range(w):
        m = img[i,j]
        img_gray[i,j] = int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)

print(img_gray)

cv2.imshow("image show gray",img_gray)



""""
此处引入matplotlib 主要是用于结果排版

221 为2x2 第一个
"""
plt.subplot(221)
img = plt.imread("lenna.png")
plt.imshow(img)
print("---image lenna----")
print(img)


""""
cmap的意思是选择通道，即使有了值，也应该给出一个是那个通道的值

"""
plt.subplot(222)
plt.imshow(img_gray,cmap="gray")

img_tow = np.zeros([h,w],dtype=img.dtype)
for i in range(h):
    for j in range(w):
        if img_gray[i,j] >=126:
            img_tow[i,j] = 255
        else:
            img_tow[i,j] = 0

plt.subplot(223)
plt.imshow(img_tow,cmap="gray")


"""
rgb2gray 该函数的返回值是0-1之间的数，故用是否大于0.5来判断
"""
img_gray = rgb2gray(img)

print(img_gray[111,111])


plt.show()
