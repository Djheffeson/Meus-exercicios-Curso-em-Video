from random import randint
palp = 1
numa = randint(0, 10)
print('''Sou seu computador...Acabei de pensar em um número de 0 a 10.
Será que você consegue adivinhar qual foi?''')
num = int(input('Qual é seu palpite? '))
while num != numa:
    if num < numa:
        print('Mais... Tente mais uma vez.')
    elif num > numa:
        print('Menos... Tenta mais uma vez')
    num = int(input('Qual é o seu palpite? '))
    palp += 1
print('Acertou com {} tentativas. Parabéns!'.format(palp))
