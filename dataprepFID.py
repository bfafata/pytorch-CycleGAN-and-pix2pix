#Made by Brandon Fafata for CMU Department of Computational Biology
# usage:
# python dataprepFID.py --imagespath ./path/to/images/ --path_real ./resultfolder/real --path_fake ./resultfolder/fake

import os
from PIL import Image
import shutil
import argparse
import time

parser= argparse.ArgumentParser(description='Prepare data from pix2pix test for FID')
parser.add_argument('--imagespath',
                       metavar='imagespath',
                       type=str,
                       help='path to test results. Should look somthing like ./results/experimentname/test_latest/images')
parser.add_argument('--path_real',
                       metavar='path_real',
                       type=str,
                       default="./real/",
                       help='result path for real images')
parser.add_argument('--path_fake',
                       metavar='path_fake',
                       type=str,
                       default="./fake/",
                       help='result path for fake images')
args = parser.parse_args()

imagespath=args.imagespath
path_real=args.path_real
path_fake=args.path_fake

for folder in [path_real,path_fake]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

imglist_real=[name for name in os.listdir(imagespath) if name.endswith("fake_B.png")]
imglist_fake=[name for name in os.listdir(imagespath) if name.endswith("real_B.png")]

def makeFolder(imglist,path):
    mark=0
    for item in imglist:
        img=Image.open(imagespath+item)
        img.save(path+str(mark)+".png")
        mark+=1
        if mark%10==0:
            print(f"{path}: Done {mark}/{len(imglist)}")
begin=time.time()
makeFolder(imglist_fake,path_fake)
print(f"executed fake in {time.time()-begin}")
begin=time.time()
makeFolder(imglist_real,path_real)
print(f"executed real in {time.time()-begin}")