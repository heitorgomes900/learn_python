letras = ('Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

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
    option = input('  Digite sua opção: ')
    #option = '3'
    if option is '1':
        return criptografia()
    elif option is '2':
        return descriptografia()
    elif option is '3':
        return descobrir_chave()
    return get_option()

def criptografia():
    msg = input("Mensagem: ")
    msg = msg.upper()
    ch = input("Chave: ")
    ch = ch.upper()
    msgTrim = msg.replace(" ", "")
    s = ""
    i = 0
    j = 0
    while i < len(msgTrim): #or j < len(ch):
        if(j == len(ch)):
            j = 0    
        s += letras[((letras.index(msgTrim[i])) + (letras.index(ch[j]))) % 26]
        i = i + 1
        j = j + 1
    print(s)

def descriptografia():
    msg = input("Mensagem Criptografada: ")
    msg = msg.upper()
    ch = input("Chave: ")
    ch = ch.upper()
    msgTrim = msg.replace(" ", "")
    s = ""
    i = 0
    j = 0
    while i < len(msgTrim): #or j < len(ch):
        if(j == len(ch)):
            j = 0    
        s += letras[abs(((letras.index(msgTrim[i])) - (letras.index(ch[j]))) % 26)]
        i = i + 1
        j = j + 1
    print(s)

def descobrir_chave():
    msg = input("Mensagem Criptografada: ")
    msg = msg.upper()
    ch = input("Mensagem: ")
    ch = ch.upper()
    l = input("Tamanho da chave: ")
    try:
        l = int(l)
        msgTrim = msg.replace(" ", "")
        s = ""
        i = 0
        j = 0
        while i < len(msgTrim): #or j < len(ch):
            if(j == len(ch)):
                j = 0    
            s += letras[abs(((letras.index(msgTrim[i])) - (letras.index(ch[j]))) % 26)]
            i = i + 1
            j = j + 1
        print(s[:l])

    except:
        print("O tamanho da chave deve ser inteiro!")
        descobrir_chave()
    

main()



