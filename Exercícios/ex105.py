def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opicional, indicano se deve ou não adicionar a situação.
    :return: dicionário com varias informações sobre a situação da turma.
    '''
    maior = menor = tot = 0
    quant = len(n)
    for i, v in enumerate(n):
        tot += v
        if i == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
    media = tot / quant
    dicionario = {'total': quant, 'maior': maior, 'menor': menor, 'média': media}
    if sit:
        if media < 5:
            dicionario['situação'] = 'RUIM'
        elif media < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOA'
    return dicionario


# Programa Principal
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)

help(notas)
