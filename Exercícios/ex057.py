n = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while n != 'M' and n != 'F':
    n = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(n))
