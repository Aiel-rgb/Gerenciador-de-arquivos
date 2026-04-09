def ver_protocolo(df,protocolo):
    filtrado = df[df["protocolo"] == protocolo.upper()]

    if filtrado.empty:
        print(f"Nenhum pacote {protocolo} encontrado.")
        return
    
    print(f"\n=== {protocolo.upper()} - {len(filtrado)} pacotes ===")
    colunas = [c for c in ["No.", "Time", "origem", "destino", "Length", "Info"] if c in filtrado.columns]
    if not colunas:
        colunas = [c for c in ["origem", "destino", "protocolo", "Length"] if c in filtrado.columns]
    print(filtrado[colunas].to_string(index=False))
    input("\nPressione Enter para continuar...")

def ver_dns(df):
    ver_protocolo(df, "DNS")

def ver_http(df):
    ver_protocolo(df, "HTTP")

def ver_tcp(df):
    ver_protocolo(df, "TCP")

def ver_ip(df, ip):
    filtrado = df[(df['origem'] == ip) | (df['destino'] == ip)]
    print(f"\n=== IP {ip} - {len(filtrado)} pacotes ===")
    colunas = [c for c in ["No.", "Time", "origem", "destino"] if c in filtrado.columns]
    if not colunas:
        colunas = [c for c in ["origem", "destino", "protocolo", "Length"] if c in filtrado.columns]
    print(filtrado[colunas].to_string(index=False))