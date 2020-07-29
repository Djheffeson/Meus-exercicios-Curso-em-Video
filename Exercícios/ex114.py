import requests

try:
    url = 'http://pudim.com.br/'
    response = requests.get(url)

    print('\033[0;32mConsegui acessar o site do pudim!\033[m')
except:
    print('\033[0;31mNão consegui acessar o site do pudim!\033[m')
