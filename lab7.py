from PIL import Image, ImageFilter
def n1():
    pic1='pic/izo.jpg'
    with Image.open(pic1) as img:
        img.load()

    img.show()
    w, h = img.size
    f=img.format
    m=img.mode
    print('Высота',h)
    print('Ширина',w)
    print('Формат',f)
    print('Цветовая модель',m)
# n1()

def n2():
    pic1 = 'pic/izo.jpg'
    with Image.open(pic1) as img:
        img.load()
    pic2=img.reduce(3)
    pic2.save('pic/izo-3.jpg')
    pic3=img.transpose(Image.FLIP_LEFT_RIGHT)
    pic3.save('pic/izo-flipleft.jpg')
    pic4=img.transpose(Image.FLIP_TOP_BOTTOM)
    pic4.save('pic/izo-fliptop.jpg')
# n2()

def n3():
    pics = ['1.jpg', '2.jpg','3.jpg','4.jpg','5.jpg']
    for pic in pics:
        with Image.open(pic) as img:
            img.load()
            new_pics=img.filter(ImageFilter.FIND_EDGES)
            # new_pics.show()
            new_pics.save('new_'+pic)
# n3()
def n4():
    pic1 = 'pic/izo.jpg'
    log='pic/log.jpg'
    with Image.open(pic1) as img:
        img.load()
    with Image.open(log) as img1:
        img1.load()
    img_logo = img1.convert("L")



    img_logo = img_logo.filter(ImageFilter.CONTOUR)
    img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
    # img_logo.show()
    img.paste(img_logo, (480, 160), img_logo)
    img.show()
# n4()
