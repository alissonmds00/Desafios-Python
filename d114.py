import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Não há conexão')
else:
    print('Há conexão')