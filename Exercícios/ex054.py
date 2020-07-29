maior = 0
menor = 0
from datetime import date
for x in range(1, 8):
    pessoa = int(input('Em que ano a {}ª pessoa nasceu? '.format(x)))
    res = date.today().year - pessoa
    if res >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} menores de idade'.format(maior, menor))
