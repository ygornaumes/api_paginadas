import requests

link = "https://api.github.com/users?since=1&per_page=1"

requisicao = requests.get(link)
informacoes = requisicao.json()


import pprint

pprint.pprint(informacoes)