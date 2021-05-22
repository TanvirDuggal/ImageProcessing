# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 00:41:13 2021

@author: Tanvy
"""

from PIL import Image
from pylab import *

im = array(Image.open('../images/profile.jpg'))
imshow(im)

x = [100, 150, 200, 345]
y = [451, 121, 89, 87]

plot(x, y, 'r*')

plot(x[:2], y[:2], 'r')

plot(x[2:], y[2:], 'ks:')


show()