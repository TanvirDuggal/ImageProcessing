# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:58:21 2021

@author: Tanvy
"""

from PIL import Image
from pylab import *

im = array(Image.open('../images/profile.jpg'))
imshow(im)

pt = ginput(4)

print(pt)

show()