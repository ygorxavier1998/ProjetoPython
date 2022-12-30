#Faça um programa que peça 10 números inteiros,
#calcule e mostre a quantidade de números pares e a quantidade de números impares.


def Numero(dado):
    par = 0
    impar = 0
    for x in range(len(dado)):
        if(x%2==0):
            par +=1
        elif(x%2 != 0):
            impar +=1
    print("PAR {}".format(par))
    print("IMPAR {}".format(impar))
    


if __name__ == '__main__':
    entrada = 0
    lista = []
    for x in range(10):
        entrada = int(input())
        lista.append(entrada)
    Numero(lista)
