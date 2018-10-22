import random

artigos = ["o", "a", "um", "uma"]
substantivos = ["eu", "gato", "homem", "mulher", "ela", "cachorro"]
verbos = ["cantou", "tocou", "admirou", "falou", "assustou"]
adverbios = ["longíssimo", "inconstitucionalissimamente", "pertinho", "devagarinho", "bem", "afinal"]
all = [artigos, substantivos, verbos, adverbios]

for i in range(5):
    print(artigos[random.randint(0,3)] + " " + substantivos[random.randint(0, 5)] + " " + verbos[random.randint(0, 4)] + " " + adverbios[random.randint(0,5)])
    