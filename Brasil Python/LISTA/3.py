#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 

import math


def media(list):
    tamanho = len(list)
    soma = sum(list)
    return soma/tamanho
def main():
    vet4 = []
    for x in range(1,4,1):
        valor = float(input("digite a nota"))
        vet4.append(valor)
    print("{}".format(media(vet4)))

if __name__ == '__main__':
    main()
    