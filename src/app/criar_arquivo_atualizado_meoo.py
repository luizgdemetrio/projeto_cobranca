""""""
import getpass
import os
from datetime import datetime
import getpass
import pandas as pd


def extrair_data_arquivo(nome_arquivo):
    try:
        data_str = nome_arquivo.split()[-1].replace(".xlsx", "")
        return datetime.strptime(data_str, "%d-%m-%y")
    except Exception:
        return datetime.min


def obter_arquivos_recentes(caminho_pasta, palavra_chave, quantidade=2):
    arquivos = [
        os.path.join(caminho_pasta, arquivo)
        for arquivo in os.listdir(caminho_pasta)
        if palavra_chave.lower() in arquivo.lower()
        and os.path.isfile(os.path.join(caminho_pasta, arquivo))
    ]

    if len(arquivos) < quantidade:
        raise FileNotFoundError(
            f"Menos de {quantidade} arquivos encontrados contendo '{palavra_chave}'."
        )

    arquivos.sort(
        key=lambda x: (os.path.getctime(x), extrair_data_arquivo(x)), reverse=True
    )

    return arquivos[:quantidade]


def ajustar_coluna_atribuicao_retoma_meoo(caminho_arquivo):
    # Lê o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo)

    # Verifica se a coluna "Atribuição" existe
    if 'Atribuição' in df.columns:
        # Renomeia a coluna para "Atribuicao"
        df.rename(columns={'Atribuição': 'Atribuicao'}, inplace=True)
        # Salva as alterações no mesmo arquivo
        df.to_excel(caminho_arquivo, index=False)
        print(f"Coluna 'Atribuição' renomeada para 'Atribuicao' no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuição' não foi encontrada no arquivo: {caminho_arquivo}")

    # Verifica se a coluna "Atribuicao" já existe
    if 'Atribuicao' in df.columns:
        print(f"A coluna 'Atribuicao' já existe no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuicao' não foi encontrada no arquivo: {caminho_arquivo}")

    return df


def ajustar_coluna_atribuicao_retoma_meoo_previous(caminho_arquivo):
    # Lê o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo)

    # Verifica se a coluna "Atribuição" existe
    if 'Atribuição' in df.columns:
        # Renomeia a coluna para "Atribuicao"
        df.rename(columns={'Atribuição': 'Atribuicao'}, inplace=True)
        # Salva as alterações no mesmo arquivo
        df.to_excel(caminho_arquivo, index=False)
        print(f"Coluna 'Atribuição' renomeada para 'Atribuicao' no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuição' não foi encontrada no arquivo: {caminho_arquivo}")

    # Verifica se a coluna "Atribuicao" já existe
    if 'Atribuicao' in df.columns:
        print(f"A coluna 'Atribuicao' já existe no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuicao' não foi encontrada no arquivo: {caminho_arquivo}")

    return df


def ajustar_coluna_atribuicao(caminho_arquivo):
    # Lê o arquivo Excel em um DataFrame
    df = pd.read_excel(caminho_arquivo)   

    # Verifica se a coluna "Atribuição" existe
    if 'Atribuição' in df.columns:
        # Renomeia a coluna para "Atribuicao"
        df.rename(columns={'Atribuição': 'Atribuicao'}, inplace=True)
        # Salva as alterações no mesmo arquivo
        df.to_excel(caminho_arquivo, index=False)
        print(f"Coluna 'Atribuição' renomeada para 'Atribuicao' no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuição' não foi encontrada no arquivo: {caminho_arquivo}")

    # Verifica se a coluna "Atribuicao" já existe
    if 'Atribuicao' in df.columns:
        print(f"A coluna 'Atribuicao' já existe no arquivo: {caminho_arquivo}")
    else:
        print(f"A coluna 'Atribuicao' não foi encontrada no arquivo: {caminho_arquivo}")

    return df


def renomear_arquivo_com_data_atual(caminho_arquivo):
    pasta = os.path.dirname(caminho_arquivo)
    nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
    data_atual = datetime.now().strftime("%d-%m-%Y")
    novo_nome = f"{nome_arquivo} {data_atual}{extensao}"
    novo_caminho = os.path.join(pasta, novo_nome)

    contador = 1
    while os.path.exists(novo_caminho):
        novo_nome = f"{nome_arquivo} {data_atual}_{contador}{extensao}"
        novo_caminho = os.path.join(pasta, novo_nome)
        contador += 1

    os.rename(caminho_arquivo, novo_caminho)
    print(f"Arquivo renomeado para: {novo_caminho}")
    return novo_caminho


def main():
    user = getpass.getuser()
    print(f"Usuário logado: {user}")

    path_folder = f"C:\\Users\\{user}\\OneDrive - NEXCORP SER. TELECOMUNICAÇÕES S.A\\Área de Trabalho\\prog\\automacao_pendente\\download"
    recent_files = obter_arquivos_recentes(path_folder, "Retoma")

    print(f"Arquivos mais recentes encontrados:")
    for files in recent_files:
        print(f"- {os.path.basename(files)}")

    df_recente = pd.read_excel(recent_files[0])
    caminho_salvar_recente = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Retoma Meoo.xlsx"
    )
    df_recente.to_excel(caminho_salvar_recente, index=False)
    print(f"Arquivo mais recente salvo em: {caminho_salvar_recente}")
    df_recente_ajustado = ajustar_coluna_atribuicao_retoma_meoo(caminho_salvar_recente)
    df_anterior = pd.read_excel(recent_files[1])
    caminho_salvar_anterior = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Retoma Meoo_Previous.xlsx"
    )
    df_anterior.to_excel(caminho_salvar_anterior, index=False)
    print(f"Segundo arquivo mais recente salvo em: {caminho_salvar_anterior}")
    df_anterior_ajustado = ajustar_coluna_atribuicao_retoma_meoo_previous(caminho_salvar_anterior)
    arquivo_info_cliente = obter_arquivos_recentes(
            path_folder, "Info Cliente", 1
        )[0]

    # Ajusta a coluna "Atribuição" para "Atribuicao"
    df_info_cliente = ajustar_coluna_atribuicao(arquivo_info_cliente)

    caminho_salvar_clientes = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Clientes.xlsx"
    )
    df_info_cliente.to_excel(caminho_salvar_clientes, index=False)
    print(
        f"Arquivo 'Info Cliente' salvo como 'Clientes.xlsx' em: {caminho_salvar_clientes}"
    )
    print("Visualização das primeiras linhas do arquivo 'Info Cliente':")
    print(df_info_cliente.head())

    renomear_arquivo_com_data_atual(arquivo_info_cliente)

    try:
        caminho_planilha = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "Retoma Meoo Planilha.xlsx"
        )
        novo_caminho_planilha = renomear_arquivo_com_data_atual(caminho_planilha)
        print(
            f"Arquivo 'Retoma Meoo Planilha.xlsx' renomeado para: {novo_caminho_planilha}"
        )
    except FileNotFoundError:
        print("Arquivo 'Retoma Meoo Planilha.xlsx' não encontrado.")
    except Exception as erro:
        print(f"Erro ao renomear 'Retoma Meoo Planilha.xlsx': {erro}.")


if __name__ == "__main__":
    main()