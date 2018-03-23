letras = (('A','B','C','D','E'),('F','G','H','I','J'),('K','L','M','N','O'),('P','R','S','T','U'),('V','W','X','Y','Z'))

def criptografar():
    msg = input('Mensagem: ')
    msg = msg.upper()
    msgCrip = ''
    for letra in msg:
        i = 0
        for i in range(0,len(letras[i])):
            if(letra is 'Q'):
                letra = 'K'
            if(letra in letras[i]):
                msgCrip = msgCrip + str(i+1) + str(letras[i].index(letra)+1) + ' '
            else:
                i = i + 1
        i = 0
    print(msgCrip)
criptografar()