from random import randint
from time import sleep
lista = []
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'Sorteando {num} jogos', '-='*3)
for c in range(1, num+1):
    for p in range(0, 6):
        sort = randint(1, 60)
        while sort in lista:
            sort = randint(1, 60)
        else:
            lista.append(sort)
    sleep(0.5)
    print(f'Jogo {c}: {lista}')
    lista.clear()
print('-='*5, '< BOA SORTE! >', '-='*5)
