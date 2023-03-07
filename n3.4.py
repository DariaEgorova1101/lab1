import random

m = 0
p = 0
while m != 3:
    a1 = random.randint(0, 10)
    a2 = random.randint(0, 10)
    print(a1, '+', a2, '=', end=' ')
    a3 = int(input())
    if a3 == (a1 + a2):
        p = p + 1
    else:
        m = m + 1
        if m == 3:
            print('Игра окончена. Правильных ответов:', p)
            break
