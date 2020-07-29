alfabeto = {'a':'ᵃ', 'b':'ᵇ', 'c':'ᶜ', 'd':'ᵈ', 'e':'ᵉ', 'f':'ᶠ', 'g':'ᵍ', 'h':'ʰ', 'i':'ᶤ', 'j':'ʲ', 'k':'ᵏ', 'l':'ˡ',
            'm':'ᵐ', 'n':'ⁿ', 'o':'ᵒ', 'p':'ᵖ', 'q':'۹', 'r':'ʳ', 's':'ˢ', 't':'ᵗ', 'u':'ᵘ', 'v':'ᵛ', 'w':'ʷ',
            'x':'ˣ', 'y':'ʸ', 'z':'ᶻ'}
frase = str(input('Digite sua frase: ')).strip().lower()
for l in frase:
    for g, p in alfabeto.items():
        if l == g:
            print(p, end='')
    if l == ' ':
        print(' ', end='')
