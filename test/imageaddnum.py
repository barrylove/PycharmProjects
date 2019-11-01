from PIL import Image,ImageDraw

def imageaddno():

    #打开图片
    im = Image.open("e:/1.bmp")

    #定义数字
    num = "99"

    #获取数字位置
    w,h = im.size
    print(w,h)

imageaddno()
