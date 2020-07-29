from time import sleep
from ex115.principal import menu
from ex115.cadastro import cadastrar
from ex115.visualização import visualizar

try:
    arquivo = open('cadastrados.txt', 'r')
    arquivo.close()
except FileNotFoundError:
    arquivo = open('cadastrados.txt', 'w')
    arquivo.close()

while True:
    sleep(1)
    escolha = menu()

    if escolha == 1:
        visualizar()
    elif escolha == 2:
        cadastrar()
    elif escolha == 3:
        print('\033[0;35mSaindo...\033[m')
        break
