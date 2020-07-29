jogador = dict()
jogadores = list()
while True:
    gols = []

    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())
    jogador.clear()

    while True:
        continuar = str(input('Você quer continuar? [S/N]? ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar in 'N':
        break

print('-='*30)
print(f'{"cod":<4}{"nome":<10}{"gols":<10}{"total"}')
print('-'*30)
for i, v in enumerate(jogadores):
    print(f'{i:<2}{v["nome"]:<10} {str(v["gols"]):<12} {v["total"]:>}')

while True:
    print('-'*30)
    show = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if show == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[show]["nome"]}')
    for i, gol in enumerate(jogadores[show]["gols"]):
        print(f'    No jogo {i+1} fez {gol} gols')
print('<<< ENCERRANDO >>')
