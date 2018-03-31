msg = input("Mensagem: ")

letras = []
c = 1
i = 0
while i < len(msg):
    if msg[i] in letras:
        i = i + 1
        continue
    for j in range(i+1,len(msg)):
        if(msg[i] is msg[j]):
            c = c + 1 
    if c % 2 == 0:
        msg = msg.replace(msg[i],'')
        c = 1
        i = 0
        continue
    else:
        letras.append(msg[i])
    c = 1
    i = i + 1

for i in range(0,len(letras)):
    letras[i] = ord(letras[i])

divisor = 64
count = 0
resultado = ''
#while divisor > 0.5:
while len(resultado) <= len(letras):
    for i in range(0,len(letras)):
        if letras[i] >= divisor:
            letras[i] = letras[i] % divisor
            count = count + 1
    resultado = resultado + str(int(count % 2))
    count = 0
    divisor = divisor / 2
print(resultado) 