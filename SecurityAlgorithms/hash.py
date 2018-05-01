msg = input("Mensagem: ")
msg = msg.replace(' ','')

letras = []

for i in msg:
    if not(msg.count(i) % 2 == 0) and not(i in letras):
        letras.append(i)

for i in range(0,len(letras)):
    letras[i] = ord(letras[i])
print(letras)
divisor = 64
count = 0
resultado = ''
while divisor > 0.5:
#while len(resultado) <= len(letras):
    for i in range(0,len(letras)):
        if letras[i] >= divisor:
            letras[i] = letras[i] % divisor
            count = count + 1
    resultado = resultado + str(int(count % 2))
    count = 0
    divisor = divisor / 2
print(resultado) 