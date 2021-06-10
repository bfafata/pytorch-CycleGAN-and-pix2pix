from os import listdir
from PIL import Image
  
  
def pinjie():
 # 获取当前文件夹中所有JPG图像
 #/
   width=33
   height=33
   im_list = [fn for fn in listdir("dmap") if fn.endswith('.png')]
   for i in im_list:
        inp=Image.open("dmap/"+i)
        outp=Image.open("stom/"+i)

        result = Image.new('L', (width*2, height)) #L is 8-bit black and white
        result.paste(inp, box=(0, 0))
        result.paste(outp, box=(width, 0))

        result.save('new/'+i)
        
        inp.close()
        outp.close()

 
  
  
if __name__ == '__main__':
 pinjie()