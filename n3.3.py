word = ''
while word != 'stop':
    word = (input('Введите слово: '))
    if word.count('ф'):
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')