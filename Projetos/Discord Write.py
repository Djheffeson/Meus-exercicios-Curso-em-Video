frase = str(input('Digite a frase: ')).lower().strip()
for c in frase:
    if c == ' ':
        print(' ', end=' ')
    elif c == '?':
        print(':question:', end=' ')
    elif c == '!':
        print(':exclamation:', end=' ')
    else:
        print(f':regional_indicator_{c}:', end=' ')
