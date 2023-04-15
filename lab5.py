import random


def n1(n):
    l = []
    for i in range(5):
        l.append(random.randint(0, 100))
    print(l)
    if l.count(n) == True:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')


# n1(n=int(input('Введите число: ')))


def n2(Counter):
    l = []
    for i in range(10):
        l.append(random.randint(0, 100))
    print(l)
    for number, count in Counter(l).items():
        if count > 1:
            print(count)


# n2(Counter)

def n3(w):
    day = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    print('Ваши выходные дни:', day[-w:7])
    print('Ваши рабочие дни:', day[0:-w])


# w = int(input('Сколько выходных вы хотите: '))
# n3(w)
def n4():
    A = ('Петрова', 'Иванов', 'Сидоров', 'Смирнова', 'Цветков', 'Баранова', 'Юдин', 'Школяр', 'Дмитриева', 'Сорокин')
    B = ('Уваров', 'Фокин', 'Зайкина', 'Соколова', 'Миронов', 'Бобров', 'Никитин', 'Данилов', 'Лисов', 'Собакина')
    s1 = []
    s2 = []
    for i in range(1):
        s1 = random.sample(list(A), 5)
        s2 = random.sample(list(B), 5)
    sport = s1 + s2
    a = tuple(sorted(sport))
    tuple(sport)
    print(A, sep='\n')
    print(B, sep='\n')
    print('Спортивная команда: ', tuple(sport))
    print('Количество человек', len(sport))
    print(a)
    print(sport.count('Иванов'))
n4()