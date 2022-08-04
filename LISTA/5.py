#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 
def DataAnalicts(list):
    vetPar = []
    vetInpar  = []
    for x in list:
        number = x%2
        if(number==0):
            vetPar.append(x)
        else:
            vetInpar.append(x)
    print("P - >{} /I - >{}/ entrada - >{} ".format(vetPar,vetInpar,list))
def main():
    vetPrime = []
    for x in range(1,10):
        entrada = int(input("Entrada"))
        vetPrime.append(entrada)
    DataAnalicts(vetPrime)
if __name__ == '__main__':
    main()
