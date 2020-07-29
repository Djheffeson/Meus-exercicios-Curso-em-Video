from time import sleep
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
sleep(1)
if media >= 7.0:
    print('O aluno está \033[1;32mAPROVADO!')
elif media < 6.9 and media >= 5.0:
    print('O aluno está em \033[1;33mRECUPERAÇÃO!')
elif media < 5.0:
    print('O aluno está \033[1;31mREPROVADO!')
