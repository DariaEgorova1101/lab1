n = int(input('Количество слов: '))
s=' '
word = (input('Введите слово: '))
for el in range(n):
    s=s+word+' '
    word = (input('Введите слово: '))
print(s)
