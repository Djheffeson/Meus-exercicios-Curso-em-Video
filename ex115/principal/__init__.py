def menu():
    while True:
        print('–'*40)
        print('MENU PRINCIPAL'.center(40))
        print('–' * 40)
        print('\033[0:32m1\033[m — \033[0:34mVer pessoas cadastradas\033[m')
        print('\033[0:32m2\033[m — \033[0:34mCadastrar nova Pessoa\033[m')
        print('\033[0:32m3\033[m — \033[0:34mSair do Sistema\033[m')
        print('–' * 40)

        try:
            escolha = int(input('\033[0;32mSua Opção: \033[m'))
        except:
            print('\033[0:31mEscolha um valor válido!\033[m')
        else:
            if escolha > 3 or escolha < 1:
                print('\033[0:31mEscolha um valor válido!\033[m')
                continue
            return escolha
