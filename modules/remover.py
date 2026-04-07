import os
from modules.leitua import leituraArquivos


def remocao_dados (arq):
    pasta = "arquivos"
    arquivos = os.listdir(pasta)
    arquivo_encontrado = None
    for f in arquivos:
        if f.lower().endswith('.txt') and f.lower().replace('.txt', '') == arq:
            arquivo_encontrado = f
            break
    if not arquivo_encontrado:
        print(f"Arquivo '{arq}' não encontrado.")
        return
    caminho = os.path.join(pasta, arquivo_encontrado)
    with open(caminho, "r") as file:
        linhas = file.readlines()

    dado_remover = input("Qual dado deseja remover: ").lower().strip()

    linhas_stripped = [linha.strip().lower() for linha in linhas]
    
    if dado_remover in linhas_stripped:
        index = linhas_stripped.index(dado_remover)
        del linhas[index]
        
        with open(caminho,'w') as f:
            for linha in linhas:
                f.write(linha)
        print(f"'{dado_remover}' removido com sucesso")
    else:
        print("Dado não encontrado")
    
def remover_arquivo(arq):
    pasta = "arquivos"
    arquivos = os.listdir(pasta)
    arquivo_encontrado = None
    for f in arquivos:
        if f.lower().endswith('.txt') and f.lower().replace('.txt', '') == arq:
            arquivo_encontrado = f
            break
    if not arquivo_encontrado:
        print(f"Arquivo '{arq}' não encontrado.")
        return
    caminho = os.path.join(pasta, arquivo_encontrado)
    confirmar = input(f"\033[0;31mDeseja realmente excluir '{caminho}'? (sim/\033[0;32mnão\033[0m) > \033[0m").lower().strip()

    if confirmar in ("sim", "ss", "s"):
        os.remove(caminho)
        print(f"Arquivo '{caminho}' deletado!")
    else:
        print("Cancelado")
    