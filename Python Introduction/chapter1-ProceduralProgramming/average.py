numbers = []
count = 0
total = 0
menor = -1 
maior = menor

while True:
    try:
        n = input("Digite um número ou Enter para finalizar: ")
        if n is "":
            break;
        n = int(n)
        if count == 0:
            menor = n
            maior = n
        else:
            if n < menor:
                menor = n
            if n > maior:
                maior = n    
        count += 1
        numbers.append(n)
        total += n    
    except ValueError as err:
        print(err)

print("numbers: ", numbers)
print("count = ", count, " soma = ", total, " menor: ", menor, " maior: ", maior, " media: ", total/count)
