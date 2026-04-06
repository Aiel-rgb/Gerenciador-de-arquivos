from time import sleep
from modules.criar import criacao
from modules.leitua import mostrar_arquivos
from modules.leitua import leituraArquivos
from modules.adicionar import adicionarArquivos
from modules.interface import tela

print('Escolha uma Opção de Manipulação de arquivos')
tela()
while True:
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
        add = input("Qual arquivo deseja adicionar dados? ")
        print("===============")
        adicionarArquivos(add)
        print("===============")
    elif entrada.lower().strip() == "sair":
        print("Saindo...") 
        break
