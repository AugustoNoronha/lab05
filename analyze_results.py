# analyze_results.py
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "resultados_experimento.csv"

def carregar_dados(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # sanity check básico
    print("Primeiras linhas do dataset:")
    print(df.head())
    print("\nContagem por tipo de API:")
    print(df["api_type"].value_counts())
    return df


def estatisticas_descritivas(df: pd.DataFrame):
    print("\n=== Estatísticas descritivas por tipo de API ===\n")

    metrics = ["response_time_ms", "response_size_bytes"]

    for metric in metrics:
        print(f"\nMétrica: {metric}")
        resumo = df.groupby("api_type")[metric].agg(
            ["count", "mean", "median", "std", "min", "max"]
        )
        print(resumo)


def gerar_boxplot_tempo(df: pd.DataFrame, output_file: str = "boxplot_tempo.png"):
    plt.figure()
    df.boxplot(column="response_time_ms", by="api_type")
    plt.title("Tempo de resposta (ms) por tipo de API")
    plt.suptitle("")  # remove título automático do pandas
    plt.xlabel("Tipo de API")
    plt.ylabel("Tempo de resposta (ms)")
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()
    print(f"Boxplot de tempo salvo em: {output_file}")


def gerar_boxplot_tamanho(df: pd.DataFrame, output_file: str = "boxplot_tamanho.png"):
    plt.figure()
    df.boxplot(column="response_size_bytes", by="api_type")
    plt.title("Tamanho da resposta (bytes) por tipo de API")
    plt.suptitle("")
    plt.xlabel("Tipo de API")
    plt.ylabel("Tamanho da resposta (bytes)")
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()
    print(f"Boxplot de tamanho salvo em: {output_file}")


def main():
    df = carregar_dados(INPUT_FILE)
    estatisticas_descritivas(df)
    gerar_boxplot_tempo(df)
    gerar_boxplot_tamanho(df)


if __name__ == "__main__":
    main()
