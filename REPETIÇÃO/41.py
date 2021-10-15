'''
TABELA DE JUROS 

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
'''
from prettytable import PrettyTable

def calculo(x,p):
    divida = x
    parcela = p
    Tabela_Juros = PrettyTable()
    Tabela_Juros.add_row(["Valor da Dívida", "Valor dos Juros" ,"Quantidade de Parcelas","Valor da Parcela"])
    
    if(parcela == 1):
        porcentagem = divida*(0)
        divida += porcentagem 
        Tabela_Juros.add_row([divida,porcentagem,parcela,divida])
        print(Tabela_Juros)
    elif(parcela==3):
        porcentagem = divida*(10/100)
        divida += porcentagem 
        Tabela_Juros.add_row([divida,porcentagem,parcela,round(divida/parcela,2)])
        print(Tabela_Juros)
    elif(parcela==6):
        porcentagem = divida*(15/100)
        divida += porcentagem 
        Tabela_Juros.add_row([divida,porcentagem,parcela,round(divida/parcela,2)])
        print(Tabela_Juros)
    elif(parcela==9):
        porcentagem = divida*(20/100)
        divida += porcentagem 
        Tabela_Juros.add_row([divida,porcentagem,parcela,round(divida/parcela,2)])
        print(Tabela_Juros)
    elif(parcela==12):
        porcentagem = divida*(25/100)
        divida += porcentagem 
        Tabela_Juros.add_row([divida,porcentagem,parcela,round(divida/parcela,2)])
        print(Tabela_Juros)


def main():
    
    tabela = PrettyTable()
    tabela.add_column('Quantidade',[1,3,6,9,12])
    tabela.add_column('Juros',['0','10%','15%','20%','25%'])
    print(tabela)
    
    entreda = float(input("DIGITE O VALOR DA DIVIDA:"))
    parcelar = int(input("DIGITE A QUANTIDADE DE PARCELAS:"))

    calculo(entreda,parcelar)
if __name__ == '__main__':
    main()
