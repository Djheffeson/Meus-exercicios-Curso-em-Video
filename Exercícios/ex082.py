lista = []
impares = []
pares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N]'))
    if escolha in 'Nn':
        break
impares.sort()
pares.sort()
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
