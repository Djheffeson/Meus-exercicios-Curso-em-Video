from random import randint
cpu = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Sera que você consegue adivinhar qual foi?''')
acertou = False
tent = 0
while not acertou:
    num = int(input('Qual é seu palpite? '))
    if num == cpu:
        acertou = True
    elif num < cpu:
        print('Mais...Tente mais uma vez.')
    elif num > cpu:
        print('Menos...Tente mais uma vez.')
    tent += 1
print('Acertou com {} tentativas. parabéns!'.format(tent))
