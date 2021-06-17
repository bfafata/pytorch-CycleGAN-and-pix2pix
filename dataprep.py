#Made by Brandon Fafata for CMU Department of Computational Biology
# usage:
# python dataprep.py --densitymap_path ./path/to/densitymap/ --subtomogram_path ./path/to/subtomogram/ --resultfolder ./path/to/result/


import os
from PIL import Image
import os
import cv2
import numpy as np
import shutil
import time
import argparse
begin=time.time()
parser= argparse.ArgumentParser(description='Prepare data for pix2pix from AITOM')
parser.add_argument('--densitymap_path',
                       metavar='densitymap_path',
                       type=str,
                       default="./densitymap_png/",
                       help='the path to density map images')
parser.add_argument('--subtomogram_path',
                       metavar='subtomogram_path',
                       type=str,
                       default="./subtomogram_png/",
                       help='the path to subtomogram image')
parser.add_argument('--resultfolder',
                       metavar='resultfolder',
                       type=str,
                       default="./result/",
                       help='results stored here')
args = parser.parse_args()

densitymap_path=args.densitymap_path
subtomogram_path=args.subtomogram_path

resultfolder=args.resultfolder

tempfolder1="./temp1/"
temp_sliced_density="./tempd/"
temp_sliced_subtomogram="./temps/"

for folder in [resultfolder,tempfolder1,temp_sliced_density,temp_sliced_subtomogram]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

densitymap_list = [name for name in os.listdir(densitymap_path) if name.endswith('.png')]
subtomogram_list = [name for name in os.listdir(subtomogram_path) if name.endswith('.png')]

def norm_img(img):
    max_v = img.max()
    min_v = img.min()
    img = (img - min_v) / (max_v - min_v)
    return img*255

def convert_to_8bit(path,filename,destination):

    img_copy=cv2.imread(path,cv2.IMREAD_ANYDEPTH)
    img_copy=norm_img(img_copy)
    cv2.imwrite(destination+filename,img_copy)

def slicer(path,destination):

    img = Image.open(path)
    global mark
    for i in range(5):
        for j in range(6):

            region = img.crop((j*33, i*33, j*33 + 33, i*33 + 33))
            region = region.convert('L')
            region.save(os.path.join(destination,str(mark)+".png"))
            mark = mark + 1
    img.close()

def combine(patha,pathb,name,destination):

    width=33
    height=33

    inp=Image.open(patha)
    outp=Image.open(pathb)

    result = Image.new('L', (width*2, height)) #L is 8-bit black and white
    result.paste(inp, box=(0, 0))
    result.paste(outp, box=(width, 0))

    result.save(destination+image)
        
    inp.close()
    outp.close()

mark=0
print("Converting and slicing subtomograms..")
for image in subtomogram_list:
    convert_to_8bit(subtomogram_path+image,image,tempfolder1)
    slicer(tempfolder1+image,temp_sliced_subtomogram)
mark=0
print("Converting and slicing densitymaps..")
for image in densitymap_list:
    convert_to_8bit(densitymap_path+image,image,tempfolder1)
    slicer(tempfolder1+image,temp_sliced_density)

slicedlist=[name for name in os.listdir(temp_sliced_density) if name.endswith('.png')]
print("Combining...")
for image in slicedlist:
    combine(temp_sliced_density+image,temp_sliced_subtomogram+image,image,resultfolder)

for tempdir in [temp_sliced_subtomogram,temp_sliced_density,tempfolder1]:
    shutil.rmtree(tempdir)

print(f"Success. Executed in {time.time()-begin} seconds")
#It took my computer 13 seconds for 500 pairs of images