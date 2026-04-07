import os

def adicionarArquivos(arq):
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

    with open (caminho,'a') as arquivo:
        print("=== Adicione os dados (digite 'sair' para terminar) ===")
        while True:
            dados = input("> ").lower().strip()
            if dados == "sair":
                break
            arquivo.write(dados + "\n")
    print(f"Dados adicionados em '{arq}'.")
