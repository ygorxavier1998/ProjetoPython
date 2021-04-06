#Faça um Programa que leia três números
#e mostre o maior deles


import math
def maior(a,b,c):
    maximo = a
    if (b>maximo):
        maximo=b
    elif(c>maximo):
        maximo =c

    return maximo

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(maior(a,b,c))