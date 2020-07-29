print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
x = 1
total = 0
quant = 10
while quant != 0:
    total += quant
    while x <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        x += 1
    print('PAUSA')
    quant = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
