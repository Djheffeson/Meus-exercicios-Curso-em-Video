lista = []
while True:
    y = ' '
    lista.append(int(input('Digite um valor: ')))
    while y not in 'SN':
        y = input('Quer continuar? [S/N]').upper().strip()
    if y == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
