#Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.
import math

def Area(lado):
    return pow(lado,2)

if __name__ == '__main__':
    Lado = float(input())
    print("ÁREA DO QUADRADO:{} O DOBRO DA ÁREA {}".format(Area(Lado),(2*Area(Lado))))