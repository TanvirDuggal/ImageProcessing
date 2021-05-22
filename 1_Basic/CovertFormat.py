# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:25:04 2021

@author: Tanvy
"""

import os
from PIL import Image

files = ['../images/profile.jpg', '../images/moon.jpg']

for file in files:
    outfile = '../images/'+file.split('/')[2].split('.')[0] + '.png'
    print(outfile)
    try:
        Image.open(file).save(outfile)
    except Exception as e:
        print("error")
        print(e)
        