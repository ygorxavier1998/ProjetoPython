#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

def area(Raio):

    return pow(Raio,2)*math.pi




if __name__ == '__main__':
    Raio = float(input())
    print("AREA DO CIRCULO",area(Raio))