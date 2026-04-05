import os

def leituraArquivos (arq):
    caminho = os.path.join("arquivos",arq + ".txt")

    if not os.path.exists(caminho):
        print(f"Arquivo '{arq}' não encontrado.")
        return None

    with open(caminho,"r") as arquivo:
        linhas = arquivo.read().strip().split("\n")
    
    for linha in linhas:
        print(linha)

def mostrar_arquivos():
    pasta = "arquivos"

    if not os.path.exists(pasta):
        print("Nenhum arquivo encontrado.")
        return
    
    print(f"\n📁 {pasta}")
    for arquivo in os.listdir(pasta):
        print(f"\n l__ {arquivo}\n")
    