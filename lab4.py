def n1(n):
    print(n / 3)


# n1(9)
def n2(x):
    if type(x) is not int:
        raise TypeError
    elif x == 0:
        raise ZeroDivisionError
    else:
        print(x / 100)


# n2(x=int(input('Введите число: ')))
def n3(date):
    return int(date[:2]) * int(date[3:5]) == int(date[-2:])


# date=input('Введите дату: ')
# print(n3(date))

def n4(s):
    if len(s) % 2 != 0:
        print('Число должно быть четным!')
        pass
    else:
        s2 = len(s) // 2
        return int(s[:s2]) == int(s[s2:])

# s = input('Введите четный номер: ')
# print(n4(s))
