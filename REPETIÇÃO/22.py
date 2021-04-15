#Altere o programa de cálculo dos números primos, informando,
#caso o número não seja primo, por quais número ele é divisível.

def calte(numero):
    resto = (numero)
    mmc = 0
    lista = []
    # numero =! 1
    #while(numero != 1):
    for x in range(1,numero):
        resto = (resto/x)
        if(round(resto)==resto): # SE A DIVISÃO FOR INTERIRA O NUMERO X E IGUAL A O MMC
            mmc+=1
            print(resto)
        elif(round(resto) != resto):
                if(numero%x==0):
                    lista.append(x)
                else:
                    x+=1
        if(resto==1 or resto==0):
            break
    print("MMC",mmc)
    if(mmc < 2 ):
        print("PRIMO")
    else:
        print("não primo")
        print(lista)

if __name__ == '__main__':
    entrada = int(input())
    calte(entrada)
    