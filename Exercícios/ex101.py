def voto():
    from datetime import datetime
    now = datetime.now()
    ano_atual = now.year

    ano_nasc = int(input('Em que ano você nasceu? '))
    idade = ano_atual - ano_nasc

    print(f'Com {idade} anos:', end=' ')
    if 18 <= idade <= 65:
        print('VOTO OBRIGATORIO.')
    elif idade >= 16 or idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('NÃO VOTA.')


# Programa Principal

voto()
