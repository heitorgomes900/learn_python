
def calc_digito(cpf, i, j, soma):
    for i in range(i, len(cpf)):
        soma += int(cpf[i])*j
        j -= 1
        #print("soma: " + str(soma))
    if ((soma % 11) < 2):
        cpf += "0"
        #print("dig: "+digVerif)
    else:
        cpf += str(11 - (soma % 11))
        #print("dig: "+digVerif)
    #print("dig: "+digVerif)
    if not(len(cpf) == 11):
        soma = 0
        i = 0
        j = 11
        calc_digito(cpf, i, j, soma)
    else:
        return cpf 
    
cpf = "123203046" #input("Digite os 9 primeiros dígitos de seu cpf: ")

if(len(cpf) > 9):
    print("Digite apenas 9 dígitos!")
else:
    i = 0
    j = 10
    soma = 0
    print(calc_digito(cpf, i, j, soma))