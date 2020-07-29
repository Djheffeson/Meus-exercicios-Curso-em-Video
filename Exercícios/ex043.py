peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no PESO IDEAL')
elif imc > 25 and imc >= 30:
    print('Você está em OBESIDADE!')
elif imc > 30:
    print('Você está em OBESIDADE MÓRBIDA')
