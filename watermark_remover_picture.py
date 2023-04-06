from itertools import product
from PIL import Image


def remove_watermark(img_path='',rgb_sum = 0,dest_path=''):
    img = Image.open(img_path)
    width , height = img.size
    for pos in product(range(width),range(height)):
        if sum(img.getpixel(pos)[:3]) > rgb_sum:
            img.putpixel(pos,(255,255,255))
    img.save(dest_path)

if __name__ =='__main__':
    #获取水印像素点
    remove_watermark(img_path='/Users/didi/Desktop/711.jpeg',rgb_sum=515,dest_path='/Users/didi/Desktop/Wenya03.jpeg')


