def main():
    head()
    get_option()

def head():
    print('TRANSPOSIÇÃO')
    print('\n')
    print('1 - Criptografar')
    print('2 - Descriptografar')

def get_option():
    option = input('  Digite sua opção: ')
    #option = '1'
    if option is '1':
        return criptografia()
    elif option is '2':
        return descriptografia()
    return get_option()

def ch_valid(msgTrim, ch):
    return len(msgTrim) % int(ch) == 0

def criptografia():
    msg = input("Mensagem: ")
    ch = input("Chave: ")
    msgTrim = msg.replace(" ", "")
    if ch_valid(msgTrim, ch):
        rows = len(msgTrim) / int(ch)
        s = ""
        i = 0
        while len(s) < len(msgTrim):
            if(i >= len(msgTrim)):
                i = (i % len(msgTrim)) + 1
            s += msgTrim[i]
            i = i + int(rows)
        print(s)

def descriptografia():
    msg = input("Mensagem: ")
    ch = input("Chave: ")
    #msg = "vaidartudocerto"
    #ch = 5
    msgTrim = msg.replace(" ", "")
    if ch_valid(msgTrim, ch):
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

main()



