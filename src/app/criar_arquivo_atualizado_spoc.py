import requests
from requests.auth import HTTPBasicAuth
import json
from criar_arquivo_atualizado_meoo import getpass

# Defina suas credenciais
token_url = 'https://api.getrak.com/newkoauth/oauth/token'
client_id = 'localiza_spoc'
client_secret = 'VoN5clM2N2Xh'
username = 'luiz.demetrio@localiza_spoc'
password = 'Fechado5849@'
user = getpass.getuser()


# Prepare os dados para a requisição
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

# Faça a requisição para obter o token
response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data=data)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print('Token de Acesso:', access_token)

    # Defina o endpoint que deseja acessar
    api_url = 'https://api.getrak.com/v1/spoc-internal/recovery-cases'

    # Faça a requisição à API utilizando o token de acesso
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    api_response = requests.get(api_url, headers=headers)

    # Verifique se a requisição foi bem-sucedida
    if api_response.status_code == 200:
        data = api_response.json()

        # Salve os dados em um arquivo JSON
        with open(rf"C:\Users\{user}\OneDrive - NEXCORP SER. TELECOMUNICAÇÕES S.A\Área de Trabalho\prog\workspace\luizgdemetrio\projeto_cobranca\src\data\dados_extraidos.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print('Dados salvos com sucesso!')
    else:
        print('Erro ao acessar a API:', api_response.json())
else:
    print('Erro ao obter token:', response.json())