import pandas as pd
import os

PASTA = "Shark_csvs/convertidos"

def normalizar_nome_csv(nome_arquivo):
    nome_arquivo = nome_arquivo.strip()
    if not nome_arquivo:
        return nome_arquivo
    return nome_arquivo if nome_arquivo.lower().endswith('.csv') else nome_arquivo + '.csv'


def carregar(nome_arquivo):
    nome_arquivo = normalizar_nome_csv(nome_arquivo)
    caminho = os.path.join(PASTA, nome_arquivo)

    if not os.path.exists(caminho):
        print(f"Arquivo '{nome_arquivo}' não encontrado na pasta '{PASTA}'.")
        return None
    
    df = pd.read_csv(caminho)
    print(f"Arquivo '{len(df)}' carregado com sucesso.")
    return df


def resumo(df):
    print("\n=== RESUMO ===")
    print(f"Total de pacotes: {len(df)}")
    print(f"Protocolos únicos: {df['protocolo'].nunique()}")
    print(f"IPs de origem: {df['origem'].nunique()}")
    print(f"IPs de destino: {df['destino'].nunique()}")
    print(df['protocolo'].value_counts().to_string())
    input("\nPressione Enter para continuar...")