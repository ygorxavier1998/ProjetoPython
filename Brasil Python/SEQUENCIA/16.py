'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''


# 1 litro -> 3 metros
# 2 litros -> 4 metros

# 1 lata -> 18 litros
# 1 lata -> 80.00
def valor(Area):
    float(Area)
    Valor_Litros = area/3

    while(Valor_Litros > 0):
        if Valor_Litros >= 18:
            print("QUANTIDADES DE LATAS NECESSARIAS {:.0f}".format(Valor_Litros/18))
            print("VALOR A SER PAGO {:.2f}".format((Valor_Litros / 18)*80))
            break
        else:
            print("VALOR NÃO SUFICIENTE PARA A VENDA, MININO 18 LITROS")
            break

if __name__ == '__main__':
    area = float(input("ÁREA A SER PINTADA"))
    valor(area)