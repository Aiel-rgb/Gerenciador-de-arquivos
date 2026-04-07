import os
import pyfiglet

vermelho = "\033[0;31m"
azul = "\033[0;34m"
reset = '\033[0m'

def tela():
    os.system("clear")

    largura = os.get_terminal_size().columns

    titulo = pyfiglet.figlet_format("Shark\nArchives",font="colossal")
    
    separador = '-'*largura

    print(separador)
    print(azul + titulo + reset)
    print(separador)
    print()

    opcoes = [
        "[1] Criar Arquivo                          ",
        "[2] Ler Arquivo                            ",
        "[3] Adicionar dados a um arquivo           ",
        "[4] Remover dados de um arquivo            ",
        "[5] Remover um arquivo                     ",
        vermelho + "[S] Sair" + reset,
    ]

    for opcao in opcoes:
        print(opcao.center(largura))
    
    print()
    print(separador)