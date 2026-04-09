def selecionar_colunas(df, preferidas):
    return [c for c in preferidas if c in df.columns]


def exibir_tabela(df, colunas=None):
    if colunas is None:
        colunas = selecionar_colunas(df, ["No.", "Time", "origem", "destino", "protocolo", "Length"])
    if not colunas:
        print("Nenhuma coluna disponível para exibição.")
        return
    print(df[colunas].to_string(index=False))

def exibir_pagina(df, pagina=1, por_pagina=20):
    inicio = (pagina - 1) * por_pagina
    fim = inicio + por_pagina

    fatia = df.iloc[inicio:fim]
    colunas = selecionar_colunas(fatia, ["No.", "Time", "origem", "destino", "protocolo", "Length"])
    print(f"\n=== Página {pagina} - pacotes {inicio + 1} a {min(fim, len(df))} de {len(df)} ===")
    if colunas:
        print(fatia[colunas].to_string(index=False))
    else:
        print("Nenhuma coluna disponível para exibição.")
    print(f"\n[P] Próxima  |  [V] Voltar  |  [ENTER OU QUALQUER TECLA] Sair")
