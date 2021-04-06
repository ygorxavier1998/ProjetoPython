#Faça um programa que leia 5 números
#e informe a soma e a média dos números.
import math as mate


def Maior(lista):
    soma = sum(lista)
    print("{}".format(soma))
    media = soma/5
    print("{}".format(media))



if __name__ == '__main__':
    ls = []
    a = float(input())
    ls.append(a)
    b = float(input())
    ls.append(b)
    c = float(input())
    ls.append(c)
    d = float(input())
    ls.append(d)
    e = float(input())
    ls.append(e)  
    Maior(ls)