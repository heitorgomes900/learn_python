letras = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

def main():
    head()
    get_option()

def head():
    print('CIFRAÇÃO')
    print('\n')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('3 - Chave')

def get_option():
    #option = input('  Digite sua opção: ')
    option = '1'
    if option is '1':
        return criptografia()
    elif option is '2':
        return descriptografia()
    elif option is '3':
        return descobrir_chave()
    return get_option()

def criptografia():
    msg = 'upis' #input("Mensagem: ")
    msg = msg.upper()
    ch = 'casa' #input("Chave: ")
    msgTrim = msg.replace(" ", "")
    s = ""
    i = 0
    j = 0
    while i < len(msgTrim): #or j < len(ch):
        if(j == len(ch)):
            j = 0    
        s += letras[(letras.index(msgTrim[i]) + letras.index(ch[j])) % 26]
        i = i + 1
        j = j + 1
    print(s)

def descriptografia():
    msg = input("Mensagem: ")
    '''ch = input("Chave: ")
    #msg = "vaidartudocerto"
    #ch = 5
    msgTrim = msg.replace(" ", "")
    #if ch_valid(msgTrim, ch):
        rows = len(msgTrim) / int(ch)
        s = ""
        i = 0
        while len(s) < len(msgTrim):
            if(i >= len(msgTrim)):
                i = (i % len(msgTrim)) + 1
            s += msgTrim[i]
            i = i + int(ch)
        print(s)
    else:
        print("Sua chave não é válida!")

print("Cesar")'''

def descobrir_chave():
    print("ainda nao está pronto")


main()



