'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg


Se o cliente comprar mais de 
8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 

Escreva um algoritmo para ler a quantidade 
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''  

#MORANGO = M
#MAÇA = A
def Frut(Pick,Quantidade):
    PrecoMorango = 2.50
    PrecoMaca = 1.80
    Total_Preco = 0

    if(Pick == "M"):
        print("ESCOLHA:MORAGO")
        if(Quantidade <= 5 ):                                 # SE QUANTIDADE FOR MENOR QUE 5 OU IGUAL 5 
            Total_Preco = Quantidade*PrecoMorango
            return Total_Preco

        elif(Quantidade > 5 or Quantidade > 8):              # SE A QUANTIDADE FOR MAIOR QUE 5 OU MAIOR QUE 8                               # POSSUI UM DESCONTO DE 10% EM CIMA DO SEU VALOR
            Total_Preco = Quantidade*2.20

            if(Total_Preco >25.00 or Quantidade > 8 ):
                Desconto = Total_Preco*0.10
                return Total_Preco-Desconto
            else:
                Total_Preco = Quantidade*2.20
                return Total_Preco

    if(Pick == "A"):
        print("ESCOLHA:MAÇA")
        if(Quantidade <= 5 ):                                 # SE QUANTIDADE FOR MENOR QUE 5 OU IGUAL 5 
            Total_Preco = Quantidade*PrecoMaca
            return Total_Preco

        elif(Quantidade > 5 or Quantidade > 8):              # SE A QUANTIDADE FOR MAIOR QUE 5 OU MAIOR QUE 8 # POSSUI UM DESCONTO DE 10% EM CIMA DO SEU VALOR
            Total_Preco = Quantidade*1.50
            if(Total_Preco >25.00 or Quantidade > 8 ):
                Desconto = Total_Preco*0.10
                return Total_Preco-Desconto
            else:
                Total_Preco = Quantidade*1.50
                return Total_Preco
    
if __name__ == '__main__':
    Saida = "C"
    while(Saida=="C"):
        print("DIGITE [A] PARA MAÇA \nDIGITE [M] PARA MORANGO")
        Entrada = input().upper()
        Quantidade = float(input("QUANTIDADE A SER COMPRADA"))
        Total = Frut(Entrada,Quantidade)
        if(Entrada=="A" or Entrada=="S"):
            print("MAIS ALGUMA FRUTA?")
            Continue = input("S->SIM \nN->NÃO").upper()
            if(Continue=="S"):
                print("DIGITE [A] PARA MAÇA \nDIGITE [M] PARA MORANGO")
                Entrada = input().upper()
                Quantidade = float(input())
                Total2 = Frut(Entrada,Quantidade)
                print("TOTAL-->{}".format(Total+Total2))
                Saida = " "
                
            else:
                print("TOTAL-->{}".format(Total))
                Saida = " "
        else:
            print("ERRO DE ENTRDADA")
            Saida = " "