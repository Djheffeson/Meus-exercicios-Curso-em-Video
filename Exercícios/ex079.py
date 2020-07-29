listanum = []
while True:
    escolha = ' '
    x = int(input('Digite um valor: '))
    if x not in listanum:
        listanum.append(x)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).upper()
    if escolha == 'N':
        break
print('-='*30)
print(f'Você digitou os valores {sorted(listanum)}')
