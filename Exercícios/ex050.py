soma = 0
cont = 0
for x in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(x)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma de todos eles é igual a {}'.format(cont, soma))
