from time import sleep


def contagem(ini, fim, passo):
    print('-='*30)
    if passo == 0:
        passo = 1

    print(f'Contagem de {ini} até {fim} de {abs(passo)} e {abs(passo)}')
    passo = abs(passo)

    if ini > fim:
        passo -= passo * 2
        fim -= 1
    else:
        fim += 1

    for c in range(ini, fim, passo):
        sleep(0.3)
        print(c, end=' ')
    sleep(0.3)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fimm = int(input('Fim: '))
passos = int(input('Passo: '))

contagem(inicio, fimm, passos)
