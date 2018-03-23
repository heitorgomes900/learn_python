import sys

letras = ('','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

def main():
    head()
    if(get_option() == 1):
        criptograr()
    else:
        descriptografar()
    
def head():
    print('Congruência')
    print('\n')
    print('Escolha sua opção')
    print('\n')
    print('1 - Criptografar')
    print('2 - Descriptografar')

def get_int(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = int(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("Zero não é permitido!")
                x = None
        except ValueError as err:
                print(err)
    return x

def get_option():
    opt = input()
    if opt is 1 or opt is 2:
        print('Digite 1 ou 2!')
        return get_option()
    return opt

def criptograr():
    print('ainda não pronto')

def descriptografar():
    a = get_int("a: ",False)
    b = get_int("b: ",True)
    msg = input("Mensagem: ")
    msg = msg.upper()
    s = ""
    n = 1
    if(len(msg)>0):
        for i in range(0, len(msg)):
            y = (letras.index((msg[i])))-(int(b)) + n * 26
            #print(y)
            while y % a != 0:
                y = y + 26
                n = n + 1
            y = y / int(a)
            while int(y) < 0:
                    y = y + 26
            while int(y) > 26:
                y = y - 26
            s = s + letras[int(y)]
    print(s)

main()