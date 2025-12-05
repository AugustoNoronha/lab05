# run_experiment.py
import time
import json
import requests
import pandas as pd
from typing import Dict, Any, List

# ==========================
# CONFIGURAÇÕES DO EXPERIMENTO
# ==========================

NUM_TRIALS = 50  # número de repetições por API

# API REST REAL (funciona 100%)
REST_URL = "https://jsonplaceholder.typicode.com/posts/1"

# API GraphQL REAL (funciona 100%)
GRAPHQL_URL = "https://graphql-pokeapi.graphcdn.app/"

COMMON_HEADERS = {
    "Content-Type": "application/json"
}

# REST não precisa de params, mas deixamos configurado
REST_PARAMS = {}

# GraphQL Query real
GRAPHQL_QUERY = """
query {
  pokemon(name: "pikachu") {
    id
    name
    height
    weight
  }
}
"""

GRAPHQL_BODY = {
    "query": GRAPHQL_QUERY,
    "variables": {}
}

# ==========================
# FUNÇÕES DE MEDIÇÃO
# ==========================

def medir_requisicao_rest(trial: int) -> Dict[str, Any]:
    inicio = time.perf_counter()
    response = requests.get(REST_URL, headers=COMMON_HEADERS, params=REST_PARAMS)
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000.0
    tamanho_bytes = len(response.content)

    return {
        "trial": trial,
        "api_type": "REST",
        "status_code": response.status_code,
        "response_time_ms": tempo_ms,
        "response_size_bytes": tamanho_bytes
    }


def medir_requisicao_graphql(trial: int) -> Dict[str, Any]:
    inicio = time.perf_counter()
    response = requests.post(
        GRAPHQL_URL,
        headers=COMMON_HEADERS,
        data=json.dumps(GRAPHQL_BODY)
    )
    fim = time.perf_counter()

    tempo_ms = (fim - inicio) * 1000.0
    tamanho_bytes = len(response.content)

    return {
        "trial": trial,
        "api_type": "GraphQL",
        "status_code": response.status_code,
        "response_time_ms": tempo_ms,
        "response_size_bytes": tamanho_bytes
    }

# ==========================
# EXECUÇÃO DO EXPERIMENTO
# ==========================

def executar_experimento(num_trials: int) -> pd.DataFrame:
    resultados: List[Dict[str, Any]] = []

    print(f"Executando {num_trials} trials REST...")
    for i in range(1, num_trials + 1):
        r = medir_requisicao_rest(i)
        resultados.append(r)
        print(f"[REST] Trial {i}/{num_trials} - "
              f"{r['response_time_ms']:.2f} ms, {r['response_size_bytes']} bytes, status {r['status_code']}")

    print(f"\nExecutando {num_trials} trials GraphQL...")
    for i in range(1, num_trials + 1):
        r = medir_requisicao_graphql(i)
        resultados.append(r)
        print(f"[GraphQL] Trial {i}/{num_trials} - "
              f"{r['response_time_ms']:.2f} ms, {r['response_size_bytes']} bytes, status {r['status_code']}")

    df = pd.DataFrame(resultados)
    return df

# ==========================
# MAIN
# ==========================

def main():
    df = executar_experimento(NUM_TRIALS)
    output_file = "resultados_experimento.csv"
    df.to_csv(output_file, index=False)
    print(f"\nExperimento concluído! Resultados salvos em: {output_file}")
    print(df.head())

if __name__ == "__main__":
    main()
