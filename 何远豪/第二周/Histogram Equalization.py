import cv2
import matplotlib.pyplot as plt

img =cv2.imread("lenna.png",1)

# 灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#直方图
dst = cv2.equalizeHist(gray)
# hist = cv2.calcHist([dst],[0],None,[256],[0,256])

plt.subplot(221)
plt.hist(dst.ravel(),256)
plt.show()

cv2.imshow("fa",gray)

img =cv2.imread("lenna.png",1)

(b,g,r) = cv2.split(img)

bh = cv2.equalizeHist(b)
gh = cv2.equalizeHist(g)
rh = cv2.equalizeHist(r)

req = cv2.merge((bh,gh,rh))

cv2.imshow("all",req)
cv2.waitKey()



