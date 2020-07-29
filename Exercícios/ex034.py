salario = float(input('Qual o salário do funcionario? R$'))
if salario > 1250:
    salarion = salario + (salario * 10/100)
else:
    salarion = salario + (salario* 15/100)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora.'.format(salario, salarion))
