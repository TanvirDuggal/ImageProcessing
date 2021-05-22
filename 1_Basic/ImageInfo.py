# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:07:21 2021

@author: Tanvy
"""

import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('../images/profile.jpg')
# print(image)

print(np.shape(image))
print(type(image))
print(image.dtype)

plt.imshow(image)
plt.show()