import os
import pandas as pd
from scapy.all import rdpcap
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA_ENTRADA = os.path.join(BASE, "Shark_csvs")
PASTA_SAIDA = os.path.join(BASE, "Shark_csvs", "convertidos")

def listar_arquivos_entrada():
    if not os.path.exists(PASTA_ENTRADA):
        print("Pasta 'Shark_csvs' não existe.")
        return
    arquivos = sorted([f for f in os.listdir(PASTA_ENTRADA) if os.path.isfile(os.path.join(PASTA_ENTRADA, f))])
    if not arquivos:
        print("Nenhum arquivo encontrado em Shark_csvs.")
        return
    print("Arquivos em Shark_csvs:")
    for arquivo in arquivos:
        print(f"  - {arquivo}")


def listar_arquivos_convertidos():
    if not os.path.exists(PASTA_SAIDA):
        print("Pasta 'Shark_csvs/convertidos' não existe.")
        return
    arquivos = sorted([f for f in os.listdir(PASTA_SAIDA) if os.path.isfile(os.path.join(PASTA_SAIDA, f))])
    if not arquivos:
        print("Nenhum arquivo encontrado em Shark_csvs/convertidos.")
        return
    print("Arquivos em Shark_csvs/convertidos:")
    for arquivo in arquivos:
        print(f"  - {arquivo}")


def normalizar_nome_pcap(nome_arquivo):
    nome_arquivo = nome_arquivo.strip()
    if not nome_arquivo:
        return nome_arquivo
    extensao = os.path.splitext(nome_arquivo)[1].lower()
    if extensao in [".pcap", ".pcapng"]:
        return nome_arquivo
    for ext in [".pcapng", ".pcap"]:
        candidato = nome_arquivo + ext
        if os.path.exists(os.path.join(PASTA_ENTRADA, candidato)):
            return candidato
    return nome_arquivo + ".pcap"


def importar(nome_arquivo):
    nome_arquivo = normalizar_nome_pcap(nome_arquivo)
    caminho = os.path.join(PASTA_ENTRADA, nome_arquivo)

    if not os.path.exists(caminho):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None

    print(f"Lendo '{nome_arquivo}'...")
    pacotes_raw = rdpcap(caminho)

    pacotes = []
    for pkt in pacotes_raw:
        try:
            if pkt.haslayer(IP):
                origem  = pkt[IP].src
                destino = pkt[IP].dst
            elif pkt.haslayer(IPv6):
                origem  = pkt[IPv6].src
                destino = pkt[IPv6].dst
            else:
                continue

            pacotes.append({
                "origem":    origem,
                "destino":   destino,
                "protocolo": pkt.lastlayer().name,
                "Length":    len(pkt),
            })
        except Exception:
            continue

    df = pd.DataFrame(pacotes)
    os.makedirs(PASTA_SAIDA, exist_ok=True)
    nome_saida = nome_arquivo.replace(".pcapng", ".csv").replace(".pcap", ".csv")
    caminho_saida = os.path.join(PASTA_SAIDA, nome_saida)
    df.to_csv(caminho_saida, index=False)

    print(f"{len(df)} pacotes convertidos para '{caminho_saida}'.")
    return df