from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    op = int(input('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa
    >>>>> Qual é a sua opção? '''))
    if op == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
    elif op == 2:
        mult = v1 * v2
        print('A multiplicação entre {} x {} é {}'.format(v1, v2, mult))
    elif op == 3:
        if v1 > v2:
            maior = v1
            menor = v2
        else:
            maior = v2
            menor = v1
        print('O número {} é maior que {}'.format(maior, menor))
    elif op == 4:
        v1 = int(input('Primeiro novo valor: '))
        v2 = int(input('Segundo novo valor: '))
    elif op == 5:
        print('Fechando...')
    else:
        print('Opção invalida. Tente novamente')
    print('=' * 40)
    sleep(1.5)
print('FIM DO PROGRAMA!')
