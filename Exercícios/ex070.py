prod1 = produto = ' '
cont = total = price = barato = totcaro = 0
print('-'*30)
print('LOJA SUPER JOOJ'.center(30))
print('-'*30)
while True:
    per = ' '
    cont += 1
    produto = str(input('Nome do produto: ')).strip().capitalize()
    price = float(input('Preço: R$'))
    total += price
    if cont == 1 or price < barato:
        barato = price
        prod1 = produto
    if price >= 1000:
        totcaro += 1
    while per not in 'SN':
        per = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if per == 'N':
        break
print('-'*10,'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totcaro} produtos custando mais de R$1000.00')
print(F'O produto mais barato foi {prod1} que custa R${barato}')
