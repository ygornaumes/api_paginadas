import requests
import pandas as pd

# Inicializando um DataFrame vazio
df_final = pd.DataFrame()

pagina = 1
registros_por_pagina = 100

while True:
    # Construindo a URL da API
    url = f" https://swapi.dev/api/people/?page={pagina}"

    

    # Fazendo a requisição
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        break

    # Convertendo os dados JSON em um DataFrame
    dados = response.json()
    df = pd.DataFrame(dados)

    # Verificando se há mais dados a serem buscados
    if df.empty:
        break

    # Concatenando os DataFrames
    df_final = pd.concat([df_final, df])

    # Indo para a próxima página
    pagina += 1

# Exibindo o DataFrame final
print(df_final)
