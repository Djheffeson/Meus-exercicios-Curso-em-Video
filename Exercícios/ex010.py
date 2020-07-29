#Faça um programa que mostre o quanto o dolar vale ou outras moedas.
rs = float(input('Quanto dinheiro você tem na carteira?: R$'))
dol = rs/3.7074
eu = rs/4.36
yen = rs/0.0309
print('Com R${:.2f} você pode comprar U${:.2f}, €{:.2f} e ¥{:.2f}'.format(rs, dol, eu, yen))
