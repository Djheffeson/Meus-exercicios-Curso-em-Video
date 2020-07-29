valorcasa = float(input('Valor da casa: '))
salcomprador = float(input('Salário do comprador: '))
anosf = int(input('Quandos anos de financiamento? '))
parcela = valorcasa/(anosf*12)
por = salcomprador * 30/100
if parcela <= por:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f} Emprestimo pode ser CONCEDIDO!'.format(valorcasa, anosf, parcela))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f} Empréstimo NEGADO!')
