"""
Seja P=(53412)

534 125   3412   53412 
VAI DAR TUDO CERTO
123 451   2345    12345
AIDVAOUDRTORTCE
P=(53412/12345)

P-1=(45231/12345)
452314523145231
AIDVAOUDRTORTCE
123451234512345

"""
def main():
    head()
    get_option()

def head():
    print('PERMUTAÇÃO')
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
    
def p_reversa(p):
    reversa = ''
    for i in range(0, len(p)):
        reversa = reversa + str(p.index(str(i+1))+1)
    return reversa

def fatiar(msgTrim, p):
    i = 0
    lista = []
    #j = len(p)
    while i < len(msgTrim):
        #if len(part) < len(p):
        #part = part + msgTrim[i]
        lista.append(msgTrim[i:i+len(p)])
        i = i + len(p)
        #elif len(part) == len(p):
        #    lista.append(part)
        #    part = ''
    #lista.append(part)
    return lista

def p_valid(msgTrim, p):
    return len(msgTrim) % len(p) == 0

def criptografia():
    msg = input('Digite a mensagem: ')
    p = input('Digite a chave: ')
    #msg = 'vai dar tudo certo'
    #p = '53412'
    msgTrim = msg.replace(" ", "")
    if p_valid(msgTrim, p):
        lista = fatiar(msgTrim, p)
        s = ""
        i = 0
        for i in range(0, len(lista)):
            for j in range(0, len(lista[i])):
                s = s + lista[i][int(p[j])-1]
        print(s)
    else:
        print('Sua chave não é válida!')


def descriptografia():
    msg = input('Digite a mensagem: ')
    p = input('Digite a chave: ')
    #msg = 'AIDVAOUDRTORTCE'
    #p = '53412'
    msgTrim = msg.replace(" ", "")
    if p_valid(msgTrim, p):
        pRev = p_reversa(p)
        lista = fatiar(msgTrim, p)
        s = ""
        i = 0
        for i in range(0, len(lista)):
            for j in range(0, len(lista[i])):
                s = s + lista[i][int(pRev[j])-1]
        print(s)
    else:
        print('Sua chave não é válida!')

main()