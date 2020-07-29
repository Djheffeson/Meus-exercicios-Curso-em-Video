frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
if frase == junto[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
print(junto)
