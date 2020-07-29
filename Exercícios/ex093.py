jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0

for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
for c in gols:
    total += c

jogador['gols'] = gols
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {jogador["gols"][i]}')
print(f'Foi um total de {jogador["total"]}')
