#Faça um programa que, dado um conjunto de N números, 
#determine o menor valor, o maior valor e a soma dos valores.

def Quantity(dado):
    print("MININO ",min(dado))
    print("MAXIMO ",max(dado))
    print("SOMA ",sum(dado))


if __name__ == '__main__':
    print("QUANTOS NUMEROS DESEJA SER COMPUTADOR ?")
    Quanti_Numero = int(input())
    lista =[]
    while(Quanti_Numero != 0):
        entrada = int(input("?"))
        lista.append(entrada)
        Quanti_Numero -= 1
        
    Quantity(lista)
