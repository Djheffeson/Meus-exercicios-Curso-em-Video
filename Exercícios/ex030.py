num = int(input('\033[35mMe diga um número qualquer: '))
res = num%2
if res == 0:
    print('\033[mO número {} é \033[34mpar!'.format(num))
else:
    print('\033[mO número {} é \033[34mimpar!'.format(num))
