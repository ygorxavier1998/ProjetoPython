#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 

def retorno(firt,second,tird):
    ListRet = []
    for x,y,z in zip(firt,second,tird):
        ListRet.append(x)
        ListRet.append(y)
        ListRet.append(z)

    return ListRet

def main():
    vet1 = []
    vet2 = []
    vet3 =[]
    
    for x in range(5):
        y = input("Digite o elemento do {} do Vet 1".format(x))
        vet1.append(y)
        y = input("Digite o elemento do {} do Vet 2".format(x))
        vet2.append(y)
        y = input("Digite o elemento do {} do Vet 3".format(x))
        vet3.append(y)
        
    for x in retorno(vet1,vet2,vet3):
        print(x)
if __name__ == '__main__':
    main()
    