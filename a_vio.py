import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_FILE = "resultados_experimento.csv"

def carregar_dados(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print("\nPrimeiras linhas do dataset:\n", df.head())
    print("\nContagem por tipo de API:\n", df["api_type"].value_counts())
    return df


def estatisticas(df: pd.DataFrame):
    print("\n=========== Estatísticas Descritivas ===========\n")

    for column in ["response_time_ms", "response_size_bytes"]:
        print(f"\n>>> {column}\n")
        print(df.groupby("api_type")[column].agg(["mean", "median", "std", "min", "max"]))


def grafico_violino_tempo(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    sns.violinplot(
        x="api_type",
        y="response_time_ms",
        data=df,
        inner="quartile",
        palette="Set2"
    )
    plt.title("Distribuição do Tempo de Resposta (ms) por Tipo de API")
    plt.xlabel("Tipo de API")
    plt.ylabel("Tempo de Resposta (ms)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig("violino_tempo.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Violino salvo como: violino_tempo.png")


def grafico_violino_tamanho(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    sns.violinplot(
        x="api_type",
        y="response_size_bytes",
        data=df,
        inner="quartile",
        palette="Set2"
    )
    plt.title("Distribuição do Tamanho da Resposta (bytes) por Tipo de API")
    plt.xlabel("Tipo de API")
    plt.ylabel("Tamanho da Resposta (bytes)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig("violino_tamanho.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Violino salvo como: violino_tamanho.png")


def main():
    df = carregar_dados(INPUT_FILE)
    estatisticas(df)
    grafico_violino_tempo(df)
    grafico_violino_tamanho(df)


if __name__ == "__main__":
    main()
