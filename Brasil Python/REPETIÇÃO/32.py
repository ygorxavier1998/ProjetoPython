#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120
import math

if __name__ == '__main__':

    entrada = int(input())
    soma = 0
    for numero in range(entrada,1,-1):
        if(numero==entrada):
            soma = (numero*(numero-1))
            numero -= 1
        else:
            numero -= 1
            soma += (soma*(numero -1))

    for numero in range(entrada,1,-1):
        print(numero ,end="*")
    print("1 =",soma)
