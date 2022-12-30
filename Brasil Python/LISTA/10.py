#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos 
#elementos intercalados dos dois outros vetores. 




def retorno(firt,second):
    ListRet = []
    for x,y in zip(firt,second):
        ListRet.append(x)
        ListRet.append(y)
            
    return ListRet

def main():
    vet1 = []
    vet2 = []
    
    for x in range(5):
        y = input("Digite o elemento do {} do Vet 1".format(x))
        vet1.append(y)
        y = input("Digite o elemento do {} do Vet 2".format(x))
        vet2.append(y)
    for x in retorno(vet1,vet2):
        print(x)
if __name__ == '__main__':
    main()
    