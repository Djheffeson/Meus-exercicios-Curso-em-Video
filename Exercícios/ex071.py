print('=' * 25)
print('BANCO JOOJ'.center(25))
print('=' * 25)
saque = int(input('Que valor quer sacar? R$'))
total = saque
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 25)
print('Volte sempre ao BANCO JOOJ! Tenha um bom dia!')
