# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:10:18 2021

@author: Tanvy
"""

from PIL import Image

img = Image.open('../images/profile.jpg')

img.show()

imgGrey = Image.open('../images/profile.jpg').convert('L')

imgGrey.show()