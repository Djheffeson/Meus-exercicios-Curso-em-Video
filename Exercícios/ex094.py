pessoa = dict()
pessoas = list()
idade_geral = 0
mulheres = []

while True:
    pessoa.clear()
    continuar = ' '
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]')).lower()[0]
        print('ERRO! Responda apenas S ou N.')
    if continuar == "n":
        break


print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')


for c in pessoas:
    idade_geral += c['idade']
idade_media = idade_geral / len(pessoas)
print(f'B) A média de idade é de {idade_media:.2f} anos.')

for i, v in enumerate(pessoas):
    if pessoas[i]['sexo'] == 'f':
        mulheres.append(pessoas[i]['nome'])
print('As mulheres cadastradas foram', end=' ')
for c in mulheres:
    print(c, end=' ')
print()

print('Lista das pessoas que estão acima da média: ')
for c in pessoas:
    for k, v in c.items():
        if c['idade'] > idade_media:
            print(f'    {k} = {v}', end='; ')
    print()
print('<< ENCERRADO >>')
