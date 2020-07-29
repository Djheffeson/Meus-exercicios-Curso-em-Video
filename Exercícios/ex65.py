x = 'S'
cont = tot = maior = menor = num = 0
while x != 'N':
    cont += 1
    num = int(input('Digite um número: '))
    tot += num
    if cont == 1:
        menor = maior = num
    elif menor > num:
        menor = num
    elif maior < num:
        maior = num
    x = str(input('Você quer continuar? [S/N] ')).upper()
media = tot / cont
print('Você digitou {} números e a média foi de {}'.format(cont, media))
print('O maior valor foi de {} e o menor foi {}'.format(maior, menor))
