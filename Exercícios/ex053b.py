frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for c in (range(len(junto) - 1, -1, -1)):
    invertido += junto[c]
print('O inverso de {} é {}'.format(junto, invertido))
if junto == invertido:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
