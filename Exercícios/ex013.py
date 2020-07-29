#programa para reajustar o salario
sal = float(input('Qual é o salário do funcionário? R$: '))
nsal = sal + (sal*15/100)
print('Um funcionário que ganhava R${:.2f}, com o aumento, passa a receberR${:.2f}'.format(sal, nsal))
