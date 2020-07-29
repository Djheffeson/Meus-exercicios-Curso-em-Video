from random import randint
tup = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('O os números sorteados foram: ', end='')
for n in tup:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')
