#faça um produto que dê um desconto.
p = float(input('Qual o preço do produto? R$:'))
por = p - (p*5/100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, por))
