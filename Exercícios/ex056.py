mulheres = 0
nvelho = ''
velho = 0
total = 0
for x in range(1, 5):
    print('----- {}ª PESSOA -----'.format(x))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    total += idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nvelho = nome
    elif sexo == 'F' and idade < 20:
        mulheres += 1
media = total / 4
print('A media da idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
