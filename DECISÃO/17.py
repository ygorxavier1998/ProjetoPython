'''Faça um Programa que peça um número correspondente a um determinado ano e 
em seguida informe se este ano é ou não bissexto.


São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
x = 400/entrada
São bissextos todos os múltiplos de 4, 
exceto se for múltiplo de 100 mas não de 400, 
p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...

1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024,
 2028, 2032, 2036, 2040, 2044, 2048, 2052, ... .
'''
def AnoBixesto(x):
    Multipli_Cem = x%100
    Multipli_Quatro = x%4 
    Multipli_Quatrocentro = x%400
    if(x % 400)==0:
        return print("ANO BIXESTO")
    
    elif(Multipli_Quatro==0):
        if(Multipli_Cem != 0):
            if(Multipli_Quatrocentro != 0):
                return print("ANO BIXESTO")
  
    return print("NÃO ANO BIXESTO")

if __name__ == '__main__':
    X = int(input())
    AnoBixesto(X)