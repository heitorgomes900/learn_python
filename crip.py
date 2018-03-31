msg = input("Mensagem: ")
ch = input("Chave: ")
#msg = "vaidartudocerto"
#ch = 5

msgTrim = msg.replace(" ", "")
print(msgTrim)

try:
    if(len(msgTrim) % int(ch) == 0):
        rows = len(msgTrim) / int(ch)
        #lista = []
        s = ""
        i = 0
        #for i in range(0,len(msgTrim),int(rows)):
        while len(s) < len(msgTrim):
            #if(int(rows) > (len(msgTrim)-i)):
            if(i >= len(msgTrim)):
                #i = abs(i-len(msgTrim))+1
                i = (i % len(msgTrim)) + 1
            s += msgTrim[i]
            #print("primeiro i: ",i)
            i = i + int(rows)
            #print("segundo i: ",i)
        print(s)
    else:
        print("erro")
except EOFError as err:
    print(err)
