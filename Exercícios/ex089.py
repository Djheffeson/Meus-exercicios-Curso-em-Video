alunos = list()
id = 0
while True:
    resp = ' '
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([id, nome, [nota1, nota2], media])
    while resp not in ('SsNn'):
        resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
    id += 1
print(alunos)
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for c, v in enumerate(alunos):
    print(f'{alunos[c][0]:<4}{alunos[c][1]:<10}{alunos[c][3]:>8.1f}')
while True:
    print('-'*50)
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolha == 999:
        break
    print(f'Notas de {alunos[escolha][1]} são {alunos[escolha][2]}')
