pesado = leve = 0
temp = []
dados = []
while True:
    resp = ' '
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    dados.append(temp[:])
    temp.clear()
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N]: ')).strip()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O peso mais pesado foi {pesado}. peso de ', end='')
for p in dados:
    if p[1] == pesado:
        print(f'[ {p[0]} ]', end=' ')
print()
print(f'O peso mais leve foi {leve}. peso de ', end=' ')
for p in dados:
    if p[1] == leve:
        print(f'[ {p[0]} ]', end=' ')
