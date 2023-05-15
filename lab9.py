from PIL import Image, ImageFilter
from pathlib import Path
def n1():
    # pics = ['1.jpg', '2.jpg','3.jpg','4.jpg','5.jpg']
    current_dir = Path.cwd()
    pics = Path(current_dir).glob('*')
    Path('new_dir').mkdir(parents=True, exist_ok=True)
    for pic in pics:
        with Image.open(pic) as img:
            img.load()
            new_pics=img.filter(ImageFilter.FIND_EDGES)
            # new_pics.show()
            new_pics.save(Path('new_'+str(pic)))
# n1()
def n2():
    # pics = ['1.jpg', '2.jpg','3.jpg','4.jpg','5.jpg']
    current_dir = ''
    pics = Path(current_dir).glob('*')
    Path('new_dir').mkdir(parents=True, exist_ok=True)
    for pic in pics:
        if pic.suffix in ['.jpg', '.png']:
            with Image.open(pic) as img:
                img.load()
                new_pics = img.filter(ImageFilter.FIND_EDGES)
                # new_pics.show()
                new_pics.save(Path('new_dir', pic))
# n2()
import csv
def n3():
    file=open('data.csv','r')
    data=list(csv.reader(file, delimiter=','))
    print("Нужно купить:")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
    file.close()
n3()