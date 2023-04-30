from PIL import Image, ImageDraw, ImageFont
from termcolor import colored
def n1():
    pic1 = 'pic/postcard.jpg'
    with Image.open(pic1) as img:
        img.load()
    img_cr = img.crop((655, 515, 1200, 1197))
    # img_cr.show()
    img_cr.save('pic/croppostcard.jpg')
# n1()
def n2():
    p={1:'pic/ng.jpg',2:'pic/dr.jpg',3:'pic/8m.jpg',4:'pic/m.jpg'}
    print('1 - Новый год\n'
          '2 - День рождения\n'
          '3 - 8 марта\n'
          '4 - День матери\n')
    anv=int(input('Для получения открытки введите число - номер прадника: '))
    p1=p[anv]
    with Image.open(p1) as img:
        img.load()
    img.show()
# n2()
def n3():
    pic1 = 'pic/postcard.jpg'
    name = input('Введите имя: ')
    with Image.open(pic1) as img:
        img.load()
    # font = ImageFont.truetype("arial_bold.ttf", 50)
    # font = ImageFont.truetype("ofont.ru_Blue Curve.ttf", 50)
    font = ImageFont.truetype("ofont.ru_Maki Sans.ttf", 50)

    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        # сверху
        # (img.width // 2 - 100, 15),
        # в ценрте
        # (img.width // 2 - 100, 600),
        # снизу
        (img.width // 2 - 100, 1100),
        name+", поздравляю!",
        font=font,attrs=['bold'],
        # черный цвет
        fill=('#000000')
        # розовый цвет
        # fill=('#FF00E5')
        # желтый цвет
        # fill = ('#F9E10A')
    )
    img.show()
    img.save(name + "_postcard.png")
n3()
