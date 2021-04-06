#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
#Dica: utilize uma função de arredondamento.

def ret(x):
    if(round(x)==x):
        return True
    else:
        return False
    

if __name__=='__main__':
    entrada = float(input())

    if(ret(entrada)==True):
        print("INTEIRO")
    else:
        print("DECIMAL")
