#Faça um programa que receba dois números
#inteiros e gere os números inteiros que estão no intervalo compreendido por eles.



def Intervalo(x,y):
    primeiro = x
    segundo = y
    while(segundo != primeiro):
        print("\n",segundo)
        segundo += 1


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