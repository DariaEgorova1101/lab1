def n1():
    d = {'Россия': 'Москва', 'Франция': 'Париж', 'Англия': 'Лондон', 'Италия': 'Рим', 'Япония': 'Токио',
         'Китай': 'Пекин', 'Индия': 'Нью-Дели', 'США': 'Вашингтон'}
    print(d.items())
    print(d.get('Италия'))
    print(sorted(d.keys()))


# n1()

def n2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    word = input('Введите слово ')
    sum = 0
    for i in word:
        sum += alph[i.lower()]
    print('Сумма баллов: ', sum)


# n2()
import random


def n3():
    students = {'Петрова', 'Иванов', 'Сидоров', 'Смирнова', 'Цветков', 'Баранова', 'Юдин', 'Школяр', 'Дмитриева',
                'Сорокин'}
    languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}
    lstud = {}
    for st in students:
        k = random.randint(1, 4)
        lstud[st] = random.sample(list(languages), k)
    print(lstud)
    ul = set()
    for i in lstud:
        ul = ul.union(set(lstud[i]))
    print('Множество языков:', sorted(ul), len(ul))
    c2 = []
    for i in lstud:
        ch = i
        if "Китайский" == lstud[i]:
            ch = ch + i

        for el in lstud[i]:
            c2.append(ch)
    c2 = set(c2)
    c2 = list(c2)
    print('Знают китайский:', c2)

# n3()
