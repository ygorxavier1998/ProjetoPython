'''
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

 
Escreva um algoritmo que leia o número de
litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina 
é  o preço do litro do álcool é
'''
import math

def preco(E,Quantidade):
    PrecoAlcool = 1.90
    PrecoGasolina = 2.50
    if(E=="A"):
        print("ALCOOL\nPREÇO: {}".format(PrecoAlcool))
        if(Quantidade <= 20 ):
            print("DESCONTO DE 3%")
            desconto = ((Quantidade*PrecoAlcool)*0.03)
            preco = (Quantidade*PrecoAlcool)-desconto
            return preco
        elif(Quantidade > 20):
            print("DESCONTO DE 5%")
            desconto = ((Quantidade*PrecoAlcool)*0.05)
            preco = (Quantidade*PrecoAlcool)-desconto
            return preco

    elif(E=="B"):
        print("GASOLINA\nPREÇO: {}".format(PrecoGasolina))
        if(Quantidade <= 20 ):
            print("DESCONTO DE 4%")
            desconto = ((Quantidade*PrecoAlcool)*0.04)
            preco = (Quantidade*PrecoAlcool)-desconto
            return preco
        elif(Quantidade > 20):
            print("DESCONTO DE 6%")
            desconto = ((Quantidade*PrecoGasolina)*0.06)
            preco = (Quantidade*PrecoGasolina)-desconto
            return preco
'''
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
R$ 2,50
'''
        

if __name__ == '__main__':
    
    print("ESCOLHA O TIPO DE COMBUSTIVEL")
    print("A - ÁLCOOL\nB - GASOLINA")
    Pick = input("?").upper()
    print("QUANTIDADE DE COMBUSTIVEL")
    Quanti = int(input())
    if(Pick=="A"):
        print("{:.2f}".format(preco(Pick,Quanti)))
    elif(Pick=="B"):
        print("{:.2f}".format(preco(Pick,Quanti)))
    else:
        print("ERRO DE ENTRDA")

