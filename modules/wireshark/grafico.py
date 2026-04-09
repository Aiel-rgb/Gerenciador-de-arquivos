import plotext as plt

def grafico_protocolos(df):
    contagem = df['protocolo'].value_counts()

    plt.bar(contagem.index.tolist(), contagem.values.tolist())
    plt.title("Pacotes por Protocolo")
    plt.xlabel("Protocolo")
    plt.ylabel("Quantidade")
    plt.show()
    input("\nPressione Enter para continuar...")

def grafico_ips(df):
    contagem = df['origem'].value_counts().head(10)

    plt.bar(contagem.index.tolist(), contagem.values.tolist())
    plt.title("Top 10 IPs de Origem")
    plt.show()
    input("\nPressione Enter para continuar...")