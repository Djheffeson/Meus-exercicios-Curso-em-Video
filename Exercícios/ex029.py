velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7.0
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de \033[33mR${:.2f}'.format(multa))
print('\033[32mTenha um bom dia! Dirija com segurança!')
