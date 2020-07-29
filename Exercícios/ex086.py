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
