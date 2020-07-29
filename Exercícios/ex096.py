def area(lar, com):
    metros_quadrados = lar * com
    print(f'A área de um terreno {lar}x{com} é de {metros_quadrados}m².')


print('Controle de terrenos')
print('-'*30)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m):'))
area(lar, com)
    