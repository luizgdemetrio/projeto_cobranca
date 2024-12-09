import requests
from requests.auth import HTTPBasicAuth
import json
from criar_arquivo_atualizado_meoo import getpass
from dotenv import load_dotenv
import os
import shutil
from pathlib import Path


load_dotenv()

# Defina suas credenciais
token_url = os.getenv("TOKEN_URL")  
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
login = os.getenv('login')
password = os.getenv('password')

user = getpass.getuser()


# Prepare os dados para a requisição
data = {
    'grant_type': 'password',
    'username': login,
    'password': password
}

# Faça a requisição para obter o token
response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data=data)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print('Token de Acesso:', access_token)

    # Defina o endpoint que deseja acessar
    api_url = os.getenv('api_url')

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

# Caminhos dos arquivos usando pathlib e o nome do usuário atual
base_dir = Path(
    rf"C:\Users\{user}\OneDrive - NEXCORP SER. TELECOMUNICAÇÕES S.A\Área de Trabalho\prog\automacao_pendente"
)
retoma_meoo_path = base_dir / "Pendências Meoo LL Getrak.xlsx"


def copiar_e_renomear_arquivo(diretorio_origem, diretorio_destino, nome_base_arquivo):
    """
    Procura o arquivo mais recente com base no nome base, copia e renomeia-o, removendo a data.

    Args:
        diretorio_origem (Path): Diretório onde os arquivos estão localizados.
        diretorio_destino (Path): Diretório para onde o arquivo será copiado.
        nome_base_arquivo (str): Nome base do arquivo (sem a data).
    """
    # Listar todos os arquivos no diretório de origem que começam com o nome base
    arquivos = list(diretorio_origem.glob(f"{nome_base_arquivo}*"))

    # Verificar se há arquivos correspondentes
    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    # Encontrar o arquivo mais recente
    arquivo_mais_recente = max(arquivos, key=lambda x: x.stat().st_mtime)

    # Definir o caminho do novo arquivo (sem a data)
    novo_nome_arquivo = f"{nome_base_arquivo}.xlsx"
    novo_caminho_arquivo = diretorio_destino / novo_nome_arquivo

    # Copiar e renomear o arquivo
    shutil.copy2(arquivo_mais_recente, novo_caminho_arquivo)
    print(f"Arquivo {arquivo_mais_recente} copiado para {novo_caminho_arquivo} com sucesso.")



# Diretório de origem e destino


diretorio_origem = base_dir / "download"
diretorio_destino = base_dir
nome_base_arquivo = "Pendências Meoo LL Getrak"

copiar_e_renomear_arquivo(diretorio_origem, diretorio_destino, nome_base_arquivo)
