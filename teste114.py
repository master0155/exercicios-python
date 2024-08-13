# Crie um código em Python que teste se o site
# pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:    
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Não acessivel')
else:
    print('Consegui acesar')
    print(site.read())
# print(site.read())
# mostra o codigo do site.