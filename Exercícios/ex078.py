valores = []
for x in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {x}: ')))
print('=-'*25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c in range(0, 5):
    if valores[c] == max(valores):
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for z in range(0, 5):
    if valores[z] == min(valores):
        print(f'{z}...', end='')
