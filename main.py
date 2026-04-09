from modules.criar import criacao
from modules.leitua import mostrar_arquivos
from modules.leitua import leituraArquivos
from modules.adicionar import adicionarArquivos
from modules.remover import remocao_dados
from modules.remover import remover_arquivo
from modules.interface import tela
from modules.wireshark.importar import importar, listar_arquivos_entrada, listar_arquivos_convertidos
from modules.wireshark.dataframe import carregar, resumo
from modules.wireshark.filtros import ver_dns, ver_http, ver_tcp, ver_ip
from modules.wireshark.tabela import exibir_tabela, exibir_pagina
from modules.wireshark.grafico import grafico_protocolos, grafico_ips

current_df = None

print('Escolha uma Opção de Manipulação de arquivos')

while True:
    tela()
    entrada = input("> ").lower().strip()
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
    elif entrada == "6":
        listar_arquivos_entrada()
        nome = input("Nome do arquivo em Shark_csvs (sem extensão): ").strip()
        current_df = importar(nome)
    elif entrada == "7":
        if current_df is None:
            print("Nenhum dataframe carregado. Importe ou carregue um primeiro.")
        else:
            print("Escolha filtro:")
            print("[1] DNS")
            print("[2] HTTP")
            print("[3] TCP")
            print("[4] Por IP")
            filtro = input("> ").strip()
            if filtro == "1":
                ver_dns(current_df)
            elif filtro == "2":
                ver_http(current_df)
            elif filtro == "3":
                ver_tcp(current_df)
            elif filtro == "4":
                ip = input("Digite o IP: ").strip()
                ver_ip(current_df, ip)
    elif entrada == "8":
        if current_df is None:
            print("Nenhum dataframe carregado.")
        else:
            pagina = 1
            while True:
                exibir_pagina(current_df, pagina)
                cmd = input("> ").lower().strip()
                if cmd == "p":
                    pagina += 1
                elif cmd == "v":
                    pagina = max(1, pagina - 1)
                else:
                    break
    elif entrada == "9":
        if current_df is None:
            print("Nenhum dataframe carregado.")
        else:
            print("Escolha gráfico:")
            print("[1] Protocolos")
            print("[2] IPs de origem")
            graf = input("> ").strip()
            if graf == "1":
                grafico_protocolos(current_df)
            elif graf == "2":
                grafico_ips(current_df)
    elif entrada == "10":
        listar_arquivos_convertidos()
        nome = input("Nome do arquivo em Shark_csvs/convertidos (sem extensão): ").strip()
        current_df = carregar(nome)
        if current_df is not None:
            resumo(current_df)
    elif entrada in {"sair", "s"}:
        print("Saindo...")
        break
    else:
        print("\033[0;31m Escolha uma das alternativas corretamente!\033[0m")
