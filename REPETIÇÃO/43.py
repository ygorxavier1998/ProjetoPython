'''
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00


'''
from prettytable import PrettyTable
def main():
    TABELA = PrettyTable()
    TABELA.add_column('Especificação',['Cachorro Quente','Bauru Simples','Bauru com ovo','Hambúrguer','Cheeseburguer','Refrigerante'])
    TABELA.add_column('Código',['100','101','102','103','104','105'])
    TABELA.add_column('preço',['1,20','1,30','1,50','1.20','1,30','1,00'])
    print(TABELA)
#------------------------------------------------------------------------------------------------------------------------------------------#
    print("DIGITE 000 PARA SAIR")
    while(True):
        codigo = int(input("DIGITE O CODIGO DO PRODUTO"))
        if(codigo==000):
            calculo(codigo,quantidade)
            break
        quantidade =int(input("QUANTIDADE"))
        calculo(codigo,quantidade)
      
        

def calculo(codigo,quantidade):
    total_pagar = float
    
    if(codigo==100):
        total_pagar = (quantidade*1.20)
        print("CODIGO: {} VALOR:{} ".format(100,total_pagar))
    elif(codigo==101):
        total_pagar = (quantidade*1.30)
        print("CODIGO: {} VALOR:{} ".format(101,total_pagar))
    elif(codigo==102):
        total_pagar = (quantidade*1.50)
        print("CODIGO: {} VALOR:{} ".format(102,total_pagar))
    elif(codigo==103):
        total_pagar = (quantidade*1.20)
        print("CODIGO: {} VALOR:{} ".format(103,total_pagar))
    elif(codigo==104):
        total_pagar = (quantidade*1.30)
        print("CODIGO: {} VALOR:{} ".format(104,total_pagar)) 
    elif(codigo==105):
        total_pagar = (quantidade*1.00)
        print("CODIGO: {} VALOR:{} ".format(105,total_pagar))

if __name__ == '__main__':
    main()
