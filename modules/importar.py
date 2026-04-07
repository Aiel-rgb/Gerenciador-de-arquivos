import pyshark
import pandas as pd
import os

def pcap_para_csv(caminho_pcap, caminho_csv):
    """
    Converte um arquivo .pcap do Wireshark para .csv usando pyshark.
    Extrai campos básicos como: timestamp, protocolo, src_ip, dst_ip, length.
    """
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_pcap):
        print(f"Arquivo {caminho_pcap} não encontrado.")
        return None

    # Lê o arquivo .pcap
    cap = pyshark.FileCapture(caminho_pcap)

    # Lista para armazenar os dados
    dados = []

    for pkt in cap:
        try:
            # Extrai campos comuns (ajuste conforme necessário)
            timestamp = pkt.sniff_time
            protocolo = pkt.highest_layer
            src_ip = getattr(pkt, 'ip', {}).get('src', 'N/A')
            dst_ip = getattr(pkt, 'ip', {}).get('dst', 'N/A')
            length = pkt.length

            dados.append({
                'timestamp': timestamp,
                'protocolo': protocolo,
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'length': length
            })
        except AttributeError:
            # Pula pacotes que não têm os campos esperados
            continue

    # Cria DataFrame
    df = pd.DataFrame(dados)

    # Salva como CSV
    df.to_csv(caminho_csv, index=False)
    print(f"Arquivo convertido e salvo em {caminho_csv}")

    return df

# Exemplo de uso (pode ser chamado do main.py)
# df = pcap_para_csv('arquivos/captura.pcap', 'arquivos/captura.csv')