import requests
import pandas as pd

# Substitua estas variáveis com suas credenciais
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


# Configuração do cabeçalho
headers = {
    'token': token,
    
}

# Inicializando um DataFrame vazio
df_final = pd.DataFrame()

pagina = 1
registros_por_pagina = 500

while True:
    # Construindo a URL da API
    url = f"seu_link_da_api_aqui?pagina={pagina}&registros_por_pagina={registros_por_pagina}"

    # Fazendo a requisição
    response = requests.get(url, headers=headers)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code != 200:
        print(f"Erro na requisição. Código de status: {response.status_code}")
        break

    # Convertendo os dados JSON em um DataFrame
    dados = response.json()
    df = pd.DataFrame(dados.get("dados", []))

    # Verificando se há mais dados a serem buscados
    if df.empty:
        break

    # Concatenando os DataFrames
    df_final = pd.concat([df_final, df])

    # Indo para a próxima página
    pagina += 1

# Exibindo o DataFrame final
print(df_final)




