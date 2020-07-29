lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista')
    else:
        x = 0
        while x < len(lista):
            if num <= lista[x]:
                lista.insert(x, num)
                print(f'Adicionado na posição {x} da lista...')
                break
            x += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
