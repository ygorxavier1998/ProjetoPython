#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme
#e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

def convert(Temperatura_Fahr):
    Temperatura_Cel = 5*((Temperatura_Fahr-32)/9)
    return Temperatura_Cel


if __name__ == '__main__':
    Temp_Faht = float(input())
    print("temperatura em Fahrenheit {}, temperatura em CELSIUS {} ".format(Temp_Faht,convert(Temp_Faht)))