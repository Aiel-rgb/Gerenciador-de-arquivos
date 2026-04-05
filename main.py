from time import sleep
from modules.criar import criacao
from modules.leitua import mostrar_arquivos
from modules.leitua import leituraArquivos


print('Escolha uma Opção de Manipulação de arquivos')
while True:
    sleep(2)
    print("----------------------------------------------")
    print(
        "|[1] Criar Arquivo                          |\n"
        "|[2] Ler Arquivo                            |\n"
        "|[3] Mostrar pasta de arquivos              |\n"
        "|[?] .......................................|\n"
        "|[?] .......................................|\n"
        "|[?] .......................................|\n"
        "|[?] .......................................|\n"
        "|[?] .......................................|\n"
    )
    print("----------------------------------------------")

    entrada = input("> ")
    if entrada == "1":
        nomeArq = input("Nome do seu arquivo > ")
        criacao(nomeArq)
    elif entrada == "2":
        mostrar_arquivos()
        ler = input("Qual arquivo quer ler? ")
        print("===========")
        leituraArquivos(ler)
        print("===========")
    elif entrada == "3":
        mostrar_arquivos()
    elif entrada.lower().strip() == "sair":
        print("Saindo...") 
        break
