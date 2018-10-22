import os
import sys
from matplotlib import pyplot as plt
from collections import Counter

grades = [8395, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]


def decile(grade): return grade // 10 * 10


histogram = Counter(decile(grade) for grade in grades)

plt.bar(histogram.keys(), histogram.values(), 8) # especifica a largura da barra

plt.axis([-5, 105, 0, 5])   # eixo x de -5 ate 105

# rotulos do eixo x em 0, 10, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decil')
plt.ylabel('# de Alunos')
plt.title('Distribuicao das Notas do teste 1')
plt.show()
