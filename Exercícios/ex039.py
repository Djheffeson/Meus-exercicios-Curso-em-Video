from datetime import date
sexo = int(input('''Qual seu sexo? 
[ 1 ] para masculino
[ 2 ] para feminino
Digite aqui: '''))
ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
anos_idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, anos_idade, ano_atual))
if sexo == 2:
    print('Você não precisa fazer alistamento obrigatorio')
else:
    if anos_idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif anos_idade < 18:
        alistamento = 18 - anos_idade
        print('Ainda faltam {} anos para o alistamento'.format(alistamento))
        ano_alistamento = alistamento + ano_atual
        print('Seu alistamento será em {}'.format(ano_alistamento))
    else:
        alistamento = anos_idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(alistamento))
        ano_alistamento = ano_atual - alistamento
        print('Seu alistamento foi em {}'.format(ano_alistamento))
