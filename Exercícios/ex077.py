palavras = ('aprender', 'programar', 'linguagens', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for x in palavras:
    print(f'\nNa palavra {x.upper()} temos ', end='')
    for vogal in x:
        if vogal in 'aeiou':
            print(f'{vogal}', end=' ')
