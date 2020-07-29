from datetime import datetime
now = datetime.now()

pessoa = dict()

pessoa['nome'] = str(input('Nome: ')).strip().title()
ano_nasc = int(input('Ano Nascimento: '))
pessoa['idade'] = now.year - ano_nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ano_nasc) + 35

print('-'*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
