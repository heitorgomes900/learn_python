import random

artigos = ["o", "a", "um", "uma"]
substantivos = ["eu", "gato", "homem", "mulher", "ela", "cachorro"]
verbos = ["cantou", "tocou", "admirou", "falou", "assustou"]
adverbios = ["longíssimo", "inconstitucionalissimamente", "pertinho", "devagarinho", "bem", "afinal"]

lines = 5
versos = input("Digite o número de versos ou Enter para pular: ")
if(len(versos) > 0):
    try:
        tmp = int(versos)
        if(1 <= tmp <= 10):
            lines = tmp
        else:
            print("Os versos devem ser entre 1 e 10")
    except ValueError:
        print("usage: {} [lines]".format(__file__))

def random_word(seq):
    return random.choice(seq)

#while lines:
for i in range(1, lines + 1):
    sentence = [random_word(artigos), random_word(substantivos), random_word(verbos)]
    if random.randint(0, 1):
        pass
    else:
        sentence.append(random_word(adverbios))
    print(*sentence)
    #lines -= 1