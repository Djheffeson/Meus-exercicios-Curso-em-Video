from random import randint
from time import sleep
print('\033[33m--=--'*13)
print('\033[34mVou pensar em um número entre 0 e 5 . Tente adivinhar...')
print('\033[33m--=--'*13)
num = randint(0, 5)
res = int(input('Em que número eu pensei? '))
print('\033[1;35mPROCESSANDO...')
sleep(2)
if num == res:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(num, res))
