##Faça um programa que peça 10 números inteiros, calcule e mostre a 
#quantidade de números pares e a quantidade de números impares.

def Quanti(dado):
    NumPar = 0
    NumIpar = 0
    for x in  dado:
        if(x%2==0):
            NumPar += 1
        elif(x%2==1):
            NumIpar +=1

    print("--->",NumPar)
    print("--->",NumIpar)




if __name__ == '__main__':
    lista = []
    for x in range(10):
        entrada = int(input())
        lista.append(entrada)
    
    Quanti(lista)
