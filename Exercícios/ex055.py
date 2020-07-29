maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior > peso:
            maior = peso
        elif menor < peso:
                menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
