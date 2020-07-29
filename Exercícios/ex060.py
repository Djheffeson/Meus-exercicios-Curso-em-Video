from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fact = factorial(num)
print('Calculando {}! = '.format(num), end='')
while num != 0:
    if num == 1:
        print('{}'.format(num), end=' = ')
    else:
        print('{}'.format(num), end=' x ')
    num -= 1
print('{}'.format(fact))
