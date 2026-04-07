import os
import pyfiglet

verde = "\033[0;32m"
azul = "\033[0;34m"
vermelho = "\033[0;31m"
reset = '\033[0m'

def tela():
    os.system("clear")

    largura = os.get_terminal_size().columns

    titulo = pyfiglet.figlet_format("Shark\nArchives", font="colossal")
    separador = '-' * largura

    print(separador)
    print(azul + titulo + reset)
    print(separador)
    print()

    esquerda = [
        "[1] Criar Arquivo",
        "[2] Ler Arquivo",
        "[3] Adicionar dados",
        "[4] Remover dados",
        "[5] Remover arquivo",
    ]

    direita = [
        "[6] Importar pcap",
        "[7] Filtrar tráfego",
        "[8] Mostrar tabela",
        "[9] Exibir gráfico",
        "[10] Gerar DataFrame",
    ]

    largura_esquerda = max(len(item) for item in esquerda) + 4
    largura_direita = max(len(item) for item in direita) + 4
    divisor = " | "
    bloco_largura = largura_esquerda + len(divisor) + largura_direita
    padding = max(0, (largura - bloco_largura) // 2)

    print("Menu de Seleção".center(largura))
    print()
    header_left = "Opções de Manipulação".ljust(largura_esquerda)
    header_right = "Opções de Wireshark".ljust(largura_direita)
    header = f"{verde}{header_left}{reset}{divisor}{azul}{header_right}{reset}"
    print(" " * padding + header)
    print()

    for i in range(max(len(esquerda), len(direita))):
        esquerda_item = esquerda[i] if i < len(esquerda) else ""
        direita_item = direita[i] if i < len(direita) else ""
        linha = esquerda_item.ljust(largura_esquerda) + divisor + direita_item.ljust(largura_direita)
        print(" " * padding + linha)

    print()
    saida = "[S] Sair".center(bloco_largura)
    print(" " * padding + f"{vermelho}{saida}{reset}")
    print()
    print(separador)