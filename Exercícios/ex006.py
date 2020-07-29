#Faça o programa pedir um número e some, triplique e mostre a raiz quadrada do número.
n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n, n*2))
print('O trilo de {} vale {}'.format(n, n*3))
print('A raiz quadrada de {} é igual a {:.2f}'.format(n, n**(1/2)))
