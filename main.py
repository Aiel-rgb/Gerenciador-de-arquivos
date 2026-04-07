from time import sleep
from modules.criar import criacao
from modules.leitua import mostrar_arquivos
from modules.leitua import leituraArquivos
from modules.adicionar import adicionarArquivos
from modules.remover import remocao_dados
from modules.remover import remover_arquivo
from modules.interface import tela

sleep(1)
print('Escolha uma Opção de Manipulação de arquivos')

while True:
    sleep(1.25)
    tela()
    entrada = input("> ")
    if entrada == "1":
        nomeArq = input("Nome do seu arquivo > ").lower().strip()
        criacao(nomeArq)
    elif entrada == "2":
        mostrar_arquivos()
        ler = input("Qual arquivo quer ler? ").lower().strip()
        print("===========")
        leituraArquivos(ler)
        print("===========")
    elif entrada == "3":
        mostrar_arquivos()
        add = input("Qual arquivo deseja adicionar dados? ").lower().strip()
        print("===============")
        adicionarArquivos(add)
        print("===============")
    elif entrada == "4":
        mostrar_arquivos()
        rem = input("Qual dado arquivo você quer deletar? ").lower().strip()
        print("============")
        remocao_dados(rem)
        print("============")
    elif entrada == "5":
        mostrar_arquivos()
        rem = input("Qual arquivo você quer deletar? ").lower().strip()
        print("============")
        remover_arquivo(rem)
        print("============")
    elif entrada.lower().strip() == "sair":
        print("Saindo...") 
        break
    else:
        print("\033[0;31m Escolha uma das alternativas corretamente!\033[0m")
