# LAB05 – GraphQL vs REST  

# 1. Desenho do Experimento

## A. Hipóteses

### **RQ1 – Tempo de Resposta**
- **H0₁ (Nula):** Não existe diferença estatisticamente significativa no tempo de resposta entre REST e GraphQL.  
- **H1₁ (Alternativa):** GraphQL apresenta tempo de resposta menor que REST.

### **RQ2 – Tamanho da Resposta**
- **H0₂ (Nula):** Não existe diferença significativa no tamanho (bytes) das respostas entre REST e GraphQL.  
- **H1₂ (Alternativa):** GraphQL retorna payloads menores do que REST.

---

## B. Variáveis Dependentes
- **VD1 – Tempo de resposta (ms)**
- **VD2 – Tamanho da resposta (bytes)**

---

## C. Variáveis Independentes
- **VI1 – Tecnologia da API:**  
  - REST  
  - GraphQL  

- **VI2 – Tipo de consulta (opcional):**  
  - Consulta simples  
  - Consulta com relacionamento  
  - Consulta com filtro/paginação  

---

## D. Tratamentos
- **T1 – REST:** execução das consultas na API REST.  
- **T2 – GraphQL:** execução das mesmas consultas na API GraphQL.

---

## E. Objetos Experimentais

Para este experimento utilizaremos um domínio simples: **Catálogo de Filmes**.

As três consultas utilizadas serão:

### **Q1 – Buscar filme pelo ID**  
- REST → GET `/movies/{id}`  
- GraphQL → query `{ movie(id: ID) { id title year } }`

### **Q2 – Buscar filme + atores relacionados**  
- REST → GET `/movies/{id}/full`  
- GraphQL → query `{ movie(id: ID) { id title year cast { id name } } }`

### **Q3 – Listar filmes com filtro por ano e paginação**  
- REST → GET `/movies?year=YYYY&page=X`  
- GraphQL → query `{ movies(year: YYYY, page: X) { id title year } }`

---

## F. Tipo de Projeto Experimental

O experimento será do tipo:

- **Experimento controlado**
- **Medidas repetidas**
- **Execução em ambiente constante**
- **Comparação direta REST vs GraphQL**

---

## G. Quantidade de Medições

Cada consulta (Q1, Q2, Q3) será executada:

- **N = 30 repetições** para REST  
- **N = 30 repetições** para GraphQL  

Total de medições:  

```
3 consultas × 2 tecnologias × 30 repetições = 180 medições
```

---

# 2. Preparação do Experimento

Para a execução do experimento, adotamos a linguagem Python 3.x como base. Essa escolha se deve à simplicidade para realizar requisições HTTP, medir desempenho e manipular dados posteriormente.
As bibliotecas selecionadas para essa fase incluem:
requests – utilizada para realizar as chamadas REST e GraphQL;
time – empregada para medir o tempo de execução de cada requisição;
json – usada na manipulação de estruturas de dados retornadas pelas APIs;
pandas – destinada ao processamento e análise dos resultados obtidos durante as medições.
Com isso, estruturamos o ambiente inicial do experimento da seguinte forma:
criação de um arquivo requirements.txt contendo as dependências necessárias;
desenvolvimento do arquivo esqueleto_experimento.py, responsável por iniciar e validar o processo de medição;
definição das URLs que serão utilizadas para acessar tanto a API REST quanto a GraphQL;
realização de um teste inicial de comunicação, garantindo que o cliente Python consiga se conectar às duas APIs antes da execução completa do experimento.

---

# 3. Tecnologias que serão utilizadas

## **Backend REST**
- Framework livre  
- Deve expor rotas:
  - `/movies/`
  - `/movies/{id}`
  - `/movies/{id}/full`

## **Backend GraphQL**
- Framework livre  
- Deve expor queries equivalentes:
  - `movie(id)`
  - `movies(year, page)`

---
