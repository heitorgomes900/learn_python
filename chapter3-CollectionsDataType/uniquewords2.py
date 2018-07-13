import string
import sys
import collections

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'" #tira espaços, pontuacao, digitos, "" e ''
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1 #adiciona ocorrencia de palavras
for word in sorted(words):
    print("'{0}' ocorreu {1} vezes".format(word, words[word]))