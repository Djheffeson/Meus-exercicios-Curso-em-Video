n1 = 0
n = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        n += 1
        n1 += c
print('A soma de todos os {} valores solicitados é {}'.format(n, n1))
