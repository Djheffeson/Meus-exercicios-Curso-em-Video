m18 = homens = mulheres = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA'.center(25))
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    cont = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if idade >= 18:
        m18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-' * 25)
    while cont not in 'SN':
        cont = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
