import time
import requests

REST_BASE_URL = "http://localhost:8000/api"
GRAPHQL_URL = "http://localhost:8001/graphql"


def query_rest_movie_by_id(movie_id: int):
    return {
        "method": "GET",
        "url": f"{REST_BASE_URL}/movies/{movie_id}",
        "params": None,
        "json": None
    }


def query_graphql_movie_by_id(movie_id: int):
    query = \"\"\"
    query MovieById($id: ID!) {
      movie(id: $id) {
        id
        title
        year
      }
    }
    \"\"\"
    return {
        "method": "POST",
        "url": GRAPHQL_URL,
        "params": None,
        "json": {"query": query, "variables": {"id": movie_id}}
    }


def measure_request(req_def: dict, repetitions: int = 3):
    tempos = []
    tamanhos = []

    for _ in range(repetitions):
        inicio = time.perf_counter()

        resp = requests.request(
            method=req_def["method"],
            url=req_def["url"],
            params=req_def.get("params"),
            json=req_def.get("json")
        )

        fim = time.perf_counter()

        tempos.append((fim - inicio) * 1000)
        tamanhos.append(len(resp.content))

    return {
        "tempo_medio_ms": sum(tempos) / len(tempos),
        "tamanho_medio_bytes": sum(tamanhos) / len(tamanhos),
        "amostras": repetitions
    }


if __name__ == "__main__":
    rest = query_rest_movie_by_id(1)
    gql = query_graphql_movie_by_id(1)

    print("REST:", measure_request(rest, repetitions=1))
    print("GRAPHQL:", measure_request(gql, repetitions=1))
