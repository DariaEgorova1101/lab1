import json
def n1():
    with open('1.json','r') as f:
        data=json.load(f)
    for i in data['products']:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")
# n1()

def n2():
    k=int(input('Ввведите количество товаров: '))
    products = {"products": []}
    for i in range(k):
        name=input('Название: ')
        price=int(input('Цена: '))
        weight=int(input('Вес: '))
        available=bool(input('В наличии 0/1: '))
        products["products"].append({"name": name, "price": price, "weight": weight, "available": available})
    with open('1.json', 'r') as f:
        data = json.load(f)
    data["products"].extend(products["products"])
    for i in data['products']:
        print("Название: ", i["name"])
        print("Цена: ", i["price"])
        print("Вес: ", i["weight"])
        print("В наличии" if i["available"] else "Нет в наличии!", "\n")
    with open("1.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
# n2()

def n3():
    d={}
    with open("en-ru.txt","r") as f:
        for line in f:
            ew=line.split("-")[0].strip()
            rw = line.split("-")[1].strip().split(',')
            for i in rw:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + ew
                else:
                    d[i] = ew
    with open("ru-en.txt", "w") as f:
        for i in sorted(d.keys()):
            f.writelines(f"{i} - {d[i]}\n")
# n3()
