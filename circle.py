# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:04:03 2020

@author: Admin
"""
#Grey scale image
import matplotlib.pyplot as plt
import numpy as np
m=256
n=256
r=20
img=np.zeros([m,n],dtype=np.uint8)
for i in range (0,m):
    for j in range(0,n):
        if (i-128)**2+(j-128)**2<(r**2):
            img[i,j]=255
plt.imshow(img,cmap='binary')


#Color Image

# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import random
# m=256
# n=256
# r=20
# img1=np.zeros([3,m,n],dtype=np.uint8)
# for i in range (0,m):
#       for j in range(0,n):
#           if (i-128)**2+(j-128)**2<(r**2):
#               x=random.randint(3)
#               img1[2,i,j]=90
#               img1[1,i,j]=245
#               img1[2,i,j]=0
              
# aa=np.transpose(img1, (1, 2, 0))              
# plt.imshow(aa)










