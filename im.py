# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:52:58 2020

@author: Admin
"""
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
# image = cv2.imread("amma.jpg", 1)

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# pixels = np.array(image)

# plt.imshow(pixels)
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread("amma.jpg")
plt.imshow(image)
plt.show()