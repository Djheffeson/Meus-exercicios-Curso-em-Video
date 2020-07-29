print('='*10, 'Loja do JOOJ', '='*10)
preço = float(input('Preço das compras: R$'))
forma = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
Qual é a opção? '''))
if forma == 1:
    desconto = preço * 10/100
    print('Sua compra de {} vai custar {:.2f} no final.'.format(preço, preço - desconto))
elif forma == 2:
    desconto = preço * 5 / 100
    print('Sua compra de {} vai custar {:.2f} no final.'.format(preço, preço - desconto))
elif forma == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de {} SEM JUROS'.format(parcela))
    print('Sua compra vai custar {} no final.'.format(preço))
elif forma == 4:
    juros = preço * 20 / 100
    novopreço = preço + juros
    quant = int(input('Quantas parcelas? '))
    parcela = novopreço / quant
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(quant, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novopreço))
else:
    print('\033[31mOPÇÃO INVALIDA de pagamento. Tente novamente!')
