v = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m{}'.format(c), end=' ')
        v += 1
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\033[37m\nO número {} foi divisível {} vezes'.format(num, v))
if v == 2:
    print('E por isso ele é um número primo!')
else:
    print('E por isso ele não é um número primo!')
