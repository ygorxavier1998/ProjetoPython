#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#  Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def calte(numero):
    resto = (numero)
    mmc = 0
    # numero =! 1
    #while(numero != 1):
    for x in range(1,100):
        resto = (resto/x)
        var = round(resto-0.5)
        #print(x , resto, var , var==resto)
        if(round(resto)==resto):
        #verdade = type(resto)
        #if(verdade==int):
            mmc+=1
        elif(var != resto):
            x+=1
        if(resto==1 or resto==0):
            break
    print("MMC",mmc)
    if(mmc < 2 ):
        print("PRIMO")
    else:
        print("não primo")

if __name__ == '__main__':
    entrada = int(input())
    calte(entrada)
    