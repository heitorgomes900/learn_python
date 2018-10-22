from matplotlib import pyplot as plt

text_1_grades = [99, 90, 85, 97, 80]
text_2_grades = [100, 85, 60, 90, 70]

plt.scatter(text_1_grades, text_2_grades)
plt.title('Os eixos nao sao compativeis')
plt.xlabel('nota do teste 2')
plt.ylabel('nota do teste 1')
plt.show()
