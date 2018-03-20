print("Congruencia")

letras = ('','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

msg = input('Mensagem: ')
msg = msg.upper()
msgCrip = ''

for i in msg:
    msgCrip = letras[(letras.index(i)+3) % 26]

print(msgCrip)