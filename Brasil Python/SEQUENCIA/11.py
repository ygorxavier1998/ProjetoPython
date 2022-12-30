#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
import math
def produto(a,b):
    int(a)
    int(b)

    return ((2*a)+(b/2))

def soma(a,b,c):
    int(a)
    int(b)
    float(c)
    soma = (a*3)+c
    return soma
def ele(c):
    return math.pow(c,2)



if __name__ == '__main__':
    primeiro= int(input())
    segundo = int(input())
    terceiro = float(input())

    print("o produto do dobro do primeiro com metade do segundo",produto(primeiro,segundo))
    print("a soma do triplo do primeiro com o terceiro.", soma(primeiro,segundo,terceiro))
    print("o terceiro elevado ao cubo.", ele(terceiro))
