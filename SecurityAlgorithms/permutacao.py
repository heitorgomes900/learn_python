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
    while i < len(msgTrim):
        lista.append(msgTrim[i:i+len(p)])
        i = i + len(p)
    return lista

def p_valid(msgTrim, p):
    return len(msgTrim) % len(p) == 0

def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 
    
def multiplicar(p):
    result = 1
    for i in p:
        result = result * int(i)
    return result

def criptografia():
    msg = input('Digite a mensagem: ')
    p = input('Digite a chave: ')
    #msg = 'vai dar tudo certo'
    #p = '53412'
    msgTrim = msg.replace(" ", "")
    if p_valid(msgTrim, p):
    #if multiplicar(p) is fatorial(len(p)):
        lista = fatiar(msgTrim, p)
        s = ""
        i = 0
        for i in range(0, len(lista)):
            for j in range(0, len(lista[i])):
                s = s + lista[i][int(p[j])-1]
        print(s)
    #else:
    #    print('Sua chave não é válida!')
    else:
        print('Sua chave não é válida!')


def descriptografia():
    msg = input('Digite a mensagem: ')
    p = input('Digite a chave: ')
    #msg = 'AIDVAOUDRTORTCE'
    #p = '53412'
    msgTrim = msg.replace(" ", "")
    if p_valid(msgTrim, p):
    #if multiplicar(p) is fatorial(len(p)):
        pRev = p_reversa(p)
        lista = fatiar(msgTrim, p)
        s = ""
        i = 0
        for i in range(0, len(lista)):
            for j in range(0, len(lista[i])):
                s = s + lista[i][int(pRev[j])-1]
        print(s)
    #else:
    #    print('Sua chave não é válida!')
    else:
        print('Sua chave não é válida!')
main()