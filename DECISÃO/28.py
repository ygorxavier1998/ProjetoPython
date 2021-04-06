'''
 Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg

Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg

Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar
apenas um dos tipos de carne 
da 
promoção, porém não há limites para a quantidade de carne por cliente. 

Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade
de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 

tipo e quantidade de carne,
preço total, tipo de pagamento, 
valor do desconto e valor a pagar.


# int 1 - FILE DUPLO
# int 2 - ALCATRA
# int 3 - PICANHA
'''

from datetime import datetime

def cabecalho():
    print("________________________ BEM VINDO AO MERCADO TABAJARA __________________________")
    print("                       Até 5 Kg                    Acima de 5 Kg")
    print("File Duplo (1)         R$ 4,90 por Kg              R$ 5,80 por Kg")
    print("Alcatra    (2)         R$ 5,90 por Kg              R$ 6,80 por Kg")
    print("Picanha    (3)         R$ 6,90 por Kg              R$ 7,80 por Kg")
    print("_________________________________________________________________________________")

def Preco(Pick,Quantidade): 
    P = Pick
    Q = Quantidade
    if(P==1):       
        if(Q <= 5):
            Total_Preco = (Q*4.90)
            return Total_Preco
        elif(Q > 5):
            Total_Preco = (Q*5.80)
            return Total_Preco

    elif(P==2):        
        if(Q <= 5):
            Total_Preco = Q*5.90
            return Total_Preco
        elif(Q > 5):
            Total_Preco = Q*6.80
            return Total_Preco

    elif(P==3):
        if(Q <= 5):
            Total_Preco = Q*6.90
            return Total_Preco
        elif(Q> 5):
            Preco = Q*7.80
            return Preco

def Desconto(Valor):
    x = Valor
    return Valor*0.05

def NotaFiscal(TipoCarne,PreCoTotal,TipoPagamento,Desconto): 
    now = datetime.now()
    D = int(Desconto)
    print("|________________________OBRIGADO POR COMPRAR__________________________|")
    print("{} - {} - {}".format(now.year,now.day,now.hour))
    print("|TIPOS DE CARNE {}".format(TipoCarne)) 
    print("|DESCONTO: {}|".format(D))
    print("|TIPO DE PAGAMENTO {}|".format(TipoPagamento))   
    print("|PREÇO A SER PAGO {}|".format(PreCoTotal))  
    print("|______________________________________________________________________|")

    


if __name__ == '__main__':
    Quanti_Item = 2
    cabecalho()
    Total_Pagar = 0
    cartao_desc = 0.05 #5%
    PNota=[]
    while(Quanti_Item > 0):
        print("QUANTIDADE MAXIMA DE PRODUTO POR CLIENTE {}".format(Quanti_Item))
        Escolha = int(input("DIGITE SUA ESCOLHA?\n"))
        Quantidade_Produto = int(input("QUANTIDADE \n"))
    
        if(Escolha==1):
            Total_Pagar1 = Preco(Escolha,Quantidade_Produto)
            Quanti_Item -=1
        elif(Escolha==2):
            Total_Pagar1 = Preco(Escolha,Quantidade_Produto)
            Quanti_Item -=1
        elif(Escolha==3):
            print("pick 3") 
            Total_Pagar1 = Preco(Escolha,Quantidade_Produto)
            Quanti_Item -=1
        else:
            print("ERRO DE ENTRADA")
            Quanti_Item = 0

        PNota.append(int(Escolha))                                          #
        print("QUANTIDADE DE PRODUTOS POSSIVEIS A RETIRADA: {}".format(Quanti_Item))
        print("DESEJA MAIS PRODUTOS:")
        cont =  input("S->SIM\nN->NAO").upper()
        if(cont=="N"):
            print("QUAL A FORMA DE PAGAMENTO CARTÃO:?")
            print("CARTÃO TABAJARA(1)\nDINHEIRO(2)\nCARTÃO DE DEBITO(3)")
            Escolha_Pagamento = int(input("ESCOLHA DE PAGAMENTO\n"))
            if(Escolha_Pagamento==1):
                valor = Desconto(Total_Pagar1)
                Total_Pagar = Total_Pagar1-valor
                NotaFiscal(PNota,Total_Pagar,"CARTÃO TABAJARA",valor)
                break
            elif(Escolha_Pagamento==2):
                valor = 0
                Total_Pagar = Total_Pagar1-valor
                NotaFiscal(PNota,Total_Pagar,"DINHEIRO",valor)
                break
            elif(Escolha_Pagamento == 3):
                valor = 0              
                Total_Pagar = Total_Pagar1-valor
                NotaFiscal(PNota,Total_Pagar,"CARTÃO DEBITO",valor)
                break
            Quanti_Item = 0




        elif(cont=="S"):
            print("QUANTIDADE DE PRODUTO POR CLIENTE {}".format(Quanti_Item))
            Escolha = int(input("DIGITE SUA ESCOLHA?\n"))
            PNota.append(int(Escolha)) 
            Quantidade_Produto = int(input("QUANTIDADE?\n"))
            if(Escolha==1):
                Total_Pagar2 = Preco(Escolha,Quantidade_Produto)
                Total_Pagar = Total_Pagar1+Total_Pagar2
                Quanti_Item -=1
            elif(Escolha==2):
                Total_Pagar2 = Preco(Escolha,Quantidade_Produto)
                Total_Pagar = Total_Pagar1+Total_Pagar2
                Quanti_Item -=1
            elif(Escolha==3):
                Total_Pagar2 = Preco(Escolha,Quantidade_Produto)
                Total_Pagar = Total_Pagar1+Total_Pagar2
                Quanti_Item -=1
            else:
                print("ESCOLHA ERRDA")
                Total_Pagar = Total_Pagar1+Total_Pagar2
                print("TOTAL A PAGAR{}".format(Total_Pagar))
                Quanti_Item = 0

 
        
            print("QUAL A FORMA DE PAGAMENTO CARTÃO:?")
            print("CARTÃO TABAJARA(1)\nDINHEIRO(2)\nCARTÃO DE DEBITO(3)")

            Escolha_Pagamento = int(input("ESCOLHA DE PAGAMENTO\n"))
            if(Escolha_Pagamento==1):
                valor = Desconto(Total_Pagar) 
                Total_Pagar = Total_Pagar-valor
                NotaFiscal(PNota,Total_Pagar,"CARTÃO",valor)
            elif(Escolha_Pagamento==2):
                valor = 0
                Total_Pagar = Total_Pagar-valor
                NotaFiscal(PNota,Total_Pagar,"DINHEIRO",valor)
                NotaFiscal(PNota,Total_Pagar,"0",valor)
            elif(Escolha_Pagamento == 3):
                valor = 0
                Total_Pagar = Total_Pagar-valor
                NotaFiscal(PNota,Total_Pagar,"CARTÃO DEBITO",valor)
                NotaFiscal(PNota,Total_Pagar,"0",valor)
            