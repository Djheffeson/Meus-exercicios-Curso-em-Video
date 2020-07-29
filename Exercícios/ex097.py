def mensagem(frase):
    tam = len(frase) + 4
    print('~'*tam)
    print(frase.center(tam))
    print('~' * tam)


mensagem('Gustavo Guanabara')
mensagem('Curso de Python no Youtube')
mensagem('cev')
