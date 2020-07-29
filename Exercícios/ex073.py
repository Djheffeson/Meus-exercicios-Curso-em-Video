tabela = ('Flamengo', 'Atletico', 'São paulo', 'Internacional', 'Grêmio', 'Palmeiras', 'Sport Recife',
          'Cruzeiro', 'Botafogo', 'Corinthias', 'Vasco da gama', 'Fluminense', 'América-MG', 'Chapecoense',
          'Santos', 'EC Vitória', 'Bahia', 'Paraná', 'Atlético-PR', 'Ceará SC')
print('-='*15)
print(f'Lista de times do brasileirão: {tabela}')
print('-='*15)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('-='*15)
print(f'Os 4 últimos são{tabela [-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*15)
print(f'O Chapecoense esta na {tabela.index("Chapecoense")+1}ª posição')
