#Altere o programa anterior para mostrar no final a soma dos números.
def Intervalo(x,y):
    primeiro = x
    segundo = y
    soma = 0
    while(segundo != primeiro):
        print("\n",segundo)
        segundo += 1
        soma += segundo
    print("SOMA-->{}".format(soma))


if __name__ == '__main__':
    firt = int(input())
    second = int(input())
    t = True
    while t == True:
        if(firt > second):
            Intervalo(firt,second)
            t = False
        else:
            print("primeiro precisa ser maior que o segundo")
            firt = int(input())
            second = int(input())