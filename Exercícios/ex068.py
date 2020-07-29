from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
totnum = cont = 0
while True:
    valor = int(input('Diga um valor: '))
    player = str(input('Par ou Ímpar? [P/I]')).upper()
    computador = randint(0, 10)
    totnum = valor + computador
    IOP = totnum % 2
    res = ''.upper()
    if IOP == 0:
        res = 'P'
        x = 'PAR'
    else:
        res = 'I'
        x = 'ÍMPAR'
    print('-'*55)
    print(f'Você jogou {valor} e o computador {computador}. Total de {totnum} DEU {x}')
    print('-'*55)
    if player == res:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont += 1
    elif player != res:
        print(f'GAME OVER! você venceu {cont} vezes.')
        print('=-' * 20)
        break
    print('=-'*20)
