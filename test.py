import random

c = ""
while(len(c)<9):
    i = random.randint(0,9)
    c += str(i)
print(c)