# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:37:14 2021

@author: Tanvy
"""

from PIL import Image

img = Image.open('../images/profile.jpg')

newImg = img.resize((150,150))
newImg.show()

cropArea = (100,100,400,400)
cropImg = img.crop(cropArea)
cropImg.show()

rotateImg = img.rotate(45)
rotateImg.show()