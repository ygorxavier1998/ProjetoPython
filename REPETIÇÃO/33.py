##O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
#programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a,
#maior temperaturas informadas, bem como a média das temperaturas.

import math

def Verificacao(lista):
   
    print("Maior temperatura %f"% max(lista))
    print("Menor Temperatura %f " % min(lista))
    soma = sum(lista)
    #media = soma/(len(lista))
    media = (sum(lista)/len(lista))
    print(" Media Temperatura %f" % media)

if __name__ == '__main__':
    try:
        Dado = float(input("Temperaturas"))
        lista = []
        while(type(Dado)== float):
            lista.append(Dado)
            Dado = float(input("Temperatura:"))
    except BaseException:
        Verificacao(lista)

