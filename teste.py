import urllib.request
import json
import requests


url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=9064c6b20e001de09c9440faa6d1f822"

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)


print(jsondata['results'])
