maior = 0
menor = 10000
for x in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(x)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior paso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
