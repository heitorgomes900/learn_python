from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2013, 2014], mentions, 0.8)
plt.xticks(years)
plt.xlabel("# de vezes que ouvimos alguem dizer 'Data Science'")

# se voce nao fizer isso, matplotlib nomeara o eixo x de 0, 1
# e entao adiciona a +2.013e3 para fora do canto 
plt.ticklabel_format(useOffset=False)

# enganar o eixo y mostra apenas a parte acima de 500
plt.axis([2012.5,2014.5,499,506])
plt.title('Olhe o "Grande" Aumento!')
plt.show()