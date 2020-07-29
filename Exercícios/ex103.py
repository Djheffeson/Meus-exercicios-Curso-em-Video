def ficha(n='<desconhecido>', g=0):

    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa Principal

nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

if gols == '':
    gols = 0

ficha(nome, gols)
