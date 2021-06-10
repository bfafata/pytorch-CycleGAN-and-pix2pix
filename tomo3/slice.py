# 导入相关的库
from PIL import Image
# 打开一张图

# 图片尺寸
import cv2
import os

file1=r".\qie"
if not os.path.exists(file1):
    os.makedirs(file1)
pyname = [name for name in os.listdir() if name.endswith('.png')]
mark = 0
for imgname in pyname:
    print("slicing",imgname)
    img = Image.open(imgname)
    for i in range(5):
        for j in range(6):
            # 开始截取
            region = img.crop((j*33, i*33, j*33 + 33, i*33 + 33))
            region = region.convert('L')
            # 保存图片
            region.save(os.path.join(file1,str(mark)+".png"))
            mark = mark + 1