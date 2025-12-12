from PIL import Image
import matplotlib.pyplot as plt

# Lista dos gráficos (ordem pensada para leitura acadêmica)
images = [
    "boxplot_tempo.png",
    "violino_tempo.png",
    "hist_tempo.png",
    "boxplot_tamanho.png",
    "violino_tamanho.png",
    "hist_tamanho.png"
]

titles = [
    "Tempo de Resposta – Boxplot",
    "Tempo de Resposta – Violino",
    "Tempo de Resposta – Histograma",
    "Tamanho da Resposta – Boxplot",
    "Tamanho da Resposta – Violino",
    "Tamanho da Resposta – Histograma"
]

# Abre imagens
imgs = [Image.open(img) for img in images]

# Configuração do grid (2 linhas x 3 colunas)
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

for ax, img, title in zip(axes.flatten(), imgs, titles):
    ax.imshow(img)
    ax.set_title(title, fontsize=12)
    ax.axis("off")

# Título geral do dashboard
fig.suptitle(
    "LAB05 – Dashboard Comparativo REST vs GraphQL",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Salva imagem final
plt.savefig("dashboard_lab05.png", dpi=300)
plt.close()

print("Dashboard gerado com sucesso: dashboard_lab05.png")
