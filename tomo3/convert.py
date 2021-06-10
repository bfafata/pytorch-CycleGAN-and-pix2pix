#JPG turn to RGB565
#import os
#import sys
#import PIL
#from PIL import *
import PIL.Image as Image

import os
import re
import shutil
import cv2
import numpy as n

def norm_img(img):
    max_v = img.max()
    min_v = img.min()
    img = (img - min_v) / (max_v - min_v)
    return img*255
#import file


file1=r".\converted"
if not os.path.exists(file1):
    os.makedirs(file1)


pyname = [name for name in os.listdir() if name.endswith('.png')]
for imgname in pyname:
    print("converting", imgname)
    img_copy=cv2.imread(imgname,cv2.IMREAD_ANYDEPTH)
    img_copy=norm_img(img_copy)
    
    cv2.imwrite(os.path.join(file1,imgname),img_copy)

           