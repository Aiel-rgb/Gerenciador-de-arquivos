import os
from time import sleep

def leituraArquivos (arq):
    pasta = "arquivos"
    arquivos = os.listdir(pasta)
    arquivo_encontrado = None
    for f in arquivos:
        if f.lower().endswith('.txt') and f.lower().replace('.txt', '') == arq:
            arquivo_encontrado = f
            break
    if not arquivo_encontrado:
        print(f"Arquivo '{arq}' não encontrado.")
        return None
    caminho = os.path.join(pasta, arquivo_encontrado)
    with open(caminho,"r") as arquivo:
        linhas = arquivo.readlines()
    sleep(0.5)
    for linha in linhas:
        print(linha.rstrip('\n'))
    return linhas

def mostrar_arquivos():
    pasta = "arquivos"

    if not os.path.exists(pasta):
        print("Nenhum arquivo encontrado.")
        return
    
    print(f"📁 {pasta}")
    for arquivo in os.listdir(pasta):
        print(f"    ├── {arquivo}")
    