import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Lista para armazenar os pontos
points = []

# Configuração do campo de futebol
def desenhar_campo(ax):
    ax.set_xlim(0, 105)  # Comprimento do campo (em metros)
    ax.set_ylim(0, 68)   # Largura do campo (em metros)
    ax.set_aspect('equal', adjustable='box')
    
    # Desenhando o campo
    ax.plot([0, 105, 105, 0, 0], [0, 0, 68, 68, 0], 'green')  # Linhas externas
    ax.plot([52.5, 52.5], [0, 68], 'green', linestyle='--')  # Linha central
    circle = plt.Circle((52.5, 34), 9.15, color='green', fill=False)  # Círculo central
    ax.add_patch(circle)

# Função para calcular distâncias entre os pontos no fecho convexo
def calcular_distancia(hull, points):
    distances = []
    for i in range(len(hull.vertices)):
        p1 = points[hull.vertices[i]]
        p2 = points[hull.vertices[(i + 1) % len(hull.vertices)]]
        distance = np.linalg.norm(p2 - p1)
        distances.append(distance)
    return distances

# Função para atualizar o gráfico
def atualizar_grafico():
    plt.cla()
    desenhar_campo(ax)
    
    # Desenhar os pontos
    if points:
        x, y = zip(*points)
        ax.scatter(x, y, c='blue', label='Pontos')

    # Calcular e desenhar o Convex Hull
    if len(points) > 2:
        hull = ConvexHull(points)
        hull_points = np.append(hull.vertices, hull.vertices[0])  # Fechar o loop
        ax.plot(np.array(points)[hull_points, 0], np.array(points)[hull_points, 1], 'r-', label='Convex Hull')
        
        # Calcular área e distâncias
        area = hull.area
        distances = calcular_distancia(hull, np.array(points))
        
        # Mostrar informações
        info_text = f"Área: {area:.2f} m²\nDistâncias: " + ", ".join(f"{d:.2f}m" for d in distances)
        ax.text(40, 70, info_text, fontsize=10, va="bottom", ha="center", bbox=dict(facecolor='white', alpha=0.5))
    
    ax.legend()
    plt.draw()

# Função para encontrar o ponto mais próximo
def encontrar_ponto_mais_proximo(x, y, points):
    min_dist = float('inf')
    nearest_point = None
    for point in points:
        dist = np.sqrt((point[0] - x) ** 2 + (point[1] - y) ** 2)
        if dist < min_dist:
            min_dist = dist
            nearest_point = point
    return nearest_point, min_dist

# Callback para cliques no gráfico
def onclick(event):
    global points

    # Verifica se o clique foi dentro do campo
    if event.xdata is not None and event.ydata is not None:
        if 0 <= event.xdata <= 105 and 0 <= event.ydata <= 68:
            x, y = event.xdata, event.ydata
            
            # Verifica se há um ponto próximo para remoção (distância limite: 2 metros)
            nearest_point, dist = encontrar_ponto_mais_proximo(x, y, points)
            if dist < 2:
                points.remove(nearest_point)  # Remove o ponto mais próximo
            else:
                points.append([x, y])  # Adiciona um novo ponto

            atualizar_grafico()

# Configurando o campo de futebol
fig, ax = plt.subplots(figsize=(10, 6))
desenhar_campo(ax)

# Conectar evento de clique
fig.canvas.mpl_connect('button_press_event', onclick)

# Mostrar o gráfico
plt.title("Clique para adicionar ou remover pontos\nConvex Hull com área e distâncias calculadas")
plt.show()
