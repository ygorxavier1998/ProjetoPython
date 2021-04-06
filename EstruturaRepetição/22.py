#Altere o programa de cálculo dos números primos, informando,
#caso o número não seja primo, por quais número ele é divisível.


def Call_back(x):
    number  = x
    if(number%2==0):
        return True
    elif(number%2 != 0):
        print("NUMERO PRIMO")
        for x in range(1,100):
            if(number%x==0):
                print("NUMEROS DIVISICEIS {}".format(x))
            

if __name__ == '__main__':
    numero = int(input())
    if(Call_back(numero)==True):
        print("par")
    else:
        print("não primo")
