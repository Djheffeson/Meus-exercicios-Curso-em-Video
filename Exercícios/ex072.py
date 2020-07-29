numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        per = ' '
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente: ', end='')
    print(f'Você digitou o número {numeros[num]}')
    while per not in 'SN':
        per = str(input('Você quer continuar? [S/N]')).upper()
    if per == 'N':
        break
print('Programa finalizado!')
