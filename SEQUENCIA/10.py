#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def convert(Temperatura_Cel):
    float(Temperatura_Cel)
    Temperatura_Fahr = (Temperatura_Cel*(9/5)+32)

    return Temperatura_Fahr


if __name__ == '__main__':
    Temp_Cel = float(input())
    print("temperatura em CELSIUS {}, temperatura em FAHRENHEIT {} ".format(Temp_Cel,convert(Temp_Cel)))