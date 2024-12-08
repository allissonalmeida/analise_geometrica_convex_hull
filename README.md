Este protótipo tem por objetivo investigar a aplicabilidade da análise geométrica por visualização interativa na exploração de dados espaciais por posicionamento de jogadores de futebol mediante o desenvolvimento de um protótipo utilizando o algoritmo Convex Hull.

O algoritmo foi desenvolvido em linguagemm Python.
Foram utilizadas as seguintes bibliotecas:

matplotlib.pyplot
from scipy.spatial import ConvexHull
numpy

O algoritmo é composto por 5 funções, são elas:

1. desenhar_campo: configuração do campo de futebol;
2. calcular_distancia: função para calcular distâncias entre os pontos no fecho convexo;
3. atualizar_grafico: função para atualizar o gráfico;
4. encontrar_ponto_mais_proximo: função para encontrar o ponto mais próximo; e
5. onclick: Callback para cliques no gráfico.

Para executar o script, basta executar o arquivo pelo comando no terminal:

python analise_geometrica_convex_hull.py

Obrigado!
