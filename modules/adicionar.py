import os

def adicionarArquivos(arq):
    caminho = os.path.join("arquivos", arq + ".txt")

    if not os.path.exists(caminho):
        print(f"Arquivo '{arq}' não encontrado.")
        return None

    with open (caminho,'a') as arquivo:
        print("=== Adicione os dados (digite 'sair' para terminar) ===")
        while True:
            dados = input("> ")
            if dados.lower().strip() == "sair":
                break
            arquivo.write(dados + "\n")
    print(f"Dados adicionados em '{arq}'.")
    