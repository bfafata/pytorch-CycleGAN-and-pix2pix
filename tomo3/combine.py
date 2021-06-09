from os import listdir
from PIL import Image
  
  
def pinjie():
 # 获取当前文件夹中所有JPG图像
 im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.png')]
 im_list1 = [Image.open("../densitymap_png"+fn) for fn in listdir() if fn.endswith('.png')]
 # 图片转化为相同的尺寸
 ims = []
 for i in im_list:
    new_img = i.resize((198, 198), Image.BILINEAR)
    width, height = new_img.size
    result = Image.new(new_img.mode, (width*2, height))
    result.paste(i, box=(0, 0))
    result.paste(im_list1[i], box=(width, 0))
    result.save('./new'+im_list)

 
  
  
if __name__ == '__main__':
 pinjie()