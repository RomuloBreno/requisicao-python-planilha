#import imp
#import string
from datetime import date
import json
import urllib.request, urllib.error, urllib.parse, urllib.response, requests
urldefault = 'Insira uma planilha do sheetdb'
response = urllib.request.urlopen(urldefault)
dados = json.loads(response.read())
for dado in dados:
  requisicao = dado['dominios']
  urls = urllib.request.Request(url=requisicao, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
  responseT = urllib.request.urlopen(urls)
  html = str(responseT.read())
  if 'syntax error' in html:
    dia = date.today()
    data = {'id': 1, 'dia': {dia} ,'dominios': {requisicao}, 'erros': {html}}
    responsea = requests.post('https://sheetdb.io/api/v1/r9fdgawufubel?sheet=erros', data=data)
    print(responsea)
    print(f"erro do site {requisicao} foi adicionado")
  else:
    print(f"{requisicao} não tem erros")
#Esse código também é uma parceria com "Eduardo Pinheiro(https://github.com/odraudep)"
