'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;

misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

#6 metros- 1 litro

#18L- 80 real

#3.6L - 25 real
import math
def ValorTinta(area):
    while(area > 0):
        area = math.ceil((area/6))
        if(area >= 18):
          lata = math.ceil(area/18)
          print("A QUANTIDADE DE LATAS DE 18 LITROS POSSIVEIS {}".format(lata))
          print("PREÇO TOTAL DE LATAS DE 18 LITROS {}".format(math.ceil(lata*80.00)))
          resto = math.ceil(area%18)

        if(resto>3.6):
            print("APROVEITAMENTO DE RESTO DE TINTA, LATAS RESTANTES -> {}".format(int(lata%18)))
            print("PREÇO TOTAL DE GALÕES DE 2,5 LITROS {}".format(math.ceil((lata%18) * 25.00)))
            break # SEGUNDO IF


        if(area<18):
            print("A QUANTIDADE DE GALÕES DE 3.5 LITROS POSSIVEIS {}".format(int(area)))
            print("PREÇO TOTAL DE LATAS DE 3.5 LITROS {}".format(area * 25.00))
        break




if __name__ == '__main__':
    Valor_Area =  float(input("DIGITE A ÁREA:"))
    Porcentagem = Valor_Area*0.10
    Valor_Area = Valor_Area+Porcentagem

    ValorTinta(Valor_Area)