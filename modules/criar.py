import os
def criacao (arq):
    pasta = "arquivos"
    os.makedirs(pasta, exist_ok=True)
    arqTexto = os.path.join(pasta,arq + ".txt")
    with open (arqTexto, "w") as arquivo:
        print("Deseja colocar dados no seu arquivo?")
        entrada = input("> ")
        if entrada.lower().strip() in ('sim',"s","ss"):
            print("=== Adicione os dados ===")
            while True:
                dados = input("> ")
                if dados.lower().strip() == 'sair':
                    break
                arquivo.write(dados + "\n")
            print(f"Arquivo, {arqTexto}, salvo com dados")
        elif entrada.lower().strip() in ("não","nao","n"):
            print("Saindo...")
            print(f"Arquivo, {arqTexto} ,salvo")
        else:
            print("Escreva Sim ou Não")
    return arqTexto

