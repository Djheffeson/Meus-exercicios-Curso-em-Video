try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):
    print('ERRO GARAI AZIEDEIA, SE DIGITO ERRADO MEU IRMÃO ASS: ZOIO RARDCORE')
except ZeroDivisionError:
    print('GARAI MEU IRMÃO, DIVIDIR POR ZERO É IMPOSSIVEL AZIDEIA KKKK ASS: ZOIO RAARD')
except KeyboardInterrupt:
    print('GARAI MEU IRMÃO, DIGITA AI PO ASS: ZOIO PO')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('falo garai ate a proxima')
