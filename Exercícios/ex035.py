print('-=-'*10)
print('Analizador de Triângulos')
print('-=-'*10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmenots acima NÃO PODEM FORMAR triângulo')
