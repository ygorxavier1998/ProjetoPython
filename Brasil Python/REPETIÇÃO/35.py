#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
#existentes entre 1 e um número inteiro informado pelo usuário.

def primos(numero):
    mmc = 0
    divisor = 2
    for x in range(2,numero):
        resto = x
        for y in range(1,100):
            if(x%4==0):
                break
            resto = resto/divisor
            if(round(resto)==resto): # SE A DIVISÃO FOR INTERIRA O NUMERO X E IGUAL A O MMC
                mmc+=1
                divisor = 2
            elif(round(resto) != resto):
                divisor += 1
                resto = x
            if(round(resto)==1 or round(resto)==0):
                if(mmc < 2):
                    print("NUMERO PRIMO {}  ".format(x,))
                    mmc = 0
                    break
                else:
                    mmc = 0
                  


if __name__ == '__main__':
    entrada = int(input())
    primos(entrada)
