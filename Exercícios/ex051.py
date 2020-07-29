import emoji
print('='*21)
print('10 TERMOS DE UMA PA')
print('='*21)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for x in range(1, 11):
    print(emoji.emojize('{} :arrow_right:'.format(termo), use_aliases=True), end=' ')
    termo += razao
print('ACABOU')
