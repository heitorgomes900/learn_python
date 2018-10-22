import os
import sys
from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

# barras possuem o tamanho padrao de 0.8, entao adicionaremos 0.1 as coordenadas
# a esquerda para cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(movies)]

# as barras do grafico com as coordenadas x a esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel('# de Premiacoes')
plt.title('Meus Filmes Favoritos')

plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()