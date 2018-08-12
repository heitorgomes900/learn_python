import string
import sys
import collections

def by_value(item):
    return item[1]

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'" #tira espaços, pontuacao, digitos, "" e ''
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1 #adiciona ocorrencia de palavras
for word, count in sorted(words.items(), key=by_value):
    print("'{0}' ocorreu {1} vezes".format(word, words[word]))