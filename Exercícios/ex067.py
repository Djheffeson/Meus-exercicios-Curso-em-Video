while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        res = c * num
        print(f'{num} x {c} = {res}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO.')
