from time import sleep
from random import randint
from operator import itemgetter
jogadores = dict()
ranking = dict()
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print(" == RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f'  {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
