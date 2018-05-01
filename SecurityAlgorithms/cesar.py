print("Cesar")

letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

def criptografia():
    msgCrip = ''
    for i in msg:
        msgCrip = msgCrip + letras[(letras.index(i)+3) % 26]
    print(msgCrip)

def descriptografia():
    msgCrip = ''
    for i in msg:
        msgCrip = msgCrip + letras[abs((letras.index(i)-3) % 26)]
    print(msgCrip)

msg = input('Mensagem: ')
msg = msg.upper()
