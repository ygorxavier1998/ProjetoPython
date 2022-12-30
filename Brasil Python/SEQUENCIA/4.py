#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
import math
def Media(nota1,nota2,nota3,nota4):
    soma = nota1+nota2+nota3+nota4
    return soma/4



if __name__ == '__main__':
    notas1 = int(input())
    notas2 = int(input())
    notas3 = int(input())
    notas4 = int(input())

    print(Media(notas1,notas2,notas3,notas4))