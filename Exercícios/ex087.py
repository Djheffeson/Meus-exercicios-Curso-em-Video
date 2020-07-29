pares = soma = maior = 0
matriz = [[], [], []]
for x in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [0, {x}]: ')))
for x in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1, {x}]: ')))
for x in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2, {x}]: ')))
print('-='*20)
for c in range(0, 3):
    print(f'[ {matriz[0][c]} ]', end='')
print()
for c in range(0, 3):
    print(f'[ {matriz[1][c]} ]', end='')
print()
for c in range(0, 3):
    print(f'[ {matriz[2][c]} ]', end='')
print()
print('-='*20)
for c in matriz:
    for x in c:
        if x % 2 == 0:
            pares += x
for c in range(0, 3):
    soma += matriz[c][2]
for c in matriz[1]:
    if c > maior:
        maior = c
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
