numbers = []
count = 0
total = 0
menor = -1 
maior = menor

def ordenaVetor(numbers):
    tmp = 0
    i = 0
    j = i + 1
    for i in range(i,len(numbers)-1):
        for j in range(j,len(numbers)):
            if numbers[i] > numbers[j]:
                tmp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
    return numbers

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

if len(numbers) % 2 == 0:
    meio = int(numbers[int(len(numbers)/2)-1]) + int(numbers[int((len(numbers)/2))])
else:
    meio = int(numbers[int(len(numbers)/2)])  

numbers = ordenaVetor(numbers)
print("numbers: ", numbers)
print("count = ", count, " soma = ", total, " menor: ", menor, " maior: ", maior, " media: ", total/meio)
