print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
x = 1
termo = primeiro
while x <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    x += 1
print('Fim')
