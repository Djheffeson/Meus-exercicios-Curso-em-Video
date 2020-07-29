from time import sleep


def maior(*num):
    print('-='*30)
    maior = 0
    print('Analizando os valores passados...')
    for c in num:
        sleep(0.3)
        print(c, end=' ')
        if c > maior:
            maior = c
    print(f'foram informados ao todo {len(num)} valores ao todo.')
    print(f'O maior valor foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
