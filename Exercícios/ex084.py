maior_peso = menor_peso = 0
pesada = []
leve = []
dados = []
galera = []
while True:
    escolha = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    #Testa o maior menor peso Int
    if len(galera) == 1:
        maior_peso = dados[1]
        menor_peso = dados[1]
        leve.append(dados[0])
        pesada.append(dados[0])
    else:
        if dados[1] > maior_peso:
            pesada.clear()
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            leve.clear()
            menor_peso = dados[1]
        #Testa o maior menor peso Str
        if maior_peso == dados[1]:
            pesada.append(dados[0])
        if menor_peso == dados[1]:
            leve.append(dados[0])
    #Pergunta se o usuario quer continuar
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N]')).strip()
    if escolha in 'Nn':
        break
    dados.clear()
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pesada}')
print(f'O menor peso foi de {menor_peso}Kg.Peso de {leve}')
