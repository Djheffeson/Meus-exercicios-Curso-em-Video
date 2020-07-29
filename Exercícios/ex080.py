lista = []
num = 0
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0:
        lista.append(num)
        print(f'Valor {num} adicionado no final da lista')
    else:
        if num <= min(lista):
            lista.insert(0, num)
            print('Adicionado na posição 0 da lista')
        elif num >= max(lista):
            lista.insert(5, num)
            print('Adicionado ao final da lista')
        elif lista[1] < num < lista[3]:
            lista.insert(2, num)
            print('Adicionado na posição 2 da lista')
        else:
            lista.insert(1, num)
            print('Adicionado na posição 1 da lista')
print(lista)
